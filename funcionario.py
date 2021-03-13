# Tipos funcionarios
class Funcionario:

  def __init__(self,nome):
    self.nome = nome.title()

  def registra_horas(self, horas):
    print('Horas registradas...')
  
  def mostrar_tarefas(self):
    print('Fez muita coisa...')

class FuncionarioCaelum(Funcionario):
  def mostrar_tarefas(self):
    print('Fez muita coisa Caelum')
  
  def busca_cursos_do_mes(self, mes=None):
    print('Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mes')

class FuncionarioAlura(Funcionario):
  def mostrar_tarefas(self):
    print('Fez muita coisa Alura')
  
  def busca_perguntas_sem_respostas(self):
    print('Mostrando perguntas nao respondidas no forum')

class Hispter:
  def __str__(self):
    return f'Hispter, {self.nome}'

# Niveis funcionarios
class Junior(FuncionarioAlura):
  pass

class Pleno(FuncionarioAlura,FuncionarioCaelum):
  pass

class Senior(FuncionarioAlura, FuncionarioCaelum, Hispter):
  pass


# funcionarios
joao = Junior('joao')
guilherme = Pleno('guilherme')
pedro = Senior('pedro')

# print(f'{joao.nome}')
# print(f'{guilherme.nome}')
# print(f'{pedro.nome}')

print(f'str guilherme:  {str(guilherme)}')
print(f'str pedro:  {str(pedro)}')


# joao.busca_perguntas_sem_respostas()
# guilherme.busca_perguntas_sem_respostas()
# guilherme.mostrar_tarefas()