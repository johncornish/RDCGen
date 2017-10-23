import click, os, itertools, pprint
from ldap3 import Server, Connection, NTLM, ALL
from ldap3 import ObjectDef, AttrDef, Reader

usr = "ADIT\\{}".format(click.prompt('Username'))
psswd = os.environ['PSS']
#psswd = click.prompt('Password', hide_input=True)

server = Server('corsair.adit.mines.edu', use_ssl=True, get_info=ALL)
with Connection(server, user=usr, password=psswd, authentication=NTLM, auto_bind=True) as conn:
    conn.search('ou=classrooms-win10,ou=csm computers,dc=adit,dc=mines,dc=edu', '(objectclass=computer)')
    print(conn.entries)
    # ^^use this, the cursor sucks
