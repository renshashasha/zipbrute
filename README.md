````markdown
# AES-256 ZIP Brute Force Tool

A simple Python script to brute-force ZIP files encrypted with AES-256 (e.g., created by 7-Zip or WinZip).

## Requirements

- Python 3.x
- `pyzipper` library

Install `pyzipper` with:
````


## Usage

```bash
python zip_brute.py <zipfile> <wordlist>
```

* `<zipfile>`: Path to the encrypted ZIP file.
* `<wordlist>`: Path to the password wordlist file (one password per line).

## Example

```bash
python zip_brute.py secret.zip rockyou.txt
```

## Notes

* Only supports ZIP files encrypted with AES (not legacy ZipCrypto).
* Brute-force may take a long time depending on wordlist size.
* For faster attacks or other encryption types, consider specialized tools.
