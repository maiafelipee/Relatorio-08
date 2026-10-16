
class MortoVivo:
    def __init__(self, nome, almas, estus):
        
        self.nome = nome
        self._almas = almas
        self.__estus = estus

    def get_estus(self):
        
        return self.__estus

    def set_estus(self, quantidade):
        
        if quantidade >= 0 and quantidade <= 10:
            self.__estus = quantidade
        
        else:
            print("Quantidade de Estus inválida!")

    def mostrar_status(self):
        
        return f"Morto-vivo {self.nome} | Almas: {self._almas} | Estus: {self.__estus}"


class Clerigo(MortoVivo):
    def __init__(self, nome, almas, estus, milagre):
        
        super().__init__(nome, almas, estus)
        
        self.milagre = milagre

    def mostrar_status(self):
        
        
        
        return f"{super().mostrar_status()} | Milagre: {self.milagre}"


nome = input("Digite o nome: ")
almas = int(input("Digite a quantidade de almas: "))
estus = int(input("Digite a quantidade de Estus: "))
milagre = input("Digite o milagre: ")

clerigo = Clerigo(nome, almas, estus, milagre)
print(clerigo.mostrar_status())
quantidade = int(input("Digite a nova quantidade de Estus: "))
clerigo.set_estus(quantidade)

print(clerigo.mostrar_status())

 # print(clerigo.__estus) unexpected indent Entendi que isso acontece porque o atributo __estus foi declarado como privado dentro da classe MortoVivo. Por isso, não consigo acessá-lo diretamente pelo objeto clerigo no main. Para consultar esse valor, preciso utilizar o método get_estus(), que foi criado justamente para retornar a quantidade de Estus. Isso é um exemplo de encapsulamento em Python, que ajuda a controlar o acesso aos atributos de uma classe.
 # (pesquisei na IA o pq)
