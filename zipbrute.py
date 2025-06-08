import pyzipper
import sys

def brute_force_zip(zip_path, wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.read().splitlines()

    for password in passwords:
        try:
            with pyzipper.AESZipFile(zip_path) as zf:
                zf.pwd = password.encode('utf-8')
                zf.extractall()
                print(f"[+] Password found: {password}")
                return
        except (RuntimeError, pyzipper.BadZipFile, pyzipper.LargeZipFile):
            continue
        except Exception as e:
            print(f"[-] Unexpected error: {e}")
            continue

    print("[-] Password not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <zipfile> <wordlist>")
        sys.exit(1)

    zip_file = sys.argv[1]
    wordlist_file = sys.argv[2]
    brute_force_zip(zip_file, wordlist_file)
