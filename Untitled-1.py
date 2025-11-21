print("¡Hola, mundo de Python en RAIZMIND!")
# Aquí irá el resto de tu código
# =============================================
#   RAÍZMIND - Cultivador de Hábitos Sostenibles
#   Autor: Jhamir Rivera Mendoza
#   Ingeniería en Ciberseguridad - UIDE 2025
# =============================================

import os
import time
from datetime import datetime, timedelta

# --- Datos persistentes ---
ARCHIVO = "raizmind_progreso.txt"
habitos = [
    "Usé botella reutilizable",
    "Ducha de menos de 5 minutos", 
    "Apagué luces al salir",
    "Reciclé correctamente",
    "Comí una comida sin carne",
    "Usé transporte público o bici",
    "Evité plásticos de un solo uso",
    "Compré local o de segunda mano",
    "Apagué dispositivos en standby",
    "Planté o cuidé una planta"
]

# --- Cargar progreso ---
def cargar_progreso():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if len(lineas) >= 6:
                return {
                    "nombre": lineas[0].strip(),
                    "puntos": int(lineas[1].strip()),
                    "racha": int(lineas[2].strip()),
                    "ultima_fecha": lineas[3].strip(),
                    "arboles_donados": int(lineas[4].strip()),
                    "record_racha": int(lineas[5].strip())
                }
    # Valores por defecto
    nombre = input("¡Bienvenid@ a RaízMind! ¿Cómo te llamas? ").strip() or "Ecohéroe"
    return {"nombre": nombre, "puntos": 0, "racha": 0, "ultima_fecha": "", 
            "arboles_donados": 0, "record_racha": 0}

# --- Guardar progreso ---
def guardar_progreso(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write(f"{datos['nombre']}\n")
        f.write(f"{datos['puntos']}\n")
        f.write(f"{datos['racha']}\n")
        f.write(f"{datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"{datos['arboles_donados']}\n")
        f.write(f"{datos['record_racha']}\n")

# --- Jardín ecológico ---
def mostrar_jardin(puntos):
    print("\n" + "="*50)
    print("         TU JARDÍN ECOLÓGICO")
    print("="*50)
    if puntos < 50:
        print("🌵 Tierra árida... ¡necesita vida!")
    elif puntos < 150:
        print("🌱 Primeras plantas brotando")
        print("🌳 Árbol joven")
    elif puntos < 300:
        print("🌸 Flores por todos lados")
        print("🌳🌳 Árboles creciendo")
        print("💧 Río cristalino")
    elif puntos < 500:
        print("🦜 Pájaros cantando")
        print("🦋 Mariposas volando")
        print("🌳🌳🌳 Bosque joven")
    else:
        print("🌍 ¡ECOSISTEMA COMPLETO Y VIVO!")
        print("🌳🌳🌳🌳🌳 Bosque maduro")
        print("🦌🦊🐦 Todos los animales han vuelto")
        print("¡ERES UN VERDADERO GUARDIÁN DEL PLANETA!")
    print("="*50)

# --- Menú principal ---
def menu():
    datos = cargar_progreso()
    hoy = datetime.now().strftime('%Y-%m-%d')
    
    # Verificar racha
    if datos["ultima_fecha"] != hoy:
        ultima = datetime.strptime(datos["ultima_fecha"], '%Y-%m-%d') if datos["ultima_fecha"] else None
        if ultima and (datetime.now().date() - ultima.date()).days > 1:
            datos["racha"] = 0  # Rompió la racha
        datos["ultima_fecha"] = hoy

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n🌱 ¡Hola {datos['nombre'].upper()}! Bienvenid@ a RaízMind 🌍\n")
        print(f"Puntos verdes: {datos['puntos']} | Racha: {datos['racha']} días 🔥")
        print(f"Árboles donados: {datos['arboles_donados']} 🌳\n")
        
        print("1. Marcar hábitos del día")
        print("2. Ver mi Jardín Ecológico")
        print("3. Canjear Puntos Verdes")
        print("4. Desafío Semanal")
        print("5. Mis Estadísticas")
        print("6. Salir")
        
        opcion = input("\nElige una opción → ")
        
        if opcion == "1":
            print("\n¿Qué hábitos cumpliste hoy?\n")
            puntos_hoy = 0
            for i, habito in enumerate(habitos, 1):
                print(f"{i}. {habito}")
            seleccion = input("\nNúmeros separados por coma (ej: 1,3,5) → ")
            nums = [int(x.strip())-1 for x in seleccion.split(",") if x.strip().isdigit()]
            for n in nums:
                if 0 <= n < len(habitos):
                    puntos_hoy += 10
                    print(f"✓ {habitos[n]} +10 puntos")
                    time.sleep(0.3)
            datos["puntos"] += puntos_hoy
            datos["racha"] += 1
            if datos["racha"] > datos["record_racha"]:
                datos["record_racha"] = datos["racha"]
            print(f"\n¡+{puntos_hoy} puntos! Total: {datos['puntos']}")
            time.sleep(2)
            
        elif opcion == "2":
            mostrar_jardin(datos["puntos"])
            input("\nPresiona Enter para volver...")
            
        elif opcion == "3":
            print(f"\nTienes {datos['puntos']} puntos disponibles")
            if datos["puntos"] >= 200:
                print("1. Donar 1 árbol real (200 puntos)")
            if datos["puntos"] >= 100:
                print("2. 10% descuento en tienda aliada (100 puntos)")
            if datos["puntos"] < 100:
                print("¡Sigue acumulando puntos!")
            else:
                canje = input("\n¿Qué quieres canjear? (o 0 para salir) → ")
                if canje == "1" and datos["puntos"] >= 200:
                    datos["puntos"] -= 200
                    datos["arboles_donados"] += 1
                    print("¡Árbol plantado con éxito! Gracias por salvar el planeta 🌳")
                elif canje == "2" and datos["puntos"] >= 100:
                    datos["puntos"] -= 100
                    print("¡Cupón del 10% generado! Código: RAIZ2025")
            time.sleep(3)
            
        elif opcion == "4":
            print("\nDESAFÍO SEMANAL: ¡Semana sin carne!")
            print("Cumple 4 días → +50 puntos extra")
            input("\nEnter para volver...")
            
        elif opcion == "5":
            co2 = datos["puntos"] * 0.5
            print(f"\nESTADÍSTICAS DE {datos['nombre'].upper()}")
            print(f"• Puntos totales: {datos['puntos']}")
            print(f"• Racha actual: {datos['racha']} días")
            print(f"• Récord histórico: {datos['record_racha']} días")
            print(f"• Árboles donados: {datos['arboles_donados']}")
            print(f"• CO₂ ahorrado estimado: {co2:.1f} kg")
            input("\nEnter para volver...")
            
        elif opcion == "6":
            guardar_progreso(datos)
            print("\n¡Progreso guardado! Nos vemos mañana 🌱")
            time.sleep(2)
            break

# === ¡RAÍZMIND COBRA VIDA! ===
if __name__ == "__main__":
    print("Cargando RaízMind...")
    time.sleep(1)
    menu()