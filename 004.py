# Dissecando uma variável
x = input('Digite algo:')
print('O tipo primitivo desse valor é', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabetico?', x.isalpha())
print('Tem letras e números?', x.isalnum())
print('Está em maiusculas?', x.isupper())
print('Está em minusculas?', x.islower())
print('Está capitalizada?', x.istitle())