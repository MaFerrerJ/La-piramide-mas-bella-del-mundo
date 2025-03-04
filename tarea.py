print("Bienvenid@ al programa de pagos para la construcción de la piramide")
print("Seleccione una opción\n")
op=1
empleados = {
    "Juan Arias": {'salario': 900000, 'horas_tardanza': 2},
    "Obi Wan Kenobi": {'salario': 7850000, 'horas_tardanza': 1},
    "Padme Amidala": {'salario': 6600000, 'horas_tardanza': 0},
    "Anakin skywalker": {'salario': 8000000, 'horas_tardanza': 3},
    "Luke Skywalker": {'salario': 5680000, 'horas_tardanza': 4},
}
while op != 4: #Se ejecuta mientras op sea diferente de 4
    print("1.Ingresar empleado\n2.Ingresar Salario\n3.Listar los empleados\n4.Salir") #Muestra las opciones
    op = int(input("Ingresa una opcion: ")) # Usuario ingresa opcion
    if op == 1:
        nombre_trabajador = input("Ingrese nombre del trabajador: ")
        empleados[nombre_trabajador] = {'salario': None, 'horas_tardanza': 0}  # Inicializa salario como None y horas de tardanza como 0
        print(f"Empleado {nombre_trabajador} ingresado.")
    elif op == 2:
            if empleados:
                nombre_trabajador = input("Ingrese nombre del trabajador: ")
                if nombre_trabajador in empleados:
                    horas_trabajadas = float(input("Ingrese número de horas trabajadas: "))
                    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))          
                    
                    # HORAS EXTRAS
                    if(horas_trabajadas > 40):
                        pago_total = (horas_trabajadas-40)*1.2*tarifa_por_hora + 40*tarifa_por_hora
                        #print("El pago total para ", nombre_trabajador, " es: ", pago_total)
                    else:
                        pago_total = horas_trabajadas*tarifa_por_hora
                        #print("El pago total para ", nombre_trabajador, " es: ", pago_total)
            
                
                    #DESCUENTO POR TARDANZA
                    numero_horas_tardanza = int(input("Ingrese el numero de horas de tardanza: "))
                    empleados[nombre_trabajador]["horas_tardanza"] = numero_horas_tardanza  
                    if numero_horas_tardanza >= 3:
                        print(f"El trabajador  {nombre_trabajador} tiene un descuento por tardanza del 5%")
                        pago_total -= pago_total * 0.05
                    
                    # BONIFICACION
                    if pago_total > 600000:
                        print(f"El trabajador {nombre_trabajador} tiene una bonificación de 50,000 pesos")
                        pago_total += 50000
                    
                    empleados[nombre_trabajador]["salario"] = int(pago_total)              
                    print(f"El pago total para {nombre_trabajador} es: {pago_total}")
                else:
                    print("El trabajador no esta registrado")
            else:
                print("No se ha ingresado un trabajador\nIngrese una opcion valida\n")
    elif op == 3:
        print("Lista de empleados")
        if empleados:
            for empleado, datos in empleados.items():
                print(f"Empleado: {empleado}")
                print(f"Salario: {datos['salario']}")
                if datos['salario'] is None:
                    print(f"El trabajador {empleado} no ha ingresado su salario\n")    
                print(f"Horas de tardanza: {datos['horas_tardanza']}\n")
                print("\n")
                                 
        else:
            print("No se ha ingresado un trabajador\nIngrese una opcion valida\n")
    elif op == 4:
        print("Salir")
    else:
        print("Ingrese una opcion valida")   