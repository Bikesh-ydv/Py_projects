import random;
import string;

word = string.ascii_letters + " " + string.digits + string.punctuation;

words = list(word);


keys = words.copy();


random.shuffle(keys);
#Encryption

original_message = input("Enter message to encrypt:");
encrypted_message = "";

for letter in original_message:
    index = words.index(letter);
    encrypted_message += keys[index];
print(f"Original Message :{original_message}");
print(f"Encrypted Message:{encrypted_message}");

#Decryption

encrypted_message= input("Enter message to encrypt:");
original_message = "";

for letter in encrypted_message:
    index = keys.index(letter);
    original_message += words[index];
print(f"Original Message :{encrypted_message}");
print(f"Encrypted Message:{original_message}");