sbox = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
]

insbox = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d],
]

rcon = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1B, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00]
]


def keyschedule(chave):
    for a in range(0, 10):
        ax = 16 * a
        rotword = [*chave[ax + 7::4], chave[ax + 3]]
        rotword = subbytes(rotword)  # Coluna 4 root
        c0 = chave[ax + 0:-3:4]  # Coluna 0 root
        c1 = chave[ax + 1:-2:4]  # Coluna 1 root
        c2 = chave[ax + 2:-1:4]  # Coluna 2 root
        c3 = chave[ax + 3::4]  # Coluna 3 root
        c4 = []  # Coluna 4 / 0
        # 1 = c0  xor  rotword  xor  rcon
        for n in range(0, 4):
            temp = c0[n] ^ rotword[n] ^ rcon[0][n]
            chave.append(temp)  # Cria coluna 0
            c4.append(temp)
            chave.append(c1[n] ^ c4[n])  # Cria coluna 1
            chave.append(c2[n] ^ chave[-1])  # Cria coluna 2
            chave.append(c3[n] ^ chave[-1])  # Cria coluna 3
        rcon.pop(0)
    chave = chave[16:]
    return chave


def subbytes(texto):
    state = []
    s = []
    for b in range(0, len(texto)):
        if type(texto[b]) == int:
            s.append("{:02x}".format(texto[b]))
        else:
            # Condição para fazer a subbyte no KeySchedule
            s.append("{:02x}".format(ord(str(texto[b]))))  # tradução de cada elemento para seu valor em hex/utf-8
        # usar o valor hex como chave pra a tradução
        state.append(sbox[int(s[b][0], 16)][int(s[b][1], 16)])
    return state


def decsubbyte(texto):
    state = []
    s = []
    for c in range(0, len(texto)):
        if type(texto[c]) == int:
            s.append("{:02x}".format(texto[c]))
        else:
            # Condição para fazer a subbyte no KeySchedule
            s.append("{:02x}".format(ord(str(texto[c]))))  # tradução de cada elemento para seu valor em hex/utf-8
        # usar o valor hex como chave pra a tradução
        state.append(insbox[int(s[c][0], 16)][int(s[c][1], 16)])
    return state


def shiftrows(state):
    newstate = [
        *state[0: 4],
        state[5], state[6], state[7], state[4],
        state[10], state[11], state[8], state[9],
        state[15], state[12], state[13], state[14],
    ]
    return newstate


def decshiftrow(state):
    newstate = [
        *state[0: 4],
        state[7], state[4], state[5], state[6],
        state[10], state[11], state[8], state[9],
        state[13], state[14], state[15], state[12],
    ]
    return newstate


def mixcolumns(state):
    reducer = 283
    a0 = state[0:4]
    a1 = state[4:8]
    a2 = state[8:12]
    a3 = state[12:]
    b0, b1, b2, b3 = [], [], [], []
    for d in range(0, 4):
        b0.append(a0[d] << 1)
        b1.append(a1[d] << 1)
        b2.append(a2[d] << 1)
        b3.append(a3[d] << 1)
        '''
        Para cripto:    2 3 1 1    Para decripto:  14 11 13  9
                        1 2 3 1                    9  14 11 13
                        1 1 2 3                    13  9 14 11
                        3 1 1 2                    11 13  9 14
        '''
        state[d] = b0[d] ^ a3[d] ^ a2[d] ^ b1[d] ^ a1[d]
        state[d + 4] = b1[d] ^ a0[d] ^ a3[d] ^ b2[d] ^ a2[d]
        state[d + 8] = b2[d] ^ a1[d] ^ a0[d] ^ b3[d] ^ a3[d]
        state[d + 12] = b3[d] ^ a2[d] ^ a1[d] ^ b0[d] ^ a0[d]
    for e in range(0, len(state)):
        if state[e] > 0xff:
            state[e] = state[e] ^ reducer
    return state


def decmixcolumns(state):
    """
    Para decripto:  14 11 13  9
                    9  14 11 13
                    13  9 14 11
                    11 13  9 14
    """
    teste = [
        0x39, 0x20, 0xdc, 0x19,
        0x25, 0xdc, 0x11, 0x6a,
        0x84, 0x90, 0x85, 0xb0,
        0x1d, 0xfb, 0x97, 0x32,
    ]
    reducer = 283
    a0 = state[0:4]
    a1 = state[4:8]
    a2 = state[8:12]
    a3 = state[12:]
    for f in range(0, 4):
        state[f] = (a0[f] * 14) ^ (a1[f] * 11) ^ (a2[f] * 13) ^ (a3[f] * 9)
        state[f + 4] = (a0[f] * 9) ^ (a1[f] * 14) ^ (a2[f] * 11) ^ (a3[f] * 13)
        state[f + 8] = (a0[f] * 13) ^ (a1[f] * 9) ^ (a2[f] * 14) ^ (a3[f] * 11)
        state[f + 12] = (a0[f] * 11) ^ (a1[f] * 13) ^ (a2[f] * 9) ^ (a3[f] * 14)
    print(state)
    for g in range(0, len(state)):
        print(state[g], ' | ', teste[g])
        print(bin(state[g]), ' | ', bin(teste[g]))
        print(state[g] ^ teste[g])
        temp = state[g] ^ reducer
        print(temp, bin(temp))
        print(temp ^ teste[g])
        if temp == teste[g]:
            print(temp, True)
        temp = (state[g] ^ reducer) >> 3
        print(temp, bin(temp))
        print(temp ^ teste[g])
        if temp == teste[g]:
            print(temp, True)
        print(10*'*')
    return state


def addroundkey(state, rk):
    # deve ser enviado como hex()
    for j in range(0, 16):
        print(state[j], rk[j])
        state[j] = state[j] ^ rk[j]
    return state


def tohexlist(texto):
    pt = []
    for h in range(0, len(texto)):
        pt.append(ord(str(texto[h])))
    return pt


def tostr(state):
    temp = ''
    for e in state:
        temp += ''.join(chr(e))
    return temp


def encript(texto, chave):
    chave = tohexlist(chave)
    print(chave)
    rk = keyschedule(chave)
    plaintext = tohexlist(texto)
    print(plaintext)
    # --- Round 0 ---
    state = addroundkey(plaintext, chave)

    print('*************')
    print('addroundkey 0 --')
    for o in state:
        print(hex(o))
    print('*************')
    for n in range(0, 9):
        # --- Round 1 a 9 ---
        state = subbytes(state)  # ok
        print('*************')
        print('subbytes', n)
        for o in state:
            print(hex(o))
        print('*************')
        state = shiftrows(state)  # ok
        print('*************')
        print('shiftrows', n)
        for o in state:
            print(hex(o))
        print('*************')
        state = mixcolumns(state)
        print('*************')
        print('mixcolumns', n)
        for o in state:
            print(hex(o))
        print('*************')
        state = addroundkey(state, rk[16 * n:16 * n + 16])
        print('*************')
        print('addroundkey', n)
        for o in state:
            print(hex(o))
        print('*************')
    # --- Round 10 ---
    state = subbytes(state)  # ok
    print('*************')
    print('subbytes  10')
    for o in state:
        print(hex(o))
    print('*************')
    state = shiftrows(state)
    print('*************')
    for o in state:
        print(hex(o))
    print('*************')
    state = addroundkey(state, rk[-16:])
    print('*************')
    for o in state:
        print(hex(o))
    print('*************')

    # for i in range(0, 16, 4):
    #    print(hex(state[i]), hex(state[i + 1]), hex(state[i + 2]), hex(state[i + 3]))
    state = tostr(state)
    return state


def decript(texto, chave):
    """
    :param texto: ciphertext com 128bits
    :param chave: com 128bits
    :return: plaintext
    Deve seguir o mesmo principio de receber e retornar arrays de hex()
    AddRoundkey(), Keyschedule() são as mesmas
    Subbyte é a mesma mas precisa usar outra sbox
    round -10: addroundkey, shiftrow, subbyte
    round -9 a -1: addroundkey, mixcolumns, shiftrows, subbytes.
    round 0: addroundkey
    """
    chave = tohexlist(chave)
    rk = keyschedule(chave)
    ciphertext = tohexlist(texto)
    # --- Round -10  ---
    state = addroundkey(ciphertext, chave)
    state = decshiftrow(state)
    state = decsubbyte(state)
    # --- Round -9 a -1 ---
    state = addroundkey(state, rk[0:16])
    state = decmixcolumns(state)
    return state


'''
Tudo Ok com  a criptografia
ttext = '21àCZ17ö0¨¢4'
tchave = "+(«	~®÷ÏÒO¦<"
result = encript(ttext, tchave)

0x39 0x2 0xdc 0x19
0x25 0xdc 0x11 0x6a
0x84 0x9 0x85 0xb
0x1d 0xfb 0x97 0x32

print('\n', 18 * '=')
print('Olá, pessoa. Tudo bom? '
      '\nQue tal criptografar aquela mensagem que você que mandar?'
      '\nSeu texto/mensagem devem ter 16 caracteres cada '
      '\nE os caracteres podem ser: '
      '\nLetras, numeros, espaços ou caracteres especias("/,#,@,?")')

t = str(input('Vamos começar! '
              '\nDigite sua mensagem com 16 digitos'
              '\n=>> '))
c = str(input('Agora digite sua chave secreta, que será a base para criptografar e descriptografar sua mensagem '
              '\nGuarde bem sua chave, você precisará dela depois'
              '\nLembrando que a chave também deve ter 16 caracteres '
              '\n=>> '))
print('Ok...'
      '\nEntão essa é sua mensagem criptografada\n')
'''

x = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
x2 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xf, 0x4f, 0x3c]
tx = ''
ch = ''

for i in x:
    tx += ''.join(chr(i))
for i in x2:
    ch += ''.join(chr(i))
print(tx)
print(ch)

r = encript(tx, ch)
for i in r:
    print(hex(ord(i)))
