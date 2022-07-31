nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1+nota2+nota3)/3
m_ponderada = ((nota1*2)+(nota2*2)+(nota3*3))/7
m_ponderada1 = ((nota1*1)+(nota2*2)+(nota3*2))/5

print(f'{media:.2f}\n{m_ponderada:.2f}\n{m_ponderada1:.2f}')
