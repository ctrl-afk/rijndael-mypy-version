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
    for c in range(0, 10):
        x = 16 * c
        rotword = [*chave[x + 7::4], chave[x + 3]]
        rotword = subbytes(rotword)  # Coluna 4 root
        c0 = chave[x + 0:-3:4]  # Coluna 0 root
        c1 = chave[x + 1:-2:4]  # Coluna 1 root
        c2 = chave[x + 2:-1:4]  # Coluna 2 root
        c3 = chave[x + 3::4]  # Coluna 3 root
        c4 = []             # Coluna 4 / 0
        # 1 = c0  xor  rotword  xor  rcon
        for i in range(0, 4):
            temp = c0[i] ^ rotword[i] ^ rcon[0][i]
            chave.append(temp)  # Cria coluna 0
            c4.append(temp)
            chave.append(c1[i] ^ c4[i])  # Cria coluna 1
            chave.append(c2[i] ^ chave[-1])  # Cria coluna 2
            chave.append(c3[i] ^ chave[-1])  # Cria coluna 3
        rcon.pop(0)
    chave = chave[16:]
    return chave


def subbytes(texto):
    state = []
    s = []
    for i in range(0, len(texto)):
        if type(texto[i]) == int:
            s.append("{:02x}".format(texto[i]))
        else:
            # Condição para fazer a subbyte no KeySchedule
            s.append("{:02x}".format(ord(str(texto[i]))))  # tradução de cada elemento para seu valor em hex/utf-8
        # usar o valor hex como chave pra a tradução
        state.append(sbox[int(s[i][0], 16)][int(s[i][1], 16)])
    return state


def shiftrows(state):
    newstate = [
        *state[0: 4],
        state[5],   state[6],   state[7],   state[4],
        state[10],  state[11],  state[8],   state[9],
        state[15],  state[12],  state[13],  state[14],
    ]
    return newstate


def mixcolumns(state):
    reducer = 283
    a0 = state[0:4]
    a1 = state[4:8]
    a2 = state[8:12]
    a3 = state[12:]
    b0, b1, b2, b3 = [], [], [], []
    for i in range(0, 4):
        b0.append(a0[i] << 1)
        b1.append(a1[i] << 1)
        b2.append(a2[i] << 1)
        b3.append(a3[i] << 1)
        '''
        Para cripto:    2 3 1 1    Para decripto:  14 11 13  9
                        1 2 3 1                    9  14 11 13
                        1 1 2 3                    13  9 14 11
                        3 1 1 2                    11 13  9 14
        '''
        state[i] = b0[i] ^ a3[i] ^ a2[i] ^ b1[i] ^ a1[i]
        state[i + 4] = b1[i] ^ a0[i] ^ a3[i] ^ b2[i] ^ a2[i]
        state[i + 8] = b2[i] ^ a1[i] ^ a0[i] ^ b3[i] ^ a3[i]
        state[i + 12] = b3[i] ^ a2[i] ^ a1[i] ^ b0[i] ^ a0[i]
    for i in range(0, len(state)):
        if state[i] > 0xff:
            state[i] = state[i] ^ reducer
    return state


def addroundkey(state, rk):
    # deve ser enviado como hex()
    for i in range(0, 16):
        state[i] = state[i] ^ rk[i]
    return state


def tohexlist(texto):
    pt = []
    for i in range(0, len(texto)):
        pt.append(ord(str(texto[i])))
    return pt


def tostr(state):
    temp = ''
    for e in state:
        temp += ''.join(chr(e))
    return temp


def encript(texto, chave):
    chave = tohexlist(chave)
    rk = keyschedule(chave)
    plaintext = tohexlist(texto)
    # --- Round 0 ---
    state = addroundkey(plaintext, chave)
    for i in range(0, 9):
        # --- Round 1 a 9 ---
        state = subbytes(state)     # ok
        state = shiftrows(state)    # ok
        state = mixcolumns(state)
        state = addroundkey(state, rk[16*i:16*i+16])
    # --- Round 10 ---
    state = subbytes(state)  # ok
    state = shiftrows(state)
    state = addroundkey(state, rk[-16:])

    # for i in range(0, 16, 4):
    #    print(hex(state[i]), hex(state[i + 1]), hex(state[i + 2]), hex(state[i + 3]))
    state = tostr(state)
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
'''

print('\n', 18*'=')
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

resultado = encript(t, c)
print('\n', 18*'=')
print(resultado)
print('\n', 18*'=')
