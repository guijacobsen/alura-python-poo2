class Programa:
  def __init__(self, nome, ano):
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
    def __init__(self, nome, ano, duracao):
      self._nome = nome.title()
      self.ano = ano
      self.duracao = duracao
      self._likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
      self._nome = nome.title()
      self.ano = ano
      self.temporadas = temporadas
      self._likes = 0

   

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


atlanta.dar_like()
atlanta.dar_like()

vingadores.dar_like()

vingadores.nome = 'vingadores - ultimato'

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')