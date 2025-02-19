class Calculadora:
    @staticmethod
    def somar(a, b): #Método Estático
        return a + b

resultado = Calculadora.somar(10, 5) #Chamado pela classe
print(resultado) # Saída: 15