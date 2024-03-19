from datetime import date
from anuncio import Video,Display,Social
from error import LargoExcedidoError
class Campania():
    MAX_CARACTERES=250 #Cantidad máxima de caracteres para el nombre de campaña
    
    def __init__(self, nombre:str, fecha_inicio:date,fecha_termino:date,anuncios:list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios)
        
    def _crear_anuncios(self, anuncios: list):
        '''
        Método privado que permite la creación de una lista de anuncios
        Parameter
        -----------
        anuncios
            Type:   Lista de tuplas [(formato, datos de anuncio)]
            Ejemplo:    [
                            ("Video",{"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "instream","duracion":10}),
                            ("Social",{"ancho":10, "alto":25,"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "linkedin"})
                        ]
            
        Return
        -----------
        anunciosList
            Type:   Lista de objetos Video, Display y/o Social
            Descripcion:    Lista de objetos subtipo de Anuncios
        '''
        anunciosList = []
        for data in anuncios:  
            if "Video" == data[0]:
                anunciosList.append(Video(**data[1]))
            if "Display" == data[0]:
                anunciosList.append(Display(**data[1]))
            if "Social" == data[0]:
                anunciosList.append(Social(**data[1]))
        return anunciosList
                
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > self.MAX_CARACTERES:
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
    anuncios_data = [
        ("Video",{"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "instream","duracion":10}),
        ("Social",{"ancho":10, "alto":25,"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "linkedin"}),
        ("Display",{"ancho":10, "alto":25,"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "native"}),
        ("Video",{"url_archivo": "archivo2", "url_clic": "clic1", "sub_tipo": "instream","duracion":10}),
    ]


    campania = Campania("Campaia1","2023-01-01","2023-02-01", anuncios_data)
    print(campania)

