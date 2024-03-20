from campania import Campania
from error import LargoExcedidoError,SubTipoInvalidoError
import datetime
import os

def escribir_log (excepcion):
    '''
        Método que escribe error en un log diario. Este log escribe la fecha y hora del error más la descripción.
        Parameter
        -----------
        excepcion
            Type:   Exception
            
        '''
    try:
        archivo = f"log.{datetime.date.today()}.log"
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.abspath('logs/'+archivo), 'a') as log:
            log.write(f"[{fecha_hora}]  ERROR:  {str(excepcion)}\n")
    except OSError as e:
        print(f"Error al intentar crear y/o escribir el archivo log: {str(e)}")

try:
    anuncios_data = [("Video",{"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "instream","duracion":10})]
    campania = Campania("Campaia prueba","2024-01-01","2024-02-01", anuncios_data)

    try:
        nombre_campania = input("Por favor ingrese el nuevo nombre para la campaña\n")
        print(campania)
        
        campania.nombre = nombre_campania
        print(campania)
        
    except LargoExcedidoError as e:
        escribir_log(e)
        print("El nombre de la campaña excede el largo permitido")
    except Exception as e:
        escribir_log(e)
        print("Error no especificado")
        
    try:   
        print(f"Formato de anuncio: {campania.anuncios[0].FORMATO}")
        sub_tipo = input("Por favor ingrese el nuevo nombre para la campaña\n")
        campania.anuncios[0].sub_tipo=sub_tipo
        
        #campania.anuncios[0].redimensionar_anuncio()
    except SubTipoInvalidoError as e:
        escribir_log(e)
        print("El subtipo ingresado no coincide con el formato")
    except Exception as e:
        escribir_log(e)
        
except Exception as e:
    escribir_log(e)
    print("Error no especificado")
