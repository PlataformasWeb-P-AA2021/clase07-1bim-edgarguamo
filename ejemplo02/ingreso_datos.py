from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
import requests
# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
sesion = Session()

df_clubs = open('./data/datos_clubs.txt','r')
df_jugadores = open('./data/datos_jugadores.txt','r')
lista_clubs = list(df_clubs)
lista_jugadores = list(df_jugadores)

datos_jugadores = []
datos_clubs = []

for l in lista_clubs:
    l = l.replace('\n','')
    datos_clubs = l.split(';')
    clubes = Club(nombre=datos_clubs[0], deporte= datos_clubs[1],\
            fundacion= int(datos_clubs[-1]))
    sesion.add(clubes)
    print(datos_clubs)

for lj in lista_jugadores:
    lj = lj.replace('\n','')
    datos_jugadores = lj.split(';')
    jugadores = Jugador( nombre = datos_jugadores[3],\
            dorsal = int(datos_jugadores[2]),\
            posicion = datos_jugadores[1],\
            club = sesion.query(Club).filter_by(nombre=datos_jugadores[0]).one())
    sesion.add(jugadores)
    print(int(datos_jugadores[2]))

sesion.commit()
df_clubs.close()
df_jugadores.close()
