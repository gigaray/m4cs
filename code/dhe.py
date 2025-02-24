import random

'''
A primitive root modulo p is a number g where g's powers (g^1, g^2, g^3, ..., g^(p-1)) generate 
all numbers from 1 to p-1 when taken modulo p. Each power must generate a unique number.

'''
def is_primitive_root(g, p):
    """
    Check if g is a primitive root modulo p
    """
    # Generate all numbers from 1 to p-1
    numbers = set(range(1, p))
    # Generate all powers of g mod p
    generated = set()
    value = 1
    '''
    Each time we multiply by g, we effectively computing the next power
    Thus the modulo operations keeps the numbers manageable without
    dealing with explicit exponentiation!
    '''
    for _ in range(1, p):
        value = (value * g) % p
        generated.add(value)
    # Check if all numbers were generated
    return numbers == generated


def diffie_hellman(g, p, a, b):
    """
    Demonstrate Diffie-Hellman key exchange with small numbers
    g: generator (primitive root modulo p)
    p: prime number
    a: Alice's private key
    b: Bob's private key
    """
    print(f"Public parameters:")
    print(f"Prime (p) = {p}")
    print(f"Generator (g) = {g}")
    print(f"\nPrivate keys:")
    print(f"Alice's private key (a) = {a}")
    print(f"Bob's private key (b) = {b}")

    # Alice computes A = g^a mod p
    A = pow(g, a, p)
    print(f"\nAlice computes A = g^a mod p = {g}^{a} mod {p} = {A}")

    # Bob computes B = g^b mod p
    B = pow(g, b, p)
    print(f"Bob computes B = g^b mod p = {g}^{b} mod {p} = {B}")

    # Alice computes the shared secret
    alice_secret = pow(B, a, p)
    print(f"\nAlice computes shared secret = B^a mod p = {B}^{a} mod {p} = {alice_secret}")

    # Bob computes the shared secret
    bob_secret = pow(A, b, p)
    print(f"Bob computes shared secret = A^b mod p = {A}^{b} mod {p} = {bob_secret}")

    return alice_secret, alice_secret == bob_secret

def main():
    # Example with small numbers
    p = 23  # A small prime number
    g = 7  # A primitive root modulo 23
    a = random.randint(2, 1000)   #15 # Alice's private key
    b = random.randint(2, 300)   #12 # Bob's private key

    # Verify that g is indeed a primitive root modulo p
    if not is_primitive_root(g, p):
        print(f"Warning: {g} is not a primitive root modulo {p}")
    else:
        print(f"{g} is a primitive root modulo {p}\n")

    # Run the demonstration
    secret, success = diffie_hellman(g, p, a, b)
    print(f"\n Secret is {secret} - Key exchange {'successful ' if success else 'failed'}!")

if __name__ == "__main__":
    main()
