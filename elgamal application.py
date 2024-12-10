import random 

def is_prime(n):  #This function Checks if a number is prime.
    if n <= 1:  # Prime numbers must be greater than 1.
        return False
    for i in range(2, int(n**0.5) + 1):  #Loops from 2 to root n.
        if n % i == 0:  #If n is divisible with 0 remainder, it's not a prime number.
            return False
    return True  #If n is prime it returns true as prime.

def is_primitive_root(g, p):  #This function Checks if g is a primitive root of p.
    required_set = set(num for num in range(1, p) if num < p)  #This function declares the required set to be a primitive root,.
    actual_set = set(pow(g, powers, p) for powers in range(1, p))  # The actuall generated set.
    return required_set == actual_set  #Returns true if both sets match together.

def generate_prime_and_primitive_root():  #This function Generates a random prime number with its primitive root.
    while True:  #Loops until valid prime and primitive root are found.
        P = random.randint(100, 1000)
        if is_prime(P):  #This loop checks if the number is prime using the prime checker function.
            while True:
                G = random.randint(2, P - 1)  #Generates a integer in the range 2 to p-1 for the primitive root.
                if is_primitive_root(G, P):  #If function to makes sure if it’s a primitive root.
                    return P, G 

def key_generation():  #This function generates public and private keys.
    P, G = generate_prime_and_primitive_root()  #Generates P and G.
    A = random.randint(1, P - 2)  #Private key A is randomly chosen within the range 1 to P-2.
    E = pow(G, A, P)  #E = g^a mod p
    return (P, G, E), A 

def encrypt(public_key, message):  #This function encrypts a message with the public key.
    P, G, E = public_key  #Declaring the public key as p , g , e.
    B = random.randint(1, P - 2)  #Random integer used for encryption.
    C1 = pow(G, B, P)  #Calculates the first part of encrypted message.
    C2 = (message * pow(E, B, P)) % P  #Calculated the second part of the encrypted message.
    return C1, C2  

def decrypt(private_key, public_key, cipher_text):  #This function decrypts the ciphertext with the private key.
    P, G, E = public_key  #Declaring the public key as p , g , e.
    A = private_key  
    C1, C2 = cipher_text  
    s = pow(C1, A, P)  #Calculate s with c1^a mod p.
    s_inv = pow(s, P - 2, P)  #alculatesS inverse with s^p-2 mod p.
    message = (C2 * s_inv) % P  #pulls the decrypted message after decrypting it.
    return message 

def main():  
    print("ElGamal Encryption Applocation")  
    
    public_key, private_key = key_generation()  #Key generation.
    while True:  # This loop lets the user select as many options until selects exit.
        print(f"Public Key: {public_key}") 
        print(f"Private Key: {private_key}")  
        choice = input("Enter (1)'encrypt' or (2)'decrypt', or (3)'exit'): ")  
        print("-------------")
        if choice == '1': 
            message = int(input("Enter the message you'd like to encrypt (as an integer): ")) 
            print("-------------")
            cipher_text = encrypt(public_key, message) 
            print(f"Encrypted Message: {cipher_text}")  
            print("=============")
        elif choice == '2':  
            C1 = int(input("Enter (C1): ")) 
            print("-------------")
            C2 = int(input("Enter (C2): ")) 
            print("-------------")
            cipher_text = (C1, C2) 
            decrypted_message = decrypt(private_key, public_key, cipher_text)  
            print(f"Decrypted Message: {decrypted_message}")  
            print("=============")
        elif choice == '3':  # If the user chooses to exit.
            break  # Exits the loop and program when user selects exit option.
        else: 
            print("Invalid choice. Please enter (1)'encrypt', (2)'decrypt', or (3)'exit'.")  
            
if __name__ == "__main__":
    main()  # Calls the main function.
