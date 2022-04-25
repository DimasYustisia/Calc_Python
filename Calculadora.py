from cmath import tan


print('='*50, '\n Seja Bem vindo(a) ao Projeto Calculadora 2000 ;D \n'+'='*50)
print('Obrigado por se nossa cobaia! \n')

#Menu

print('Escolha uma das operações: \n 1 = Soma \n 2 = Subtração \n 3 = Multiplicação \n 4 = Divisão \n 5 = Seno \n 6 = Cosseno \n 7 = Tangente')
res = int(input('Escolha: '))

def soma():
    print('='*50,'\n Soma: \n')
    v1_soma = float(input('Digite um número: '))
    v2_soma = float(input('Digite outro número: '))
    print(v1_soma+v2_soma, '\n' ,'='*50)

def sub():
    
    v1_sub = float(input('Digite um valor: '))
    v2_sub = float(input('Outro Valor: '))
    print(v1_sub-v2_sub)


def mult():  
    v1_mult = float(input('Digite um valor: '))
    v2_mult = float(input('Outro Valor: '))
    print(v1_mult*v2_mult)


def div():
    v1_div = float(input('Digite um valor: '))
    v2_div = float(input('Outro Valor: '))
    print(v1_div/v2_div)


def sen():
    v1_div = float(input('Digite um valor: '))
    #v2_div = float(input('Outro Valor: '))
    #print(v1_div/v2_div)

def cos():
    v1_div = float(input('Digite um valor: '))
    #v2_div = float(input('Outro Valor: '))
    #print(v1_div/v2_div)

def tan():
    v1_div = float(input('Digite um valor: '))
    #v2_div = float(input('Outro Valor: '))
    #print(v1_div/v2_div)



operacoes = {1:soma, 2:sub, 3:mult, 4:div, 5:sen, 6:cos, 7:tan}


operacoes.get(res)()

