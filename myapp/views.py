from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import *
from .excel import *
from .plc import *
from datetime import date, datetime
import random

"""REAL"""

IP_ADDRESS="192.168.1.13"

"""PRUEBA CON EXCEL Y PLC"""

# def enviar_db(request):
#     try:
#         """LECTURA DEL EXCEL"""
#         url=""
#         celdas=""
#         valores_excel=leer_excel_periodico(loop=False)

#         """LECTURA DEL PLC"""
#         valores_plc=leer_db(IP_ADDRESS,6,0,6)
        
#         registro = datos_copeinca.objects.create(
#             fecha=date.today().strftime("%Y-%m-%d"),
#             hora=datetime.now().time().strftime("%H:%M:%S"),
#             caldero_1=valores_plc["caldero_1"],
#             caldero_2=valores_plc["caldero_2"],
#             caldero_3=valores_plc["caldero_3"],
#             caldero_4=valores_plc["caldero_4"],
#             caldero_5=valores_plc["caldero_5"],
#             caldero_6=valores_plc["caldero_6"],
#             caldero_7=valores_plc["caldero_7"],
#             caldero_8=valores_plc["caldero_8"],
#             energia=valores_excel["energia"],
#             velocidad=valores_excel["velocidad"],
#             liquido=valores_plc["liquido"]
#         )
#         time.sleep(0.5)

#         # Si la solicitud es AJAX, devolver JSON
#         if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#             # Devolver los datos del registro como respuesta JSON
#             response_data = {
#                 "fecha": registro.fecha,
#                 "hora": registro.hora,
#                 "caldero_1": registro.caldero_1,
#                 "caldero_2": registro.caldero_2,
#                 "caldero_3": registro.caldero_3,
#                 "caldero_4": registro.caldero_4,
#                 "caldero_5": registro.caldero_5,
#                 "caldero_6": registro.caldero_6,
#                 "caldero_7": registro.caldero_7,
#                 "caldero_8": registro.caldero_8,
#                 "energia": registro.energia,
#                 "velocidad": registro.velocidad,
#                 "liquido": registro.liquido
#             }
#             return JsonResponse(response_data)
        
#         # Si la solicitud no es AJAX, renderizar la página
#         renderizado = {
#             "fecha": registro.fecha,
#             "hora": registro.hora,
#             "caldero_1": registro.caldero_1,
#             "caldero_2": registro.caldero_2,
#             "caldero_3": registro.caldero_3,
#             "caldero_4": registro.caldero_4,
#             "caldero_5": registro.caldero_5,
#             "caldero_6": registro.caldero_6,
#             "caldero_7": registro.caldero_7,
#             "caldero_8": registro.caldero_8,
#             "energia": registro.energia,
#             "velocidad": registro.velocidad,
#             "liquido": registro.liquido
#         }

#         # Si es una solicitud normal, renderizar la página
#         return render(request, 'main_v2.html', renderizado)

#     except Exception as e:
#         print(f"Error al enviar los datos a la DB: {e}")
#         return JsonResponse({'error': str(e)}, status=500)
    
"""PRUEBA"""

def enviar_db(request):
    try:
        registro = {
            "fecha": date.today().strftime("%Y-%m-%d"),
            "hora": datetime.now().time().strftime("%H:%M:%S"),
            "caldero_1": bool(random.getrandbits(1)),
            "caldero_2": bool(random.getrandbits(1)),
            "caldero_3": bool(random.getrandbits(1)),
            "caldero_4": bool(random.getrandbits(1)),
            "caldero_5": bool(random.getrandbits(1)),
            "caldero_6": bool(random.getrandbits(1)),
            "caldero_7": bool(random.getrandbits(1)),
            "caldero_8": bool(random.getrandbits(1)),
            "energia": round(random.uniform(00.0, 200.0), 2),
            "velocidad": round(random.uniform(0.0, 10.0), 2),
            "liquido": round(random.uniform(0.0, 60.0), 2)
        }
        time.sleep(0.5)

        # Guardar en la base de datos
        datos_copeinca.objects.create(**registro)

        # Preparar los datos para la respuesta
        renderizado = {
            "fecha": registro["fecha"],
            "hora": registro["hora"],
            "caldero_1": registro["caldero_1"],
            "caldero_2": registro["caldero_2"],
            "caldero_3": registro["caldero_3"],
            "caldero_4": registro["caldero_4"],
            "caldero_5": registro["caldero_5"],
            "caldero_6": registro["caldero_6"],
            "caldero_7": registro["caldero_7"],
            "caldero_8": registro["caldero_8"],
            "energia": registro["energia"],
            "velocidad": registro["velocidad"],
            "liquido": registro["liquido"]
        }

        # Si la solicitud es AJAX, devolver JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse(renderizado)

        # Si es una solicitud normal, renderizar la página
        return render(request, 'main_v2.html', renderizado)

    except Exception as e:
        print(f"Error al enviar los datos a la DB: {e}")
        return JsonResponse({'error': str(e)}, status=500)


def obtener_ultimo_dato(request):
    try:
        # Obtener el último registro de la base de datos
        ultimo_registro = datos_copeinca.objects.last()
        
        if not ultimo_registro:
            return JsonResponse({'error': 'No hay datos almacenados'}, status=404)

        # Convertir el registro en un diccionario JSON
        datos = {
            'fecha': ultimo_registro.fecha,
            'hora': ultimo_registro.hora,
            'caldero_1': ultimo_registro.caldero_1,
            'caldero_2': ultimo_registro.caldero_2,
            'caldero_3': ultimo_registro.caldero_3,
            'caldero_4': ultimo_registro.caldero_4,
            'caldero_5': ultimo_registro.caldero_5,
            'caldero_6': ultimo_registro.caldero_6,
            'caldero_7': ultimo_registro.caldero_7,
            'caldero_8': ultimo_registro.caldero_8,
            'energia': ultimo_registro.energia,
            'velocidad': ultimo_registro.velocidad,
            'liquido': ultimo_registro.liquido
        }

        return JsonResponse({'ultimo_dato': datos})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
