class Pessoa:
    populacao = 0 #Atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1

    @classmethod
    def mostrar_populacao(cls): #Método de ckasse
        print(f"A população atual é  {cls.populacao}")

pessoa1 = Pessoa("Maria")
pessoa2 = Pessoa("João")
pessoa3 = Pessoa("Petter")

Pessoa.mostrar_populacao() # Saída: A população atual é 2