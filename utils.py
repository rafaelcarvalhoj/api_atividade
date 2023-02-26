from models import Pessoas, db_session

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Carvalho', idade=18)
    print(pessoa)
    pessoa.save()

# Consulta pessoas
def consulta():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(i)
    # pessoa = Pessoas.query.filter_by(nome='Carvalho').first()


# Altera dados na tablea pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'Carlao'
    pessoa.idade = 76
    pessoa.save()


# Exclui na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Carlao').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta()
