# File Encryptor/Decryptor Program

# Variable Names Used
'''user_pass, password, salt, kdf, key,message,
original_message, test, choice, encoded, encrypted,
decoded, decrypted, data1, data2, encrypted1,
decrypted 2, f1, f2, f3, f4, f5, f6, f7, f8, f9'''

# Importing Modules/Libraries
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Defining/Asking For A Master Password Which Will be Linked To A Unique Key
user_pass = input("Enter Master Password:")
password = user_pass.encode()
# Generate Using A Key From 'os.urandom(16)', Must Be Of 'byte' Data Type
salt = b'salt'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can Use kdf Only Once
print(key)

# Storing The Key To A File
f1 = open("key.key", 'wb')
f1.write(key)
f1.close()

# Asking User For Their Message
message = input("Enter Your Message:")
test = open("test.txt", 'w')
test.write(message)
test.close()

# Asking User What To Do
choice = int(input('''What would you like to do?
1. Print Encrypted Message On Screen and in File.
2. Print Decrypted Message On Screen and in File.
3. Encryt File
4. Decrypt File.
Enter from above choices(1, 2, 3 or 4)'''))

if choice == 1:
    # Encode Message
    encoded = message.encode()
    # Encrypting Message
    f2 = Fernet(key)
    encrypted = f2.encrypt(encoded)
    f3 = open("EncryptedData.txt", 'wb')
    f3.write(encrypted)
    f3.close()
    print("Message Encrypted!")

elif choice == 2:
    # Decrypting Message
    encoded = message.encode()
    f2 = Fernet(key)
    encrypted = f2.encrypt(encoded)
    f4 = Fernet(key)
    dercypted = f4.decrypt(encrypted)
    # Decode Message
    original_message = dercypted.decode()
    f5 = open("DecryptedData.txt", 'w')
    f5.write(original_message)
    f5.close()
    print("File Decrypted. Data in file:", original_message)

elif choice == 3:
    # Encrypting Complete File
    f6 = open("test.txt", 'rb')
    data1 = f6.read()
    fernet = Fernet(key)
    encrypted1 = fernet.encrypt(data1)
    f6.close()
    # Writing To An Encrypted File
    f7 = open("test.ncryptd", 'wb')
    f7.write(encrypted1)
    f7.close()
    print("Encrypted File Created. Delete Original File If Necessary.")

elif choice == 4:
    # Decrypting Complete File
    f8 = open("test.ncryptd", 'rb')
    data2 = f8.read()
    fernet = Fernet(key)
    decrypted1 = fernet.decrypt(data2)
    f8.close()
    # Writing To A Decrypted File
    f9 = open("test.dcryptd", 'wb')
    f9.write(decrypted1)
    print("File Decrypted.")
    f9.close()