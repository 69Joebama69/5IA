import struct 

def main():
    msg = b"aa"

    hash = sha1(msg)

    print(f"msg:    {msg}")
    print(f"hash:   {hash}")

def sha1(msg):

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    padding = b"\x80" + b"\x00" * (63 - (len(msg) + 8) % 64)
    msg += padding + struct.pack(">Q", 8 * len(msg))

    
    for block in get_blocks(msg):
        expanded_block = expand_block(block)
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999

            elif i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            
            elif i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rotate(a, 5) + f + e + k + expanded_block[i] & 0xFFFFFFFF
            e = d
            d = c
            c = rotate(b, 30)
            b = a
            a = temp

        h0 += a & 0xFFFFFFFF
        h1 += b & 0xFFFFFFFF
        h2 += c & 0xFFFFFFFF
        h3 += d & 0xFFFFFFFF
        h4 += e & 0xFFFFFFFF

    return("{:08x}" * 5).format(h0, h1, h2, h3, h4)

    # digest = str(h0 << 128 | h1 << 96 | h2 << 64 | h3 << 32 | h4)

def get_blocks(bit_str):
    return [bit_str[i : i + 64] for i in range(0, len(bit_str), 64)]

def expand_block(block):
    w = list(struct.unpack(">16L", block)) + [0] * 64
    for i in range(16, 80):
        w[i] = rotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
    return w

def rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


if __name__ == "__main__":
    main()
