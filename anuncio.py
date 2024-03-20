from abc import ABC, abstractmethod
from error import SubTipoInvalidoError
class Anuncio(ABC):
    def __init__(self, ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str) -> None:
        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 1
            
        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 1
            
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 1
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 1
    
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url):
        self.__url_archivo = url
    
    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url):
        self.__url_clic = url
    
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if type(self) == Video:
            if(sub_tipo in Video.SUB_TIPOS):
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoError("El subtipo ingresado no es valido")
        elif type(self) == Display:
            if(sub_tipo in Display.SUB_TIPOS):
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoError("El subtipo ingresado no es valido")
        elif type(self) == Social:
            if(sub_tipo in Social.SUB_TIPOS):
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoError("El subtipo ingresado no es valido")
            
    def mostrar_formatos():
        print(Video.FORMATO)
        print("===============")
        for valor in Video.SUB_TIPOS:
            print(valor)
        print(f"\n{Display.FORMATO}")
        print("===============")
        for valor in Display.SUB_TIPOS:
            print(valor)
        print(f"\n{Social.FORMATO}")
        print("===============")
        for valor in Social.SUB_TIPOS:
            print(valor)
    
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion:int) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        if duracion > 1:
            self.__duracion = duracion
        else:
            self.__duracion = 5
    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self,duracion):
        if duracion > 1:
            self.__duracion = duracion
        else:
            self.__duracion = 5
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
        
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
        
        
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
        
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
        
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
        
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
    

if __name__ == "__main__":
    Anuncio.mostrar_formatos()
    
    v = Video("txt","url2","instream",0)
    v.sub_tipo="outstream"
    print("NUEVO SUB TIPO:",v.sub_tipo)
    
    v.redimensionar_anuncio()
    
    v.sub_tipo="facebook"
            


        