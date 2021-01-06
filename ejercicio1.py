def leer_frase():
    try:
       return input("ingresa una frase o texto: ")
    except ValueError as e:
        print('Error:', e)

def contar_vocales(txt):
    count = 0
    for i in 'aeiou':
        for j in txt:
            if i == j :
                count +=1
    print("el numero de vocales es: ", count)


contar_vocales(leer_frase())
