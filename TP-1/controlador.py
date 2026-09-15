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
            elif opcion == 3:
                reservas_encontradas = self.modelo.obtener_reservas()
                self.vista.mostrar_reservas(reservas_encontradas)
            elif opcion == 4:
                    break
            else:   
                self.vista.mostrar_mensaje("Opcion invalida, por favor ingresa una opcion valida")


from modelo import SistemaReservas
from vista import VistaConsolaReservas

if __name__ == "__main__":
    # 1. Creamos las piezas
    mi_modelo = SistemaReservas()
    mi_vista = VistaConsolaReservas()
    
    # 2. Creamos el controlador y le pasamos las piezas
    mi_controlador = ControladorReservas(mi_modelo, mi_vista)
    
    # 3. Arrancamos el motor
    mi_controlador.iniciar()