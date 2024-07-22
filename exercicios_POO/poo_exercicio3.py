"""
3 - Crie as classes Televisao com atributo status, volume, canal e ControleRemoto
    com o atributo televisao, de forma que:

    a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto
    via controle remoto;
    b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
    c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
    permitir que seja informado um número de canal para efetuar a troca;
"""

class Televisao:

    def __init__(self):
        self.status = False
        self.__volume = 0
        self.__canal = 0

    @property
    def status(self) -> bool:
        return self.__status
    

    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status

    @property
    def volume(self) -> int:
        return self.__volume 
   
    @volume.setter
    def volume(self, volume: int) -> None:
        self.__volume = volume

    @property
    def canal(self) -> int:
        return self.__canal

    @canal.setter
    def canal(self, canal: int) -> None:
        self.__canal = canal

    def ligar_desligar(self) -> None:
        self.status = not self.status
        print(f'Televisão: {self.status}') 

    def aumentar_volume(self) -> None:
        self.__volume += 1
        print(f'Volume: {self.__volume}') 
   
   
    def diminuir_volume(self) -> None:
        self.__volume -= 1
        print(f'Volume: {self.__volume}') 


    def aumentar_canal(self) -> None:
        self.__canal += 1
        print(f'Canal: {self.__canal}') 
   
   
    def diminuir_canal(self) -> None:
        self.__canal -= 1
        print(f'Canal: {self.__canal}') 


    def mudar_canal(self, canal: int) -> None:
        self.__canal = canal
        print(f'Canal: {self.__canal}') 





class ControleRemoto:

    def __init__(self, televisao: Televisao):
        self.__televisao : Televisao = televisao

    @property
    def televisao(self) -> Televisao:
        return self.__televisao

    def ligar_desligar(self) -> None:
        self.__televisao.ligar_desligar()


    def aumentar_canal(self) -> None:
        self.__televisao.aumentar_canal()
    
    def diminuir_canal(self) -> None:
        self.__televisao.diminuir_canal()

    def mudar_canal(self, canal: int) -> None:
        self.__televisao.mudar_canal(canal)


    def aumentar_volume(self) -> None:
        self.__televisao.aumentar_volume()
    
    def diminuir_volume(self) -> None:
        self.__televisao.diminuir_volume()



if __name__ == "__main__":
    tv: Televisao = Televisao()

    tv.aumentar_canal()
    tv.aumentar_canal()
    tv.aumentar_canal()

    tv.mudar_canal(50)

    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.ligar_desligar()
    tv.ligar_desligar()

    controle : ControleRemoto = ControleRemoto(tv)

    controle.ligar_desligar()
    controle.aumentar_canal()