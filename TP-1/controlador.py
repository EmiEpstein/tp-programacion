class ControladorReservas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        
    def iniciar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = int(input("Ingresa una opcion: "))
            
            if opcion == 1:
                vuelos_encontrados = self.modelo.obtener_vuelos()
                self.vista.mostrar_vuelos(vuelos_encontrados)
            elif opcion == 2:
                nombre, numero = self.vista.solicitar_datos_reserva()
                self.modelo.realizar_reserva(nombre, numero)