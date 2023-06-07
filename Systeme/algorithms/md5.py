from math import sin

def main():
    msg = b"ba"
    
    hash = md5(msg)
    
    print(f"msg:    {msg}")
    print(f"hash:   {hash}")

def md5(msg):
    # Konstanten
    shift_amounts = [7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22,5,9,14,20,5,9,14,20,5,9,14,20,5,9,14,20,4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23,6,10,15,21,6,10,15,21,6,10,15,21,6,10,15,21]

    consts = [ int(2**32 * abs(sin(i + 1))) for i in range(64) ]

    # initial states
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476


    # preprocess
    # convert to bits
    bit_str = b""
    for c in msg:
        bit_str += format(c, "08b").encode("utf-8")
    bit_str_len = format(len(bit_str), "064b").encode("utf-8")

    # padding
    bit_str += b"1"
    while len(bit_str) % 512 != 448: # 512 - 64 = 448
        bit_str += b"0"
    bit_str += bit_str_len


    # process hash
    for block in get_blocks(bit_str):
        words = block_to_words(block)

        a = a0
        b = b0
        c = c0
        d = d0

        for i in range(64):
            if i <= 15:
                f = (b & c) | (~b & d)
                g = i

            elif i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16

            elif i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16

            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + consts[i] + words[g]) % 2**32
            a = d
            d = c
            c = b
            b = sum_32(b, left_rotate(f, shift_amounts[i]))

        a0 = sum_32(a0, a)
        b0 = sum_32(b0, b)
        c0 = sum_32(c0, c)
        d0 = sum_32(d0, d)

    digest = format(a0, '08x') + format(b0, '08x') + format(c0, '08x') + format(d0, '08x')

    return digest

def get_blocks(bit_str):
    return [bit_str[i : i + 512] for i in range(0, len(bit_str), 512)]

def block_to_words(block):
    return [int(block[i : i + 32], 2) for i in range(0, len(block), 32)]

def left_rotate(i, shift):
    return ((i << shift) ^ (i >> (32 - shift))) % 2**32

def sum_32(a, b):
    return (a + b) % 2**32


if __name__ == "__main__":
    main()
