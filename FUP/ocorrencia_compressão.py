# função que remove pontuação de texto e terna o texto "limpo"
def removerPontuacao(texto, pontuacoes):
    for p in pontuacoes:
        texto = texto.replace(p, '')
    return texto

P = ['.', ',', ':', ';', '!', '?']  
entrada = input()
entrada = removerPontuacao(entrada, P)
L = entrada.split()

palavras = [ elem for elem in L if len(elem) > 3] #Lista contendo as palavras com tamanho maiores ou iguais a 3
ocorrencia = [L.count(elem) for elem in palavras] #Lista contendo as ocorrências das palavras da lista palavras

for i in range(len(ocorrencia)):
    print(palavras[i], ocorrencia[i])