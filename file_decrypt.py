import sys
from lib.Argument import Argument
from RSA.rsa import rsa_decrypt
from AES.aes import aes_decrypt

parser = Argument()
args = sys.argv

parser.parse_args(args)

if '--file' not in parser.option or '--algorithm' not in parser.option or '--key' not in parser.option:
    print("Usage: python3 file_decrypt.py --file <file> --algorithm <algorithm> --key <key>"
          "\n\t--file: file to decrypt"
          "\n\t--algorithm: algorithm to use for decryption (AES, RSA)"
          "\n\t--key: key to use for decryption"
          "\n\t--help: print this help message")
    exit(1)

file_path = parser.optionValues.get('--file')
algorithm = parser.optionValues.get('--algorithm')
key = parser.optionValues.get('--key')

if '--help' in parser.option:
    print("Usage: python3 file_decrypt.py --file <file> --algorithm <algorithm> --key <key>"
          "\n\t--file: file to decrypt"
          "\n\t--algorithm: algorithm to use for decryption (AES, RSA)"
          "\n\t--key: key to use for decryption"
          "\n\t--help: print this help message")
    exit(0)

if algorithm == 'AES':
    aes_decrypt(file_path, key)

elif algorithm == 'RSA':
    rsa_decrypt(file_path, key)

else:
    print('Algorithm not supported')

    