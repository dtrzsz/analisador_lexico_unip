'''
Analisador Léxico apresentado a matéria de Projeto II
'''
palavras_reservadas = ["SE", "SENAO_SE", "ENTAO", "SENAO", "FIM_SE", "FIMSE", "ESCREVA", "LEIA", "VAR", "INTEIRO", "REAL", "CARACTERE", "LOGICO", "ALGORITMO", "INICIO", "FIMALGORITMO", "E", "OU"]
Texto_digitado = str(input("Informe os caracteres da linha para análise: "))
i = 0
c = ""
token = ""
classe = ""
linha = list()

#Fase 01: identificador de palavra reservada e identificadores
#1.1: Varredura de caractere por caractere do Texto_digitado e armazenado em uma lista chamada linha
for caractere in Texto_digitado:
    linha.append(caractere)
#1.2: como no pseudocódigo a função len() não existe, se estipula um tamanho de 100 para o tam
tam = len(linha)
#1.3: em pseudocódigo era i <= tam porque o índice começa em 1. Mas em python o índice inicia em 0, o que significa que o último item de uma lista é tam-1
while i < tam:
    c = linha[i]
#1.3: c vai guardar o valor do índice conforme o i for avançando e a mesma variável vai identificar espaços em branco ou tab (\t)
    if (c == " ") or (c == "") or (c == "\t"):
        i += 1
#1.4: Aqui está o ponto central. Quando o computador compara caracteres, ele não usa a
#ordem do alfabeto. Ele compara o código numérico de cada caractere, definido pela
#tabela ASCII (ou Unicode, que mantém os mesmos valores para essas faixas).

    elif ((c >= "a") and (c <= "z")) or ((c >= "A") and (c <= "Z")) or (c == "_"):
        token = ""
        while (i < tam) and (((linha[i] >= "a") and (linha[i] <="z")) or ((linha[i] >= "A") and (linha[i] <= "Z")) or ((linha[i] >= "0") and (linha[i] <= "9")) or (linha[i] == "_")):
            token += linha[i]
            i += 1
        if token in palavras_reservadas:
            classe = "PALAVRA RESERVADA"
            print(f"{token} pertence a seguinte classe: {classe}")
        else:
            classe = "IDENTIFICADOR"
            print(f"{token} pertence a seguinte classe: {classe}")

#Fase 02: identificador de números inteiros (positivos e negativos) e decimais
#2.1: ele verifica se o caractere digitado corresponde a um range de 0 a 9 positivo, depois um range de 0 a 9 negativo
    elif ((c >= "0") and (c <= "9")) or \
        ((c == "-") and (i + 1 < tam) and (linha[i+1] >= "0") and (linha[i + 1] <= "9")):
        token = ""
        tem_ponto = False
#2.2.1: nos números inteiros positivos ele verifica se está entre 0 e 9
#2.2.2: nos números negativos ele analisa se o [i] tem "-" e se o token está vazio. Assim ele verifica se não é um simples - solto ou uma operação
#2.2.3: e caso for decimal, ele vai verificar através da variável tem_ponto, ela vai impedir que valores como 2.2.2 apareçam
        while (i < tam) and \
            (((linha[i] >= "0") and (linha[i] <= "9")) or ((linha[i] == "-") and (token == "")) or ((linha[i] == ".") and (not tem_ponto))):
            if linha[i] == ".":
                tem_ponto = True
            token += linha[i]
            i += 1
        classe = "NÚMERO"
        print(f"{token} pertence a seguinte classe: {classe}")

#Fase 03: identificador de Operadores e Delimitadores



    #ESSE ELSE É PROVISÓRIO RAPAZIADA. É PRA NÃO CAUSAR LOOP INFINITO
    else:
        print(c, "-> ainda não tratado")
        i = i + 1
    