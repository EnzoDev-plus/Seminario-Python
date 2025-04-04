def calculate_points(bajas,asistencias,muertes):
    """Esta funcion calcula y retorna el puntaje adecuado acorde a las kills,asistencias
         y muertes de cada jugador en cada ronda"""
    total = (bajas*3) + (asistencias*1) - (muertes*1 if muertes else 0)
    return total


#Diccionario con datos finales pedidos
estadisticas = {}

rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]


#Inicializo el diccionario de resultados vacio
jugadores = rounds[0].keys()
for jugador in jugadores:
        estadisticas[jugador] = {"kills": 0, "assists": 0 ,"deaths": 0, "MVP": 0 , "puntaje": 0}
    

for round_num, round in enumerate (rounds):
    if(round_num == 4):
         print(f"Ranking final: ")
         break
    print(f" Ronda numero: {round_num + 1}\n")
    
    max_puntaje = -999
    mvp = ""

    for player, resultado in round.items():
        bajas,asistencias,muertes = resultado["kills"],resultado["assists"],resultado["deaths"]
        points = calculate_points(bajas,asistencias,muertes)

        # Actualizo mvp de la ronda 
        if(points > max_puntaje):
             max_puntaje = points
             mvp = player
        
         # Actualizo estadisticas del jugador 
        estadisticas[player]["kills"] += bajas
        estadisticas[player]["assists"] += asistencias
        estadisticas[player]["deaths"] += muertes
        estadisticas[player]["puntaje"] += points

        # Actualizo cantidad de MVP'S al mvp
    if mvp: 
        estadisticas[mvp]["MVP"] += 1 

    # Imprimo datos de los jugadores al finalizar cada ronda
    for jugador, datos in estadisticas.items():
        print(f"{jugador}: {datos} \n")
  

       