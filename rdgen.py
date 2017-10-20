import click, os, itertools, pprint
from ldap3 import Server, Connection, NTLM, ALL
from ldap3 import ObjectDef, AttrDef, Reader

usr = 'ADIT\\cornish'
psswd = os.environ['PSS']
#psswd = click.prompt('Password', hide_input=True)

server = Server('corsair.adit.mines.edu', use_ssl=True, get_info=ALL)
with Connection(server, user=usr, password=psswd, authentication=NTLM, auto_bind=True) as conn:
    # conn.search('ou=classrooms-win10,ou=csm computers,dc=adit,dc=mines,dc=edu', '(objectclass=computer)')
    # print(conn.entries)

    computer = ObjectDef('computer', conn)
    computer += 'cn'
    computer += 'ou'

    #r = Reader(conn, computer, base='ou=classrooms-win10,ou=csm computers,dc=adit,dc=mines,dc=edu', sub_tree=False, query='type: computer')
    r = Reader(conn, computer, 'ou=classrooms-win10,ou=csm computers,dc=adit,dc=mines,dc=edu', '')
    #r.search_subtree(paged_size=5)
    pp = pprint.PrettyPrinter(indent=4)
    r.search_paged(paged_size=5)
    print(len(r.entries))
    for computer in itertools.islice(r.entries, 1):
        print(computer)
        #print(computer)
        #pp.pprint(computer['attributes'].keys())
        # print(computer.cn)
        # print([ou for ou in computer])

    # entry = r.entries
    # data = entry.entry_to_json()
    # print(entry)
    # print([e.entry_to_json() for e in conn.entries])
    # print(conn.extend.standard.who_am_i())
    # print(conn)

