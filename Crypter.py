def change_files(filename, crypto_fn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = crypto_fn(raw_value)

            # compare cipher and flat block size
            if len(raw_value) != len(cipher_value):
                raise ValueError('The cipher value {} has a different size than the flat value {}'
                                 .format(len(cipher_value), len(raw_value)))

            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)
