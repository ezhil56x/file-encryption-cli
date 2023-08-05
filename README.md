# File Encryption CLI

## Description

File Encryption is command-line tool used to encrypt and decrypt files using AES and RSA encryption algorithms. It is written in Python and uses the `PyCryptoDome` library.

## Requirements

- Python 3.6 or above
- `PyCryptoDome` library

## Installation

1. Install pycryptodome library

```
pip install pycryptodome
```

2. Clone the repository

```
git clone https://github.com/ezhil56x/file-encryption-cli.git
```

3. Go to file-encryption-cli directory

```
cd file-encryption-cli
```

4. Take a look at the help menu to see the usage of the tool

```
python file_encrypt.py --help
```

```
python file_decrypt.py --help
```

## Usage

### AES Encryption

#### Encrypting a File

To encrypt a file, using AES encryption, use the following command

```
python file_encrypt.py --file <file> --algorithm AES --key <text>
```

#### Decrypting a File

To decrypt a file, using AES encryption, use the following command

```
python file_decrypt.py --file <file> --algorithm AES --key <text>
```

### RSA Encryption

For RSA encryption, you need to generate public and private keys. You can use the `key_generator.py` script to generate the keys. And the keys will be stored in `public.pem` and `private.pem` files. You should move these files to the same directory as the `file_encrypt.py` and `file_decrypt.py` scripts.

#### Encrypting a File

To encrypt a file, using RSA encryption, use the following command

```
python file_encrypt.py --file <file> --algorithm RSA --key public.pem
```

#### Decrypting a File

To decrypt a file, using RSA encryption, use the following command

```
python file_decrypt.py --file <file> --algorithm RSA --key private.pem
```

#### Generating public and private keys

To generate public and private keys, go to RSA folder and run the following command

```
python key_generator.py
```
