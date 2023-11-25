import zipfile
import itertools

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print("Password found:", password)
        return True
    except Exception as e:
        return False

def brute_force(zip_file_path, charset, max_length):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        for length in range(1, max_length + 1):
            for password in itertools.product(charset, repeat=length):
                password = ''.join(password)
                if extract_zip(zip_file, password):
                    return

# Usage example
zip_file_path = 'test.zip'
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
max_length = 8
brute_force(zip_file_path, charset, max_length)
