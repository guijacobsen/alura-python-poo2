class Funcionario:
  def registra_horas(self, horas):
    print('Horas registradas...')
  
  def mostrar_tarefas(self):
    print('Fez muita coisa...')

class Funcionario2:
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
  # def mostrar_tarefas(self):
  #   print('Fez muita coisa Alura')
  
  def busca_perguntas_sem_respostas(self):
    print('Mostrando perguntas nao respondidas no forum')


class Junior(FuncionarioAlura):
  pass

class Pleno(FuncionarioAlura,FuncionarioCaelum):
  pass


# joao = Junior()
# joao.busca_perguntas_sem_respostas()


guilherme = Pleno()
# guilherme.busca_cursos_do_mes()
# guilherme.busca_perguntas_sem_respostas()

guilherme.mostrar_tarefas()