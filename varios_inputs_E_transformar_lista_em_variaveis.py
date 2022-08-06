# como separar um texto único em três variáveis diferentes
texto = input('informe 3 numeros: ') # --> 1,2,3
a,b,c = texto.split(',') # o separador informado deve ser o que é usado no imput
print(a) # --> 1
print(b) # --> 2
print(c) # --> 3

# da para separar uma lista em variáveis se o numero de variáveis for igual ao número de
# elementos na lista. EX. Essa lista possui 4 elementos, então precisa ter 4 variáveis, caso
# contrário, ocorrerá um erro.
cars = ['audi', 'bmw', 'subaru', 'toyota'] 
a,b,c,d = cars
print(a) # --> audi
print(b) # --> bmw
print(c) # --> subaru
print(d) # --> toyota
