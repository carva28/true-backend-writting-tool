from OpenSSL.crypto import *

passwd = b'ZBfCHxtjWJ_6werd'
p12 = load_pkcs12(open('deca-true_ua_pt.pfx', 'rb').read(), passwd)

pkey = p12.get_privatekey()
open('pkey.pem', 'wb').write(dump_privatekey(FILETYPE_PEM, pkey))

cert = p12.get_certificate()
open('cert.pem', 'wb').write(dump_certificate(FILETYPE_PEM, cert))

ca_certs = p12.get_ca_certificates()
ca_file = open('ca.pem', 'wb')
for ca in ca_certs:
   ca_file.write(dump_certificate(FILETYPE_PEM, ca))

