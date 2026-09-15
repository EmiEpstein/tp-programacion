from fastapi import FastAPI

# Acá inicializamos nuestra aplicación
app = FastAPI(title="Sistema de Gestión de Turnos Médicos")

@app.get("/")
def bienvenida():
    return {"mensaje": "¡Hola! El servidor está funcionando perfecto."}