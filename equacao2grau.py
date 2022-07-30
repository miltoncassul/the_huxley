# EQUACAO DO 2 GRAU

a = float(input())
b = float(input())
c = float(input())

delta = (b*b)-(4*a*c)
z = pow(delta, 0.5) # Delta 0.5 eh para aceitar numeros negativos como no exemplo 
                    # Entrada:  1
                    #          -0.02
                    #           0.001
if(delta < 0):
    print("NRR\n")
elif(a == 0):
    print("NEESG\n")
elif(a > 0):
    x = (-b+z)/(2*a)
    y = (-b-z)/(2*a)
    print(f'{x:.2f}')
    print(f'{y:.2f}')
