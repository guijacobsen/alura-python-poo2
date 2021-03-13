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

  def __str__(self):
    return f'Nome: {self.nome} - Likes: {self.likes}'
  # def __repr__(self):
  #   return f'Nome: {self.nome} - Likes: {self.likes}'


class Filme(Programa):
  total_classes = 0
  def __init__(self, nome, ano, duracao):
    Filme.total_classes += 1
    super().__init__(nome,ano)
    self.duracao = duracao

  def __str__(self):
    return f'Nome: {self.nome} - Duracao: {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome,ano)
    self.temporadas = temporadas

  def __str__(self):
    return f'Nome: {self.nome} - Temporadas: {self.temporadas} - Likes: {self.likes}'

   
class Playlist:
  def __init__(self, nome, programas):
    self.nome = nome
    self._programas = programas

  def __getitem__(self, item):
    return self._programas[item]
  
  def __len__(self):
    return len(self._programas)

  





vingadores = Filme('vingadores - guerra infinita', 2018, 160)
velozes = Filme('velozes e furiosos', 2018, 100)
atlanta = Serie('atlanta', 2018, 2)
lucifer = Serie('lucifer', 2014, 5)

lucifer.dar_like()
lucifer.dar_like()
lucifer.dar_like()
lucifer.dar_like()
lucifer.dar_like()

atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

velozes.dar_like()

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

list_filmes_e_series = [vingadores, velozes, atlanta, lucifer]
playlist_fim_de_semana = Playlist('fim de semana', list_filmes_e_series)

print(f'Tamanho playlist fim de semana: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
  print(programa)

print(f'lucifer in playlist_fim_de_semana? {lucifer in playlist_fim_de_semana}')
