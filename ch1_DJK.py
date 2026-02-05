import random
import time
import heapq

LIBRE = 0
EDIFICIO = 1
AGUA = 2
OBSTACULO = 3
INICIO = 4
SALIDA = 5
RUTA_VERDE = 6
RUTA_NARANJA = 7
EDIFICIOS = ["🏢", "🏦", "🏨"]

SIMBOLOS = {
    LIBRE: "⬛",  
    EDIFICIO: lambda: random.choice(EDIFICIOS),  # elige un edificio random
    AGUA: "🟦",   
    OBSTACULO: "🚦",
    INICIO: "🟢",
    SALIDA: "🔴",
    RUTA_VERDE: "🟩",
    RUTA_NARANJA : "🟧"  # ruta bloqueada por obstáculos
}

COSTOS = {
    LIBRE: 1,  
    AGUA: 5,   # mas caro que libre
    RUTA_VERDE: 2, # penaliza usar rutas anteriores
    RUTA_NARANJA : 2, 
    INICIO: 0,
    SALIDA: 0,
    OBSTACULO: float('inf'),
    EDIFICIO: float('inf')
}


def pedir_tamaño():
    while True:
        tamaño = input("Ingrese el tamaño de la matriz (filas, columnas): ").strip() # .strip para quitar espacios al principio y al final de la cadena
        
        try:
            filas_usuario, columnas_usuario = map(int, tamaño.split(","))

        except ValueError:
            print("Formato inválido. Usa fila, columna -> ejemplo: 3,5")
            continue
            
        if filas_usuario % 2 == 0:
            filas_usuario += 1
        if columnas_usuario % 2 == 0:
            columnas_usuario += 1
        
        return filas_usuario, columnas_usuario
    
    
def crear_mapa(filas, columnas):
    mapa = [[ EDIFICIO for _ in range(columnas)] for _ in range(filas)]

    for f in range(filas):
        for c in range(columnas):
            if (f % 3 == 0 or c % 3 == 0):
                mapa[f][c] = LIBRE
    return mapa




def mostrar_mapa(filas, mapa):
    
    for filas in mapa:
        fila_vista =[]
        for celda in filas:
            if celda == EDIFICIO:
                fila_vista.append(SIMBOLOS[EDIFICIO]())
            else:
                fila_vista.append(SIMBOLOS[celda])
        print(" ".join(fila_vista))
    print("\n")
        

def pedir_coordenadas(mapa, filas, columnas, mensaje):
    while True:
        entrada = input(mensaje).strip()
        
        try:
            y, x = map(int, entrada.split(","))
        except ValueError:
            print("Formato inválido. Usa fila, columna -> ejemplo: 3,5")
            continue
        if validar_coordenadas(mapa,y, x, filas, columnas):
            return y, x        

#funcion validar coordenadas ingresadas 
def validar_coordenadas(mapa, y, x, filas, columnas):
    
    if not (0 <= y < filas and 0 <= x < columnas):
        print("❌ La coordenada esta fuera de rango")
        return False
    if mapa[y][x] == EDIFICIO:
        print("❌ La coordenada coincide con un obstaculo")
        return False
    return True

def marcar_inicio_salida(mapa, inicio, salida):
    y1, x1 = inicio
    y2, x2 = salida
    mapa[y1][x1] = INICIO
    mapa[y2][x2] = SALIDA


def marcar_ruta(mapa, ruta, emoji, delay=0.1):
    for (y, x) in ruta:
        if mapa[y][x] not in (INICIO, SALIDA, OBSTACULO):
            mapa[y][x] = emoji
    mostrar_mapa(len(mapa), mapa)
    time.sleep(delay)
   

# añade agua de forma aleatoria en el mapa
def agregar_agua(mapa, prob= 0.2):
    filas, columnas = len(mapa), len(mapa[0])
    for f in range(filas):
        for c in range(columnas):
            if mapa[f][c] == LIBRE and random.random() < prob:
                mapa[f][c] = AGUA
    
#añade semaforos solo sobre la ruta calculada
def agregar_semaforos_en_ruta(mapa, ruta, cantidad = 2):
    if not ruta:
        return
    posiciones_disponibles = [pos for pos in ruta if mapa[pos[0]][pos[1]] == RUTA_VERDE]
    semaforos_a_poner = min(cantidad, len(posiciones_disponibles))
    semaforos_elegidos = random.sample(posiciones_disponibles, semaforos_a_poner) 
    for y, x in semaforos_elegidos:
        mapa[y][x] = OBSTACULO

# Funcion Dijkstra
def dijkstra(mapa, inicio, salida):
    filas, columnas = len(mapa), len(mapa[0])
    dist = {(y,x): float('inf') for y in range(filas) for x in range(columnas)}
    dist[inicio] = 0
    padres = {}
    movimientos = [(1,0), (-1,0), (0,1),(0,-1)]

    cola_imp = [(0, inicio)] # costo acumulado, nodo
    while cola_imp:
        costo, (y, x) = heapq.heappop(cola_imp)

        if (y, x) == salida:
            # reconstruir ruta
            ruta = []
            nodo = salida
            if nodo not in padres:
                return None
            
            while nodo != inicio:
                ruta.append((nodo))
                nodo = padres.get(nodo)
                if nodo is None:
                    return None
                
            ruta.append(inicio)
            ruta.reverse()
            return ruta
            
        for dy, dx in movimientos:
            ny, nx = y + dy, x + dx 
            if 0 <= ny < filas and 0 <= nx < columnas:
                nuevo_costo = costo + COSTOS[mapa[ny][nx]]
                if nuevo_costo < dist[(ny, nx)]:
                    dist[(ny, nx)] = nuevo_costo
                    padres[(ny, nx)] = (y, x)
                    heapq.heappush(cola_imp, (nuevo_costo, (ny, nx)))
    return None


def main():
    # pedir tamaño
    filas_usuario, columnas_usuario = pedir_tamaño()
    mapa = crear_mapa(filas_usuario, columnas_usuario)

    # mostrar mapa inicial
    mostrar_mapa(filas_usuario,  mapa)

    #pedir inicio y salida
    inicio = pedir_coordenadas(mapa, filas_usuario, columnas_usuario, "Ingrese las coordenadas de inicio (ej: 0,0): ")
    salida = pedir_coordenadas(mapa, filas_usuario, columnas_usuario, "Ingrese las coordenadas de salida (ej: 12,9): ")
    marcar_inicio_salida(mapa, inicio, salida)
    mostrar_mapa(filas_usuario, mapa)
    print("Se añadieron las coordenadas de inicio y salida exitosamente! \n")

   # calcular ruta inicial
    ruta = dijkstra(mapa, inicio, salida)
    if ruta:
        print("Ruta inicial encontrada!")
        marcar_ruta(mapa, ruta, RUTA_VERDE, delay=0.1)
        
    else:
        print("No hay ruta posible")

    # preguntar si añadir obstaculos
    obst = input("Desea añadir obstaculos? (s/n): ")
    if obst == "s":
        agregar_agua(mapa, prob=0.2)
        agregar_semaforos_en_ruta(mapa, ruta, 2)
    else:
        print("No se añadieron obstaculos")
        return
    
    if ruta:
        marcar_ruta(mapa, ruta, RUTA_NARANJA, delay=0.5)
       
    else:
        print("No habia ruta anterior")

    input("🚦Estos semáforos bloquean nuestro camino. \n mejor buscamos otra ruta (Enter para recalcular)...")

    # recalcular ruta
    ruta2 = dijkstra(mapa, inicio, salida)
    if ruta2:
        marcar_ruta(mapa, ruta2, RUTA_VERDE, delay=0.2)
        print("Nueva ruta encontrada! \n")
        print("Ruta anterior bloqueada = 🟧  \nRuta recalculada = 🟩\n")
        print("Ruta recalculada con exito!")

    else:
        print("NO hay ruta posible con los obstaculos añadidos")



if __name__ == "__main__":
    main()
