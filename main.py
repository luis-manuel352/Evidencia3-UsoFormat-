# Utilizaremos valores de uso String en las variables para calcular el area del triangulo
# Utilizaremos el uso format para que nos muestre en la pantalla el procedimiento

base = 7
altura = 9
AreaTriangulo = (base * altura)/ 2 
txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
print(txt.format(base, altura, AreaTriangulo))
print(AreaTriangulo)
