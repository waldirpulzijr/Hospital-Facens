from entidades.pacientes import Paciente
from entidades.pacientes import ListarPacientes
from processar.pacientes import ProcessarPaciente

class OperacoesPaciente():
    def __init__(self, Paciente=None):
        self.__processar = ProcessarPaciente()
        self.__paciente = Paciente

    def load(self):
        lista = self.__processar.read_file()
        lista_pacientes = ListarPacientes()

        if lista.count == 0:
            return lista
        else:
            for linha in lista:
                paciente = Paciente(linha[0], linha[1], linha[2], linha[3])
                lista_pacientes.inserir(paciente)
            return lista_pacientes    

    def save(self):
        self.__processar.wrote_file(
            self.__paciente
        )
