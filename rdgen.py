import click, os, itertools, pprint
from ldap3 import Server, Connection, NTLM, ALL
from ldap3 import ObjectDef, AttrDef, Reader

usr = "ADIT\\{}".format(click.prompt('Username'))
psswd = os.environ['PSS']
#psswd = click.prompt('Password', hide_input=True)

def get_computers():
    ## Search is limited by server to 1000 results, but we have 1200+, so breaking up search to next OU level
    server = Server('corsair.adit.mines.edu', use_ssl=True, get_info=ALL)
    with Connection(server, user=usr, password=psswd, authentication=NTLM, auto_bind=True, read_only=True) as conn:
        entry_generator = conn.extend.standard.paged_search(
            search_base = 'ou=classrooms-win10,ou=csm computers,dc=adit,dc=mines,dc=edu',
            search_filter = '(objectclass=computer)',
            generator=True
        )
        return entry_generator

computers = get_computers()
for c in computers:
    print(c)
    break
## Debugging notes:
## 
## Install requirements
##
##   pip install -r requirements.txt
##
## View results with colorizing
##
##   echo username | python rdcgen.py | ccze -A
##
## Count results
##
##   echo username | python rdcgen.py | ccze -A | wc -l
##
## Save results to file
##
##    echo jnorris | python rdcgen.py > ~/results.txt
##
## Create environment variable PSS and store password or an LM:NTLM hash of password there
## To generate the LM:NTLM password, run the following commands, then join the results with a ':'
## character and store that in the PSS variable.
##
##    apt-get install freeradius-utils
##    smbencrypt Myp\@\$\$word
##    export PSS=123123123123123123123123123:123123123123123123123123123

