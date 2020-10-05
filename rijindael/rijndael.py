from encript import encript
from decript import decript

print('Olá! Você deseja encriptar ou decriptar sua mensagem:')
while True:
    menu = int(input('0 - Sair'
                     '\n1 - Encriptar'
                     '\n2 - Decriptar'
                     '\n=>> '))
    if menu == 1:
        print('\n', 10 * '=', 'Encriptar', 10 * '=')
        print('Olá, pessoa. Tudo bom? '
              '\nQue tal criptografar aquela mensagem que você quer mandar?'
              '\nSeu texto/mensagem devem ter 16 caracteres'
              '\nOBS: Os caracteres podem ser: '
              '\nLetras, numeros, espaços ou caracteres especias("/,#,@,?")')

        txt = str(input('Vamos começar! '
                        '\nDigite sua mensagem com 16 digitos'
                        '\n=>> '))
        while len(txt) != 16:
            txt = str(input('Tamanho de texto incorreto! Tente Novamente... \n=>>'))
        chv = str(
            input('Agora digite sua chave secreta, que será a base para criptografar e descriptografar sua mensagem '
                  '\nGuarde bem sua chave, você precisará dela depois'
                  '\nLembrando que a chave também deve ter 16 caracteres '
                  '\n=>> '))
        while len(chv) != 16:
            chv = str(input('Tamanho de chave incorreto! Tente Novamente... \n=>>'))
        print('Ok...'
              '\nEntão essa é sua mensagem criptografada\n')
        res = encript(txt, chv)
        print(res)
        print(29*'=')
        break
    elif menu == 2:
        print('\n', 10 * '=', 'Encriptar', 10 * '=')

        res = str(input('Então basta inserir a mensagem Encriptada com 16 caracteres'
                        '\n=>>'))
        while len(res) != 16:
            res = str(input('Tamanho de texto incorreto! Tente Novamente... \n=>>'))
        chv = str(input('E agora insira a sua chave'
                        '\n=>>'))
        while len(chv) != 16:
            chv = str(input('Tamanho de chave incorreto! Tente Novamente... \n=>>'))
        print('Sua mesagem decriptografada é:')
        txt = decript(res, chv)
        print(txt)

        print(29 * '=')
        break
    elif menu == 0:
        break
    else:
        print('*** Opção Invalida ***')

print("Fim.")
