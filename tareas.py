# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento, brocoli y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.

# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.

# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

# Tambien mostrar el precio

# Pizza vegetariana: 49.99 soles
# Pizza no vegetariana: 59.99 soles
# Recordar que tambien se hace servicio de delivery a 8 soles.

pedido = input('''hola bienvenido a La 
pizzería Bella Napoli 
desea una pizza ?
la vegetariana esta 49.99 
y la carnivora seria 59.99 
con delivery la vegetaria 
costaria 57.99 y la carnivora seria 67.99 : ''')
delivery = input("¿desea delivery?: ")

if delivery ==  'si' and pedido == "vegetariana":
    print("perfecto los ingredientes que tiene para elegir son los siguientes solo puede elegir uno ")
    print("1 Pimiento")
    print("2 brocoli")
    print("3 tofu")
    ingredientes = int(input("cual decea el 1 el 2 o el 3 : "))
    if ingredientes == 1:      
        print('''ya esta lista su pizza es vegetariana lleva motzarela, salsa de tomate y pimientos cuesta
             57.99''')
    elif ingredientes == 2:
        print('''es vegetariana lleva motzarela, salsa de tomate y brocoli cuesta
                  57.99''')
    elif ingredientes == 3:
            print('''es vegetariana lleva motzarela, salsa de tomate y tofu cuesta
                  57.99''')
    else:
         print('''no decea ingredientes entonces su pizza lleva motzarela y salsa de tomate
               50.00''')
elif delivery ==  'no' and pedido == "vegetariana":
    print("perfecto los ingredientes que tiene para elegir son los siguientes solo puede elegir uno ")
    print("1 Pimiento")
    print("2 brocoli")
    print("3 tofu")
    ingredientes = int(input("cual decea el 1 el 2 o el 3 : "))
    if ingredientes == 1:      
        print('''ya esta lista su pizza es vegetariana lleva motzarela, salsa de tomate y pimientos cuesta
             49.99''')
    elif ingredientes == 2:
        print('''es vegetariana lleva motzarela, salsa de tomate y brocoli cuesta
                  49.99''')
    elif ingredientes == 3:
            print('''es vegetariana lleva motzarela, salsa de tomate y tofu cuesta
                  49.99''')
    else:
         print('''no decea ingredientes entonces su pizza lleva motzarela y salsa de tomate
               50.00''')
elif delivery == "no" and pedido == "carnivora":
    print("perfecto los ingredientes que tiene para elegir son los siguientes solo puede elegir uno ")
    print("1 Peperoni")
    print("2 Jamon")
    print("3 Salmon")
    ingredientes_carnivora = int(input("cual decea el 1 el 2 o el 3 : "))
    if ingredientes_carnivora == 1:      
        print('''ya esta lista su pizza es carnivora lleva motzarela, salsa de tomate y peperoni cuesta
             59.99''')
    elif ingredientes_carnivora == 2:
        print('''ya esta lista su pizza es carnivora lleva motzarela, salsa de tomate y jamon cuesta
                  59.99''')
    elif ingredientes_carnivora == 3:
            print('''es vegetariana lleva motzarela, salsa de tomate y salmon cuesta
                  59.99''')
    else:
         print('''no decea ingredientes entonces su pizza lleva motzarela y salsa de tomate
               50.00''')
elif delivery == "si" and pedido == "carnivora":
    print("perfecto los ingredientes que tiene para elegir son los siguientes solo puede elegir uno ")
    print("1 Peperoni")
    print("2 Jamon")
    print("3 Salmon")
    ingredientes_carnivora = int(input("cual decea el 1 el 2 o el 3 : "))
    if ingredientes_carnivora == 1:      
        print('''ya esta lista su pizza es carnivora lleva motzarela, salsa de tomate y peperoni cuesta
             67.99''')
    elif ingredientes_carnivora == 2:
        print('''ya esta lista su pizza es carnivora lleva motzarela, salsa de tomate y Jamon cuesta
                  67.99''')
    elif ingredientes_carnivora == 3:
            print('''es vegetariana lleva motzarela, salsa de tomate y Salmon cuesta
                  67.99''')
    else:
         print('''no decea ingredientes entonces su pizza lleva motzarela y salsa de tomate
               50.00''')
else:
     print('''no?
           entonces vuelva pronto :)''')