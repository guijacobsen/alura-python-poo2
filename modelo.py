class Filme:
    def __init__(self, nome, ano, duracao):
      self.__nome = nome.title()
      self.ano = ano
      self.duracao = duracao
      self.__likes = 0

    def dar_like(self):
      self.__likes += 1

    @property
    def likes(self):
      return self.__likes

    @property
    def nome(self):
      return self.__nome

    @nome.setter
    def nome(self, nome):
      self.__nome = nome.title()
    

class Seria:
    def __init__(self, nome, ano, temporadas):
      self.__nome = nome.title()
      self.ano = ano
      self.temporadas = temporadas
      self.__likes = 0

    def dar_like(self):
      self.__likes += 1
    
    @property
    def likes(self):
      return self.__likes
    
    @property
    def nome(self):
      return self.__nome

    @nome.setter
    def nome(self, nome):
      self.__nome = nome.title()

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Seria('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


atlanta.dar_like()
atlanta.dar_like()

vingadores.dar_like()

vingadores.nome = 'vingadores - ultimato'

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')