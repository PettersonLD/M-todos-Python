class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome #Atributo de instância
        self.idade = idade
        
    def cumprimentar(self):
            print (f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def aniversario(self):
                self.idade += 1

pessoa = Pessoa("Maria", 30)
pessoa.cumprimentar()
pessoa.aniversario()
pessoa.cumprimentar()