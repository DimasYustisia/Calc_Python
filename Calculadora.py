print('='*50, '\n Seja Bem vindo(a) ao Projeto Calculadora 2000 ;D \n'+'='*50)
print('Obrigado por se nossa cobaia! \n')
v1 = float(input('Digite um valor: '))
v2 = float(input('Outro Valor: '))

def soma():
    print(v1+v2)
def sub():
    print(v1-v2)
def mult():
    print(v1*v2)
def div():
    print(v1/v2)

operacoes = {1:soma, 2:sub, 3:mult, 4:div}
print('Escolha uma das operações: \n 1 = Soma \n 2 = Subtração \n 3 = Multiplicação \n 4 = Divisão')
res = int(input('Escolha: '))

operacoes.get(res)()

