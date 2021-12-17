peso = float(input('Digite seu peso em quilos. "Exemplo: 85.4": '))
altura = float(input('Digite sua altura. "Exemplo: 1.72": '))
IMC = peso / altura**2
print(IMC)
if IMC < 18.5 :
    print('Seu IMC é: ',IMC,'- Abaixo do Peso.')
elif IMC < 25 :
    print('Seu IMC é: ',IMC,'- Peso Normal')
elif IMC < 30 :
    print('Seu IMC é: ',IMC,'- Sobrepeso')
elif IMC < 35 :
    print('Seu IMC é: ',IMC,'- Obesidade Grau I')
elif IMC < 40 :
    print('Seu IMC é: ',IMC,'- Obesidade Grau II')
else :
    print('Seu IMC é: ',IMC,'- Obesidade Mórbida')