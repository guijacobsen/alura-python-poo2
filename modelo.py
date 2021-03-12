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


class Filme(Programa):
  total_classes = 0
  def __init__(self, nome, ano, duracao):
    Filme.total_classes += 1
    super().__init__(nome,ano)
    self.duracao = duracao

class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome,ano)
    self.temporadas = temporadas

   


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
velozes = Filme('valozes e furiosos', 2018, 100)
atlanta = Serie('atlanta', 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')
print('-------------------------------------------')
print(f'Nome: {velozes.nome} - Ano: {velozes.ano} - Duracao: {velozes.duracao} - Likes: {vingadores.likes}')
print('-------------------------------------------')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

print('-------------------------------------------')
print(f'Total filmes: {Filme.total_classes}')
print(f'Total programas: {Programa.total_programas}')


print('-------------------------------------------')
filmes_e_series = [vingadores, velozes, atlanta]

print(f'filmes_e_series 0 nome: {filmes_e_series[0].nome}')