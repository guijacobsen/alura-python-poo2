class Programa:
  total_programas = 0
  def __init__(self, nome, ano):
    Programa.total_programas += 1
    self._nome = nome.title()
    self.ano = ano
    self._likes = 0

  def dar_like(self):
    self._likes += 1

  @property
  def likes(self):
    return self._likes

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome.title()

  def imprime(self):
    print(f'Nome: {self.nome} - Likes: {vingadores.likes}')


class Filme(Programa):
  total_classes = 0
  def __init__(self, nome, ano, duracao):
    Filme.total_classes += 1
    super().__init__(nome,ano)
    self.duracao = duracao

  def imprime(self):
    print(f'Nome: {self.nome} - Duracao: {self.duracao} min - Likes: {vingadores.likes}')

class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome,ano)
    self.temporadas = temporadas

  def imprime(self):
    print(f'Nome: {self.nome} - Temporadas: {self.temporadas} - Likes: {vingadores.likes}')

   


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
velozes = Filme('valozes e furiosos', 2018, 100)
atlanta = Serie('atlanta', 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()

# print(f'Total filmes: {Filme.total_classes}')
# print(f'Total programas: {Programa.total_programas}')
# print('-------------------------------------------')
filmes_e_series = [vingadores, velozes, atlanta]

for programa in filmes_e_series:
  programa.imprime()
  # print(str(programa))
  print('-------------------------------------------')