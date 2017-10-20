import click, os
from ldap3 import Server, Connection, ALL, NTLM

usr = 'ADIT\\cornish'
psswd = os.environ['PSS']
#psswd = click.prompt('Password', hide_input=True)

server = Server('corsair.adit.mines.edu', use_ssl=True, get_info=ALL)
with Connection(server, user=usr, password=psswd, authentication=NTLM, auto_bind=True) as conn:
    conn.search('ou=classrooms-win10,ou=csm computers,dc=adit,dc=mines,dc=edu', '(objectclass=computer)')
    entry = conn.entries[0]
    data = entry.entry_to_json()
    print(data)
    #print([e.entry_to_json() for e in conn.entries])
    # print(conn.extend.standard.who_am_i())
    # print(conn)

