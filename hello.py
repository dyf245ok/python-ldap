import ldap
ldapServer = 'LDAP://192.168.99.100'
password = '1234567890'
domainUserName = 'cn=admin,dc=my-company,dc=com'
#password = 'admin'
#domainUserName = 'cn=admin,dc=example,dc=org'
try:
    conn = ldap.initialize(ldapServer)
    conn.simple_bind_s(domainUserName, password)
    print('success')
except:
    print('failed')
    