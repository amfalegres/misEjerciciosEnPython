# Para el lanzamiento del videojuego Hallow Night, se debe crear la siguiente funcionalidad:

# La moneda se llama Yeo y se le debe pedir al usuario que ingrese un cantida entera entre 0 y 4500 yeos.
# Luego se debe preguntar al usuario si quiere comprar items en la tienda de Ipgy.
# Si la respuesta es si, se la cantidad es mayor a 0, se mostrara la lista de items; sino se le mostrara el mensaje "No se aceptan misios XD"
# La lista de items debe ser algo asi: Nombre | Precio | Descripcion del Item
# Una vez el usuario eliga, se debe mostrar el saldo actual que le queda y el item comprado

yeo = int(input("ingrese una cantidad de yeo del 0 hasta el 4500: "))
entrada = input("quisiera entrar ala tienda de ipgy? : ")
print(yeo)

if entrada == "si" and yeo > 0:
    print(''''             items
          sans:  1000yeo    cuando te matan te da una vida extra
          papy:  300yeo     tienes un escudo a tu alrededor, cada ves que te golpean por 5 segundos
          alg:   2000yeo    puedes crear una banca cada hora
          XD:    100yeo     puedes lanzar un rayo lazer   ''')
    amuleto = int(input("cual desea el 1 el 2 el 3 o el 4: "))
    sans = 1000
    papy = 300
    alg = 2000
    XD = 100
    if amuleto == 1 and yeo - sans >= 0:
        print("ahora tierne el amuleto sans")
        print("le queda",yeo - sans)
    elif amuleto == 2 and yeo - papy >= 0:
        print("ahora tierne el amuleto papy")
        print("le queda",yeo - papy)
    elif amuleto == 3 and yeo - alg >= 0:
        print("ahora tierne el amuleto alg")
        print("le queda",yeo - alg)
    elif amuleto == 4 and yeo - XD >= 0:
        print("ahora tierne el amuleto XD")
        print("le queda",yeo - XD)
    else:
        print("no le alcanza")

elif entrada == "si" and yeo == 0:
    print("no se aceptan misios ahora ve a farmear com desgaciado")
else:
    print('''esta bien que tenga un buen dia
          *le desinstala el juego*''')
