# python-rijndael
 Versão do algoritmo Rijndael em python

Para começar foi preciso definir alguns padrões entre as funções do programa:
1) Todos os estados da chave e do texto(state) são em formato de lista em que cada elemento representa uma letra. O formato de listas é mais simples e facilita os processos de laços "for".

2) Todas as funções devem receber e retornar valores de tipos semelhantes. Isso evitar erros de tipagem, principalmente durante os laços, além de evitar confusões entre valores inteiros decimais e hexadecimais.

3) O tipo padrão dos elementos das listas usado é o hexadecimal(em formato 0xff). As letras do texto são traduzidas para hexadecimal logo no começo do algoritmo para que todas as outras funções funcionem.

# encript.py

A função principal encript precisa receber dois parâmetros, o texto a ser cifrado e a chave. Logo no começo, para obedecer os pré-requisitos, ambos os parâmetros devem formatados em lista com a função tohexlist.
Após isso o próximo passo é a expansão da chave utilizando a função keyschedule, que calculará 10 variações de chave para serem usadas no decorrer do processo.
As 9 rodadas seguintes a mensagem é aplicada a 4 operações, a subbytes, shiftrows, mixcolumns, addroundkey. 
A última rodada é similar as anteriores, com exceção da função mixcolumns, para terminar utiliza-se a função tostr para formatar a mensagem que se encontra como uma lista de valores hexadecimais, para uma linha de texto codificada em UTF-8.

## keyschedule

A operação começa colocando o valor da chave inserida numa nova lista e a recoloca em sua lista original, dessa maneria o valor poderá ser acessado no endereço 0 da nova lista chave e todas as chaves estendidas criadas serão salvas no endereço 1 em dante.
Para o calculo das chaves é definido a variável rotword, que se trata dos mesmos elementos da coluna final da chave, porém e feita uma mudança, o primeiro elemento da coluna e movido para a última posição. Então para facilitar os passos a seguir, são definidas as variáveis c0, c1, c2, c3, cada uma recebe os valores de uma coluna da chave[0]. Depois e adicionada a chave uma lista com todos os valores iguais a 0, para que possam ser alterados futuramente, essa adição e necessária, pois a operação a seguir usara linhas para encontra o valor de colunas, de maneria que não será linear.
O primeiro item da linha e definida ela operação xor entre c0, rotword e rcon(uma lista predefinida). O segundo e calculado ela operação xor entre o c1 e o primeiro elemento(calculado anteriormente) da nova chave. O terceiro e o quarto obedecem a mesma conta do segundo, são definidos pelo xor entre c2 ou c3 e o elemento anterior da mesma linha.

## subbytes

Traduz os elementos da lista inserida para seu valor correspondente, de acordo com a tabela predefinida sbox.

## shftrows

Como o nome indica, nessa função ha um deslocamento dos itens em linha, para isso cria-se uma variável chamada newstate que receberas os elementos do state já organizados da maneira devida e a retorna.

## mixcolumns

Esta função e mais complexa, começa-se criando 4 variáveis para as linhas e outras 4 listas b vazias.
Depois inicia-se um laço para calcular as variáveis b, com os valores de 2 * a com a operação: 
a0[d] << 1
Ainda no laço são feitas as operações para calcular os novos elementos, coluna por coluna:
x0 = 2 * a0 ^ a3 ^ a2 ^ 3 * a1
x1 = 2 * a1 ^ a0 ^ a3 ^ 3 * a2
x2 = 2 * a2 ^ a1 ^ a0 ^ 3 * a3
x3 = 2 * a3 ^ a2 ^ a1 ^ 3 * a0
Em que "^" e o símbolo usado em python para a operação xor.
Para concluir ha uma condicional para filtrar os valores a cima de 0xff(255) e faz uma operação xor entre o número e a constante redutora igual a 283(valor predefinido) para torná-lo menor.

## addroundkey

Aplica-se um laço para fazer uma operação xor entre cada letra do texto e cada letra da chave.

## tohexlist

Faz com que cada elemento passe pela operação ord a qual traduzira as letras para seu valor hexadecimal de acordo com a convenção UTF-8.

## tostr

E praticamente o oposto de tohexlist essa função passa todos os elementos da lista em uma operação chr que traduz os valores hexadecimal para texto, também na convenção UTF-8, e os concatena numa única linha de texto.

## savemesg

Usa a data para criar o nome do novo arquivo com a mensagem da seguinte maneira:
nome = "mensg" + data + ".txt"
Depois e criado o arquivo escrevesse o texto no mesmo.

# Decript.py

O algoritmo para descriptografar exatamente o mesmo processo de encriptar ao contrário, sando a mesma função tohexlist para adaptar, o texto e a chave inserida, no formato adrão de lista, seguida se cria novamente a chave estendida com a mesma função do keyschedule.
Dessa maneira ja e possível fazer todos os outros processos, começando com a função addroundkey, depois usa-se a função decshiftrow, decmixcolumns e decsubbyte que revertera os respectivos processos.

# decsubbyte

E exatamente a mesma função subbytes, mas usa outra tabela predefinida como tradutor chamada insbox.

# decshiftrow
É exatamente o mesmo funcionamento de shiftrow, mas os itens são organizados de outra maneira com a intenção de desfazer o que a anterior fez.

# decmixcolumns
E função pega o state e o aplica a mixcolumns original 3 vezes, revertendo o processo criptográfico.

# selectarq
E uma função auxiliar com o objetivo de servir de menu para selecionar a mensagem a ser descriptografada. 