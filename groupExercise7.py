SECRET_KEY = 4321
MODULUS = 10000019 

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return 0
    else:
        return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

KEY_INV = modinv(SECRET_KEY, MODULUS)

def encrypt(x):
    return (x * SECRET_KEY) % MODULUS

def decrypt(x_enc):
    return (x_enc * KEY_INV) % MODULUS

salary = 5000
enc_salary = encrypt(salary)
enc_tax = enc_salary 
tax = decrypt(enc_tax) / 10 

print(f"Original salary: {salary}")
print(f"Encrypted salary: {enc_salary}")
print(f"Decrypted tax amount: {tax}")
