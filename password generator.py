import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    char_pools = []
    
    if use_lower:
        char_pools.append(string.ascii_lowercase)
    if use_upper:
        char_pools.append(string.ascii_uppercase)
    if use_digits:
        char_pools.append(string.digits)
    if use_symbols:
        char_pools.append(string.punctuation)

    if not char_pools:
        raise ValueError("At least one character type must be selected!")

    # Ensure password contains at least one from each selected type
    password = [random.choice(pool) for pool in char_pools]

    # Fill the rest from all selected pools combined
    all_chars = "".join(char_pools)
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to randomize order
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    length = int(input("Enter desired password length: "))

    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    print("Generated Password:", password)
