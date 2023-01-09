import OpenSSL.crypto
import os

pfx_cert = 'deca-true_ua_pt.pfx'
pfx_password = b'ZBfCHxtjWJ_6werd'

###########################################################    
# Version 1.00
# Date Created: 2018-12-21
# Last Update:  2018-12-21
# https://www.jhanley.com
# Copyright (c) 2018, John J. Hanley
# Author: John Hanley
###########################################################

# Convert a Google P12 (PFX) service account into private key and certificate.
# Convert an SSL Certifcate (PFX) into private key, certificate and CAs.

def write_CAs(filename, p12):
   # Write the Certificate Authorities, if any, to filename

   if os.path.exists(filename):
      os.remove(filename)

   ca = p12.get_ca_certificates()

   if ca is None:
      return

   print('Creating Certificate CA File:', filename)

   with open(filename, 'wb') as f:
      for cert in ca:
            f.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))

def pfx_to_pem(pfx_path, pfx_password, pkey_path, pem_path, pem_ca_path):
   '''
   Decrypt the P12 (PFX) file and create a private key file and certificate file.

   Input:
      pfx_path    INPUT: This is the Google P12 file or SSL PFX certificate file
      pfx_password    INPUT: Password used to protect P12 (PFX)
      pkey_path   INPUT: File name to write the Private Key to
      pem_path    INPUT: File name to write the Certificate to
      pem_ca_path INPUT: File name to write the Certificate Authorities to
   '''

   print('Opening:', pfx_path)
   with open(pfx_path, 'rb') as f_pfx:
      pfx = f_pfx.read()

   print('Loading P12 (PFX) contents:')
   p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)

   print('Creating Private Key File:', pkey_path)
   with open(pkey_path, 'wb') as f:
      # Write Private Key
      f.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))

   print('Creating Certificate File:', pem_path)
   with open(pem_path, 'wb') as f:
      # Write Certificate
      f.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))

   # Google P12 does not have certifiate authorities but SSL PFX certificates do
   write_CAs(pem_ca_path, p12)

# Start here

pfx_to_pem(
   pfx_cert,         # Google Service Account P12 file
   pfx_password,     # P12 file password
   'llama.key',      # Filename to write private key
   'llama_cert.pem', # Filename to write certificate
   'llama_ca.pem')   # Filename to write CAs if present