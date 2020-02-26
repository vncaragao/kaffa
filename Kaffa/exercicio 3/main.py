from retangulo import retangulo
#inicia os objetos retangulo conforme o exercicio
a = retangulo(3,5,11,11);
b = retangulo(7,2,13,7);
c = retangulo(10,10,14,13);
#metodo para verificar a intersecção
def existeInterseccao (r1,r2):
  if (((r1.x1<= r2.x1 <= r1.x2 ) 
  or (r1.x1<= r2.x2 <= r1.x2 ) )
  and ((r1.y1<= r2.y1 <= r1.y2 ) 
  or (r1.y1<= r2.y2 <= r1.y2 ))):
    return 'Existe'
  else:
    return "Não existe"
#imprimi resultados chamando o metodo
print(existeInterseccao(a,b),"intersecção entre A e B")
print(existeInterseccao(a,c),"intersecção entre A e C")
print(existeInterseccao(b,c),"intersecção entre B e C")


