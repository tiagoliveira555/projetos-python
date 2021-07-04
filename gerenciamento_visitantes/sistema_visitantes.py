import os, sqlite3, time, datetime


class visitantes:
    def __init__(self):
        self.id = ''
        self.nome = ''
        self.empresa = ''
        self.doc = ''
        self.hora = ''
        self.apt = ''

    def procurar(self):
        pass

    def cadastrar(self):
        rodando = True
        while rodando:
            print(8 * '##', 8 * '##')
            print(8 * '##', 'CADASTRAR VISITANTES', 8 * '##')

            self.nome = input('Nome Completo: ').strip().upper()
            time.sleep(0.6)
            self.empresa = input('Empresa: ').strip().upper()
            time.sleep(0.6)
            self.doc = input('Documento: ').strip().upper()
            time.sleep(0.6)
            hora_e_date = int(time.time())
            self.hora = str(datetime.datetime.fromtimestamp(hora_e_date).strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(0.6)
            self.apt = input('Apt: ').strip().upper()
            time.sleep(0.6)

            db = sqlite3.connect('conexao.db')
            cursor = db.cursor()

            cursor.execute('''INSERT INTO visitantes
                            (nome, empresa, doc, hora, apt) VALUES (?, ?, ?, ?, ?)''',
                            (self.nome, self.empresa, self.doc, self.hora, self.apt))
            print()
            print('Cadastro realizado com sucesso!')
            time.sleep(1)
            db.commit()

            adicionar_mais = input('Você deseja continuar cadastrando? [S/N] ').upper()
            if adicionar_mais == 'S':
                continue
            else:
                rodando = False
                db.close()
                print('Voltando para a tela principal!')
                time.sleep(1)
                self.menu()

    def editar(self):
        pass

    def visualizar(self):
        pass

    def deletar(self):
        pass

    def sair(self):
        pass

    def menu(self):
        os.system('clear')
        print(14 * '---', 'MENU DE OPÇÕES: ', 14 * '---' )
        print()
        print(f"{'[1]Procurar':<18}{'[2]Cadastrar':<18}{'[3]Editar':<18}{'[4]Visualizar':<18}{'[5]Apagar':<18}{'[6]Sair':<18}")
        print()
        print(8 * '----', 'Visitantes cadastrados recentementes', 8 * '----')
        print(f'{"ID:":<5}{"Nome:":<20}{"Empresa:":<22}{"Documento:":<20}{"Hora/Data:":<30}{"Apt:":<6}')
        print()
        acao = input('Digite uma ação de 1 a 6: ')

        if acao == '1':
            self.procurar()

        elif acao == '2':
            self.cadastrar()

        elif acao == '3':
            self.editar()

        elif acao == '4':
            self.visualizar()

        elif acao == '5':
            self.deletar()

        elif acao == '6':
            self.sair()

        else:
            print('OPÇÃO INVÁLIDA! DIGITE UMA AÇÃO ENTRE 1 E 6')
            time.sleep(1)
            self.menu()

    def janelaprincipal(self):
        os.system('clear')
        if os.path.isfile('conexao.db'):
            db = sqlite3.connect('conexao.db')
            print('Conectado com sucesso ao banco de dados')
            time.sleep(2)
            self.menu()

        else:
            print('Não existe arquivo de conexão!')
            time.sleep(2)
            print('Criando arquivo de conexão')
            time.sleep(2)
            db = sqlite3.connect('conexao.db')
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE if not exists Visitantes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            empresa TEXT NOT NULL,
                            doc TEXT NOT NULL,
                            hora TEXT NOT NULL,
                            apt TEXT NOT NULL)''')
            print('A conexão foi criada com sucesso!')
            time.sleep(2)
            self.menu()

        self.menu()


gerenciamento_visitantes = visitantes()
gerenciamento_visitantes.janelaprincipal()
