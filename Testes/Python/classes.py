class Esportes:
    def __init__ (self, nome, local, tipo, participantes):
        self.nome = nome
        self.local = local
        self.tipo = tipo
        self.participantes = participantes
        
    def get_qtd_participantes(self):
        return f"O esporte {self.nome} é praticado com {self.participantes} atletas."
    
volei = Esportes('Volei', 'Quadra', 'Em grupo', '6')

qtd_participantes = volei.get_qtd_participantes()
print('Quantidade de participantes:', qtd_participantes)

# Herança

class Volei(Esportes):
    def __init__(self, nome, local, tipo, participantes, objeto):
        self.objeto = objeto
        
        super().__init__(nome, local, tipo, participantes)
        
    def get_objeto(self):
        if self.objeto == 'Sim':
            return f"Este jogo precisa de algum objeto para ser praticado!"
        else:
            return f"Este jogo não precisa de objeto para ser praticado!"

atletismo = Volei('Atletismo', 'Pista', 'Individual', '1', 'Não')
print(atletismo.get_objeto())
volei = Volei('Volei', 'Quadra', 'Em grupo', '6', 'Sim')
print(volei.get_objeto())

# Polimorfismo

class TipoVolei:
    def __init__(self):
        pass
    
    def form_local(self):
        return 'Indefinida'
    
class VoleiPraia(TipoVolei):
    def __init__(self, local):
        self.local = local
        super().__init__()
 
    def form_local(self):
        return f"O tipo de quadra do volei de praia é de {self.local}."
    
local_praia = VoleiPraia('areia')
print(local_praia.form_local())

# Encapsulamento

class Regras:
    
    def __get_acesso_regras(self):
        return "Alteração das regras autorizada"
    
    def acesso_regras(self, entidade):
        if entidade == 'FIVB':
            return self.__get_acesso_regras()
        return "Você não tem acesso a alteração de regras do esporte."
    
regras = Regras()
print(regras.acesso_regras('CBF'))
print(regras.acesso_regras('FIVB'))
