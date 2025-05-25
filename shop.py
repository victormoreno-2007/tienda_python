productos = ['pan','leche','cafe','tostada','coca-cola']
precios =[1500, 3700, 8500, 1000, 4500]
carrito=[]
cantidad=[]
total=0

nombreTienda = 'mi tienda '
print(f'bienvenidos a {nombreTienda}')


while True:
    menu = f"""  
       menu
1. productos
2. carrito ({len(carrito)} : ${total})
3. salir
"""
    print(menu)
    opcion=input('seleccione una opcion -> ')
    if opcion == '1':
        print(f'productos disponibles: {len(productos)}')
        for posicion in range(5):
            print('------------------------')
            print(f'{posicion + 1}.{productos[posicion]} $ {precios[posicion]}')
            print('---------------')
        input('comtinuar ...... ')


        
    elif opcion == '2':
        print(f'productos disponibles: {len(productos)}')
        for posicion in range(5):
            print('------------------------')
            print(f'{posicion + 1}.{productos[posicion]} $ {precios[posicion]}')
        busqueda = int(input('ingrese la posoicion del producto: '))-1
        if busqueda < 0 or busqueda >= len(productos):
            print('seleccione un rango especifico valido')
            input('contiar ..... ')
            continue
        cantidad_busqueda =int(input(f'ingrese la cantidad del producto: {productos[busqueda]} $ {precios[busqueda]} U:'))
        carrito.append(productos[busqueda])
        cantidad.append(cantidad_busqueda)
        total=total + (cantidad_busqueda * precios[busqueda])
        suma = cantidad_busqueda * precios[busqueda]
        total_pago = cantidad_busqueda * (precios[busqueda])
        print('si desea seleccionar otro producto seleccine de nuevo la opcion 2... GRACIAS¡¡¡¡¡')
        print('si quiere finalizar su compra seleccione la opcion 3  ')
       


    elif opcion == '3':
        for producto, precio in zip(carrito,cantidad):
            pre_unitario = precios[productos.index(producto)]
            sub_total = pre_unitario * precio
            print(f'{producto} = {sub_total}')
        print('gracias por su comprar!\nHasta la proxima 😘:) ')
        print(f'su total a cancelar es de : {total}')
        input('comtinuar ...... ')
       
        break
       
    else:
         print('opcion no valida')
    input('comtinuar ...... ')
    print(carrito)

