from datetime import date
from anuncio import Anuncio,Video,Display,Social
from error import LargoExcedidoError
class Campania():
    def __init__(self, nombre:str, fecha_inicio:date,fecha_termino:date,anuncios:dict) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios)
    def _crear_anuncios(self, anuncios: dict):
        anunciosList = []
        for formato, data in anuncios.items():  
            print("FORMATO:",formato)
            if "Video" in formato:
                anunciosList.append(Video(**data))
            if "Display" in formato:
                anunciosList.append(Display(**data))
            if "Social" in formato:
                anunciosList.append(Social(**data))
        return anunciosList
                
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoError("El nuevo nombre supera los 250 caracteres.")
        self.__nombre = nuevo_nombre
        
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha):
        self.__fecha_inicio = fecha
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha):
        self.__fecha_termino = fecha
    
    @property
    def anuncios(self):
        return self._anuncios
        
    def __str__(self):
        video=0
        display=0
        social=0
        for anuncio in self.anuncios:
            if isinstance(anuncio,Video):
                video +=1
            elif isinstance(anuncio,Display):
                display += 1
            elif isinstance(anuncio,Social):
                social += 1
            
        mensaje = f"""Nombre de la campaña: {self.__nombre}
    Anuncios: {video} Video(s), {display} Display, {social} Social"""
        return mensaje
    
    
if __name__ == "__main__":
    # Ejemplo de uso
    anuncios_data = {
        "Video1":{"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "instream","duracion":10},
        "Social1":{"ancho":10, "alto":25,"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "linkedin"},
        "Display1":{"ancho":10, "alto":25,"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "native"},
        "Video2":{"url_archivo": "archivo2", "url_clic": "clic1", "sub_tipo": "instream","duracion":10},
                     }


campania = Campania("Campaia1","2023-01-01","2023-02-01", anuncios_data)
print(campania)

