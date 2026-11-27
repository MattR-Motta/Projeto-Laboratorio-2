from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self,nome,rg,cpf,anoNasc,mesNasc,diaNasc,sexo):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.anoNasc = anoNasc
        self.mesNasc = mesNasc
        self.diaNasc = diaNasc
        self.sexo = sexo

    @abstractmethod
    def cadastrar(self):
        self.nome = input("Digite seu nome: ")
        self.rg = input("Digite seu RG: ")
        self.cpf = input("Digite seu CPF: ")
        self.anoNasc = int(input("Digite seu ano de nascimento: "))
        self.mesNasc = int(input("Digite seu mês de nascimento: "))                
        self.diaNasc = int(input("Digite seu dia de nascimento: "))
        self.sexo = input("Digite seu sexo: ")

    @abstractmethod
    def exibir(self):
        print("Nome: ",self.nome)
        print("RG: ",self.rg)
        print("CPF: ",self.cpf)
        print("Ano de nascimento: ",self.anoNasc)
        print("Mês de nascimento: ",self.mesNasc)
        print("Dia de nascimento: ".self.diaNasc)
        print("Sexo: ",self.sexo)
        
class Funcionario(Pessoa):
    def __init__(self,nome,rg,cpf,anoNasc,mesNasc,diaNasc,sexo,matricula,setor,cargo,nivel):
        super().__init__(nome,rg,cpf,anoNasc,mesNasc,diaNasc,sexo)
        self.matricula = matricula
        self.setor = setor
        self.cargo = cargo
        self.nivel = nivel

    def cadastrarFuncionario(self):
        self.cadastrar()
        self.matricula = int(input("Digite seu número de matrícula de funcionário: "))
        self.setor = input("Digite o setor que vocÊ trabalha: ")
        self.cargo = input("Digite o nome do cargo que você ocupa: ")
        self.nivel = int(input("Digite o seu nível: "))

    def exibirFuncionario(self):
        self.exibir()
        print("Matrícula: ",self.matricula)
        print("Setor: ",self.setor)
        print("Cargo: ",self.cargo)
        print("Nível: ",self.nivel)       


class Matricula:
    def __init__(self, id_matricula: int, mes_matricula: int, ano_matricula: int, aluno: "Aluno | None" = None, curso: "Curso | None" = None,):

        self.id_matricula = id_matricula
        self.mes_matricula = mes_matricula
        self.ano_matricula = ano_matricula
        self.aluno = aluno
        self.curso = curso


    def matricular(self) -> str:
        if self._aluno is None or self._curso is None:
            return "Erro: Aluno ou Curso não informado para realizar a matrícula."

        idade: int = self._ano_matricula - self._aluno.ano_nasc
        if idade < 18:
            return (
                f"Matrícula negada: {self._aluno.nome} possui {idade} anos "
                f"(A Faculdade Saber Supremo apenas aceita alunos maiores de 18 anos)."
            )

        valor_final: float = round(
            self._curso.valor * (1.0 - self._aluno.desconto / 100.0), 2
        )
        return (
            f"[MATRÍCULA #{self._id}] Data: {self._mes_matricula:02d}/{self._ano_matricula:04d} | "
            f"Aluno: {self._aluno.nome} (Cód. {self._aluno.codigo}, {idade} anos) | "
            f"Curso: {self._curso.titulo} | Valor Final: R$ {valor_final:.2f}"
        )

