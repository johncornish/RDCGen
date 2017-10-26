import yaml, re
from os.path import isfile
from functools import reduce

class GroupTree:
    def __init__(self, datafile=False):
        if not datafile:
            self._datafile = "RDCMan_custom.rdg"
        else:
            self._datafile = datafile

        if not isfile(self._datafile):
            print("{} not found. It will be created on save.".format(self._datafile))
            
        self._datatree = {}

    def dump_dict(d):
        return yaml.dump(d, default_flow_style=False)
           
    def save(self):
        self.normalize_tree()
        output = str(self)
        with open(self._datafile, 'w') as f:
            f.write(output)

    def __str__(self):
        return GroupTree.dump_dict(self._datatree)

    def keys_from_path(self, path):
        return [k for k in self.branch_from_path(path).keys() if not re.match('^_.*', str(k))]
                    
    def merge_server(self, path, server_name, server_data):
        node = self.branch_from_path(path)
        node['_servers'].update({server_name: server_data})

    def delete_branch(self, path):
        node = self.branch_from_path(path[:-1])
        if len(path) >= 1:
            delete_key = path[-1]
            if delete_key in node:
                del node[delete_key]
            else:
                print("{} not found in tree:".format(' > '.join(map(str, path))))
                print(str(self))

    def branch_from_path(self, path):
        node = self._datatree
        for p in path:
            if p not in node:
                node[p] = {'_servers': {}}

            node = node[p]

        return node
