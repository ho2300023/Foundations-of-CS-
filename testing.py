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

def test_is_prime():
    print("Testing for prime number: ")
    if is_prime(2):
        print("Test passed: 2 is prime.")
    else:
        print("Test failed: 2 is prime.")

    if not is_prime(4):
        print("Test passed: 4 is not prime.")
    else:
        print("Test failed: 4 is not prime.")

    if is_prime(13):
        print("Test passed: 13 is prime.")
    else:
        print("Test failed: 13 is prime.")

def test_is_primitive_root():
    print("Testing for prime numbers: ")
    P = 7
    if is_primitive_root(3, P):
        print("Test passed: 3 is a primitive root of 7.")
    else:
        print("Test failed: 3 is a primitive root of 7.")

    if not is_primitive_root(2, P):
        print("Test passed: 2 is not a primitive root of 7.")
    else:
        print("Test failed: 2 is not a primitive root of 7.")

def test_generate_prime_and_primitive_root():
    print("Testing prime and primitive generation: ")
    P, G = generate_prime_and_primitive_root()
    if is_prime(P):
        print(f"Test passed: {P} is prime.")
    else:
        print(f"Test failed: {P} is not prime.")

    if is_primitive_root(G, P):
        print(f"Test passed: {G} is a primitive root of {P}.")
    else:
        print(f"Test failed: {G} is not a primitive root of {P}.")

def test_key_generation():
    print("Testing key generation: ")
    public_key, private_key = key_generation()
    P, G, E = public_key
    if is_prime(P):
        print(f"Test passed: {P} is prime.")
    else:
        print(f"Test failed: {P} is not prime.")

    if is_primitive_root(G, P):
        print(f"Test passed: {G} is a primitive root of {P}.")
    else:
        print(f"Test failed: {G} is not a primitive root of {P}.")

    if 1 <= private_key < P - 1:
        print(f"Test passed: {private_key} is a valid private key.")
    else:
        print(f"Test failed: {private_key} is not a valid private key.")

    if E == pow(G, private_key, P):
        print("Test passed: Public key component E is correct.")
    else:
        print("Test failed: Public key component E is incorrect.")

def test_encrypt_decrypt():
    print("Testing encryption and decryption: ")
    public_key, private_key = key_generation()
    message = random.randint(1, public_key[0] - 1)
    cipher_text = encrypt(public_key, message)
    decrypted_message = decrypt(private_key, public_key, cipher_text)
    if decrypted_message == message:
        print(f"Test passed: Original Message: {message}, Encrypted: {cipher_text}, Decrypted: {decrypted_message}.")
    else:
        print(f"Test failed: Original Message: {message}, Encrypted: {cipher_text}, Decrypted: {decrypted_message}.")

def all_tests():
    test_is_prime()
    test_is_primitive_root()
    test_generate_prime_and_primitive_root()
    test_key_generation()
    test_encrypt_decrypt()

if __name__ == "__main__":
    all_tests()


