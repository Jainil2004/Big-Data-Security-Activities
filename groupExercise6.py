SECRETKEY = 79493
MODULUS = 100000

def encryptNumber(num):
    return (num + SECRETKEY) % MODULUS

def decryptNumber(encryptedNumber):
    return (encryptedNumber - SECRETKEY) % MODULUS

def decryptSum(encryptedSum):
    return (encryptedSum - 2 * SECRETKEY) % MODULUS

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

num1Encrupted = encryptNumber(num1)
num2Encrypted = encryptNumber(num2)

encryptedSum = (num1Encrupted + num2Encrypted) % MODULUS

sum_result = decryptSum(encryptedSum)

print(f"num1 = {num1}, num2 = {num2}")
print(f"num1 after encryption: {num1Encrupted}, num2 after encryption: {num2Encrypted}")
print(f"encrypted sum: {encryptedSum}")
print(f"decrypted sum: {sum_result}")
