class Vuelo:
    def __init__(self, num_vuelo, destino, asientos_disp):
       self.num_vuelo = num_vuelo 
       self.destino = destino
       self.asientos_disp = asientos_disp
       
       
class Reserva:
    def __init__(self, nombre_pasajero, vuelo):
        self.nombre_pasajero = nombre_pasajero
        self.vuelo = vuelo
        
class SistemaReservas:
    def __init__(self):
        self.lista_vuelos = []
        self.lista_reservas = []
        
        # --- DATOS DE PRUEBA ---
        # 1. Fabricamos un par de vuelos (ajustá los nombres de los atributos a los tuyos)
        vuelo_1 = Vuelo("1", "Buenos Aires", 10)
        vuelo_2 = Vuelo("2", "Santiago del Estero", 5)
        
        # 2. Los guardamos en la lista de la "cocina"
        self.lista_vuelos.append(vuelo_1)
        self.lista_vuelos.append(vuelo_2)
        
    def agregar_vuelo(self, vuelo):
        self.lista_vuelos.append(vuelo)
    
    def obtener_vuelos(self):
        return self.lista_vuelos
    
    def realizar_reserva(self, nombre_pasajero, num_vuelo_buscado):
        for vuelo in self.lista_vuelos:
            if vuelo.num_vuelo == num_vuelo_buscado:
                if vuelo.asientos_disp > 0:
                    vuelo.asientos_disp = vuelo.asientos_disp -1
                    self.lista_reservas.append(Reserva(nombre_pasajero, vuelo))
                    return True
                else: 
                    return self.vista.mostrar_mensaje("No hay asientos disponibles para este vuelo")
            return self.vista.mostrar_mensaje("No se encontro el vuelo solicitado")
        return False
    
    def obtener_reservas(self):
        return self.lista_reservas
                
            
            