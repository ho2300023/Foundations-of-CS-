import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p) if num < p)
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

def generate_prime_and_primitive_root():
    while True:
        P = random.randint(100, 1000)
        if is_prime(P):
            while True:
                G = random.randint(2, P - 1)
                if is_primitive_root(G, P):
                    return P, G

def key_generation():   
    P, G = generate_prime_and_primitive_root()
    A = random.randint(1, P - 2)
    E = pow(G, A, P)
    return (P, G, E), A

def encrypt(public_key, message):
    P, G, E = public_key   
    B = random.randint(1, P - 2)      
    C1 = pow(G, B, P)
    C2 = (message * pow(E, B, P)) % P
    return C1, C2

def decrypt(private_key, public_key, cipher_text):
    P, G, E = public_key
    A = private_key
    C1, C2 = cipher_text   
    s = pow(C1, A, P)   
    s_inv = pow(s, P - 2, P)    
    message = (C2 * s_inv) % P 
    return message

def main():
    print("ElGamal Encryption Applocation")
    
    public_key, private_key = key_generation()
    while True:
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
        elif choice == '3':
                break
        else:
            print("Invaliid choice. Please enter (1)'encrypt', (2)'decrypt', or (3)'exit'.")
            

if __name__ == "__main__":
    main()
