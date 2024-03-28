import random
import string

def generate_code(length=10):
    """Generate a random code of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_codes(num_codes=50, code_length=8):
    """Generate a specified number of random codes."""
    return [generate_code(code_length) for _ in range(num_codes)]

if __name__ == "__main__":
    num_codes = int(input("Enter the number of codes to generate: "))
    code_length = int(input("Enter the length of each code: "))
    
    codes = generate_codes(num_codes, code_length)
    for code in codes:
        print(code)
