class VistaConsolaReservas:
    def mostrar_menu(self):
        print("\n---Menu del Sistema---")
        print("1- Ver vuelos ")
        print("2- Reservar ")
        print("3- Ver Reservas ")
        print("4- Salir ")
        
    def mostrar_mensaje(self, mensaje):
        print(mensaje)
    
    def solicitar_datos_reserva(self):
        nombre = input("escribi tu nombre: ")
        numero = int(input("escribi el numero de vuelo: "))
        return nombre, numero
    
    def mostrar_vuelos(self, lista_vuelos):
        for vuelo in lista_vuelos:
            print(f"El vuelo numero: {vuelo.num_vuelo} con destino: {vuelo.destino} tiene: {vuelo.asientos_disp} asientos disponibles")
            
    def mostrar_reservas(self, lista_reservas):
        for reserva in lista_reservas:
            print(f"Reserva a nombre del pasajero {reserva.nombre_pasajero} con numero de vuelo numero {reserva.vuelo.num_vuelo} con destino {reserva.vuelo.destino}")