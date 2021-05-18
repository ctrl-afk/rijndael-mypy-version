from rijindael.encript import encript, formattoencript, savemesg
from rijindael.decript import decript, selectarq

print('Olá! Você deseja encriptar ou decriptar sua mensagem:')
while True:
    menu = int(input('0 - Sair'
                     '\n1 - Encriptar'
                     '\n2 - Decriptar'
                     '\n=>> '))
    if menu == 1:
        print('\n', 10 * '=', 'Encriptar', 10 * '=')
        print('Olá, pessoa. Tudo bom? '
              '\nQue tal criptografar aquela mensagem que você quer mandar?')

        txt = str(input('Vamos começar! \nDigite sua mensagem aqui: \n=>> '))
        txt = formattoencript(16, txt)
        chv = str(
            input('Agora digite sua chave secreta, que será a base para criptografar e descriptografar sua mensagem. '
                  '\nGuarde bem sua chave, você precisará dela depois.'
                  '\nLembrando que sua chave DEVE ter 16 caracteres. '
                  '\n=>> '))
        while len(chv) != 16:
            chv = str(input('Tamanho de chave incorreto! Tente Novamente... \n=>>'))
        print('Ok...'
              '\nEntão essa é sua mensagem criptografada...\n')
        res = ''
        for slc in txt:
            res += encript(slc, chv)
        print(res)
        savemesg(res)
        print(29*'=')
        break
    elif menu == 2:
        print('\n', 10 * '=', 'Encriptar', 10 * '=')
        res = selectarq()
        chv = str(input('E agora insira a sua chave: \n=>>'))
        while len(chv) != 16:
            chv = str(input('Tamanho de chave incorreto! Tente Novamente... \n=>>'))
        print('Sua mesagem decriptografada é: ')
        txt = formattoencript(32, res)
        res = ''
        for slc in txt:
            res += decript(slc, chv)
        print(res.strip())
        print(29 * '=')
        break
    elif menu == 0:
        break
    else:
        print('*** Opção Invalida ***')

print("Fim.")
