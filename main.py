import itertools
import string

# Target password to guess
target_password = "Pa55"

# Character set to test (letters and digits)
charset = string.ascii_letters + string.digits

for length in range(1, 5):  # Try passwords of length 1 to 4
    for attempt in itertools.product(charset, repeat=length):
        guess = ''.join(attempt)
        print(f"Trying: {guess}")
        if
