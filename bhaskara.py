a = float(input('Digite o valor de a'))
b = float(input('Digite o valor de b'))
c = float(input('Digite o valor de c'))
delta = b**2-4*a*c
print('a=',a,'b=',b,'c=',c)
print('Delta =',delta)

import math

if delta < 0 :
    print('Não tem raízes reais')

else:
    delta >= 0
    math.sqrt(delta)
    x = (-b +- (math.sqrt(delta)) / 2*a)        

if delta == 0 :
    print('A raiz é:',x)

else:
    delta > 0
    math.sqrt(delta)
    x = (-b +- (math.sqrt(delta)) / 2*a)
    print('As raízes são: x1=',x,'e x2=',-x)