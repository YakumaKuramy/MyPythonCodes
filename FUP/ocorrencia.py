def removerPontuacao(texto, pontuacoes):
    for p in pontuacoes:
        texto = texto.replace(p, '')
    return texto

P = ['.', ',', ':', ';', '!', '?']  
entrada = input()
entrada = removerPontuacao(entrada, P)
L = entrada.split()

palavras = [] #Lista contendo as palavras com tamanho maiores ou iguais a 3
ocorrencia = [] #Lista contendo as ocorrências das palavras da lista palavras

for palavra in L:
    if len(palavra) > 3:
        palavras.append(palavra)
        ocorrencia.append(L.count(palavra))
    
for i in range(len(ocorrencia)):
    print(palavras[i], ocorrencia[i])