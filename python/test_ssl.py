import OpenSSL.crypto


def load_public_key(pfx_path, pfx_password):
    ''' Read the public key and return as PEM encoded '''

    # print('Opening:', pfx_path)
    with open(pfx_path, 'rb') as f:
        pfx_data = f.read()

    # print('Loading PFX contents:')
    pfx = OpenSSL.crypto.load_pkcs12(pfx_data, pfx_password)

    public_key = OpenSSL.crypto.dump_publickey(
        OpenSSL.crypto.FILETYPE_PEM,
        pfx.get_certificate().get_pubkey())   # Change to pfx.

    print(public_key)

    return public_key


load_public_key('D://test.pfx', '1234')
