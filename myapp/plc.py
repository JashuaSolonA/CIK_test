import snap7
from snap7.util import *
import time

IP_ADDRESS="192.168.1.13"

def leer_db(IP_ADDRESS, db_number, start, finish):
    try:
        plc = snap7.client.Client()
        plc.connect(IP_ADDRESS, 0, 1)
        data = plc.db_read(db_number, start, finish)
        # Devuelve un diccionario con claves explicativas en lugar de una lista
        values = {
            "caldero_1": get_bool(data,0,0),
            "caldero_2": get_bool(data,0,1),
            "caldero_3": get_bool(data,0,2),
            "caldero_4": get_bool(data,0,3),
            "caldero_5": get_bool(data,0,4),
            "caldero_6": get_bool(data,0,5),
            "caldero_7": get_bool(data,0,6),
            "caldero_8": get_bool(data,0,7),
            "liquido": round(get_real(data, 2),2)
        }
        return values
    except Exception as e:
        print(f"Error al leer el db: {e}")
    time.sleep(0.5)
