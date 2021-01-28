from cryptography.fernet import Fernet
def write_key():
 keys = Fernet.generate_keys()
 with open('C:/Users/Desktop/keys.key' 'wb') as keys_file:
  keys_file.write(key)

def load_keys():
 return open('C:/Users/Desktop/keys.key' 'rb').read()

def decryp(filename, keys):
 f = Fernet(keys)
 with open(filename, 'rb') as file:
  encryp_data = file.read()
  decryp_data = f.decrypt(encryp_data)
  with open(filename, 'wb') as file:
   file.write(decryp_data)
   
def encryp(filename, keys):
 f = Fernet(keys)
 with open(filename, 'rb') as file:
  file_data = file.read()
  encryp_data = f.encryp(file_data)
  with open(filename, 'wb') as file:
   file.write(encryp_data)

 keys = load_key()
 file = 'C:/Users/Desktop/keyS.txt'

write_key()
 
