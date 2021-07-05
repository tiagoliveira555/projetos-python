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
        print(8 * '##', 8 * '##')
        print(8 * '##', 'PESQUISAR VISITANTE', 8 * '##')
        print('DIGITE C SE QUISER CANCELAR E VOLTAR PARA O MENU')

        nome = input('Nome para pesquisar: ').strip().upper()
        if len(nome) != 0 and nome != 'C':
            db = sqlite3.connect('conexao.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM visitantes')
            lista = cursor.fetchall()
            for i in lista:
                if nome in i:
                    print('Esse visitante já possui cadastro!, i')
                    time.sleep(2)
                    update = input('Você deseja atualizar-lo? [S/N] ').upper()
                    if update == 'S':
                        self.nome = i[1]
                        self.empresa = i[2]
                        self.doc = i[3]
                        hora_e_date = int(time.time())
                        self.hora = str(datetime.datetime.fromtimestamp(hora_e_date).strftime('%Y-%m-%d %H:%M:%S'))
                        self.apt = input('Apt: ').strip().upper()

                        cursor.execute('''INSERT INTO visitantes
                                        (nome, empresa, doc, hora, apt) VALUES (?, ?, ?, ?, ?)''',
                                        (self.nome, self.empresa, self.doc, self.hora, self.apt))
                        print()
                        print('Cadastro realizado com sucesso!')
                        time.sleep(1)
                        db.commit()
                        db.close()
                        break

                    else:
                        print('Esse visitante não possui cadastro!')
                        p = input('Você deseja cadastra-lo? ')
                        time.sleep(1)
                        self.cadastrar()

        elif nome == 'C':
            print('Indo para tela principal')
            self.menu()


        else:
            print('Voltando para o Menu Prinicipal')
            self.menu()

    def cadastrar(self):
            rodando = True
            while rodando:
                print(8 * '##', 8 * '##')
                print(8 * '##', 'CADASTRAR VISITANTES', 8 * '##')
                print('DIGITE C SE QUISER CANCELAR E VOLTAR PARA O MENU')

                temp_name = input('Nome: ').strip().upper()
                if len(temp_name) >= 4 and temp_name != 'C':
                    db = sqlite3.connect('conexao.db')
                    cursor = db.cursor()
                    cursor.execute('SELECT id, nome FROM visitantes')
                    lista = cursor.fetchall()
                    for i in lista:
                        if temp_name in i:
                            print('Esse visitante já possui cadastro!')
                            time.sleep(2)
                            self.menu()

                    self.nome = temp_name
                    temp_name = ''
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

                elif temp_name == 'C':
                    print('Voltando para o Menu Principal')
                    time.sleep(2)
                    self.menu()

                elif len(temp_name) <= 3:
                    print('Não é permitido campos com mínimo de 3')
                    self.cadastrar()

                elif temp_name == '':
                    print('Preencha os campos corretamente.')
                    self.cadastrar()

                else:
                    print('NÃO FOI POSSÍVEL CADASTRAR, TENTE NOVAMENTE!')
                    self.cadastrar()

    def editar(self):
        print('-------------------------------------------------------------')
        print('----------- ATUALIZAR VISITANTES ---------')
        print('_____________________________________________________________')

        id_visitante = input('Digite o ID do visitante: ')
        confirma = input('Você tem certeza que deseja atualizar? [S/N]').lower()

        if confirma == 's':
            db = sqlite3.connect('conexao.db')
            cursor = db.cursor()

            nome_atualiza = input('Você deseja atualizar o nome? [S/N]').lower()
            if nome_atualiza == 's':
                nome = input('Nome: ').upper()
                cursor.execute('UPDATE visitantes SET nome=? WHERE id=?', (nome, id_visitante))
                db.commit()
                print('Nome atualizado com sucesso!')
                time.sleep(0.5)

            emprese_atualiza = input('Você deseja atualizar a empresa? [S/N]').lower()
            if emprese_atualiza == 's':
                empresa = input('Empresa: ').upper()
                cursor.execute('UPDATE visitantes SET empresa=? WHERE id=?', (empresa, id_visitante))
                db.commit()
                print('Empresa atualizada com sucesso!')
                time.sleep(0.5)

            doc_atualiza = input('Você deseja atualizar o documento? [S/N]').lower()
            if doc_atualiza == 's':
                doc = input('Documento: ').upper()
                cursor.execute('UPDATE visitantes SET doc=? WHERE id=?', (doc, id_visitante))
                db.commit()
                print('Documento atualizado com sucesso!')
                time.sleep(0.5)

            apt_atualiza = input('Você deseja atualizar o Apt? [S/N]').lower()
            if apt_atualiza == 's':
                apt = input('Apartamento: ').upper()
                cursor.execute('UPDATE visitantes SET apt=? WHERE id=?', (apt, id_visitante))
                db.commit()
                print('Apartamento atualizado com sucesso!')
                time.sleep(0.5)

            else:
                print('Voltando para o Menu Principal')
                time.sleep(2)
                self.menu()
        else:
            print('Voltando para o Menu Principal')
            time.sleep(2)
            self.menu()

    def visualizar(self):
        print('-------------------------------------------------------------')
        print('----------- VISUALIZAR TODOS VISITANTES CADASTRADOS ---------')
        print('_____________________________________________________________')

        db = sqlite3.connect('conexao.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM visitantes')
        lista = cursor.fetchall()
        for i in lista:
            print(f'{i[0]:<5}{i[1]:<20}{i[2]:<22}{i[3]:<20}{i[4]:<30}{i[5]:<6}')

        print()
        input('FIM DA LISTA DE CADASTROS! PRESSIONE QUALQUER TECLA PARA CONTINURA...')
        opcao = input('[A] ATUALIZAR [C] CADASTRAR [D] EXCLUIR [M] MENU PRINCIPAL: ').upper()
        if opcao == 'A':
            self.editar()
        elif opcao == 'C':
            self.cadastrar()
        elif opcao == 'D':
            self.deletar()
        elif opcao == 'M':
            self.menu()
        else:
            print('OPÇÃO INCORRETA! TENTA UMA DA LISTA ACIMA!')
            self.menu()

    def deletar(self):
        print('-------------------------------------------------------------')
        print('----------- DELETAR VISITANTES CADASTRADOS ---------')
        print('_____________________________________________________________')

        id_visitante = input("Digite o ID que deseja apagar: ")

        confirma = input('Você tem certeza que deseja apagar? [S/N] ').lower()
        if confirma == 's':
            db = sqlite3.connect('conexao.db')
            cursor = db.cursor()
            cursor.execute('''DELETE FROM visitantes WHERE id=?''', (id_visitante,))
            db.commit()
            print('APAGADO COM SUCESSO!')
            time.sleep(0.5)
            self.menu()

        else:
            print('Voltando para o Menu Principal')
            time.seep(0.5)
            self.menu()

    def sair(self):
        confirma = input('Você realmente deseja sair do sistema? [S/N]').lower()
        if confirma == 's':
            print('Saindo do sistema...')
            time.sleep(2)
            exit()
        else:
            print('Voltando para o menu principal...')
            self.menu()

    def menu(self):
        os.system('clear')
        print(14 * '---', 'MENU DE OPÇÕES: ', 14 * '---' )
        print()
        print(f"{'[1]Procurar':<18}{'[2]Cadastrar':<18}{'[3]Editar':<18}", end='')
        print(f"{'[4]Visualizar':<18}{'[5]Apagar':<18}{'[6]Sair':<18}")
        print()
        print(8 * '----', 'Visitantes cadastrados recentementes', 8 * '----')
        print(f'{"ID:":<5}{"Nome:":<20}{"Empresa:":<22}', end='')
        print(f'{"Documento:":<20}{"Hora/Data:":<30}{"Apt:":<6}')
        db = sqlite3.connect('conexao.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM visitantes')
        lista = cursor.fetchall()
        lista = lista[-5:]
        lista.reverse()
        for i in lista:
            print(f'{i[0]:<5}{i[1]:<20}{i[2]:<22}{i[3]:<20}{i[4]:<30}{i[5]:<6}')

        print()
        acao = int(input('Digite uma ação de 1 a 6: '))

        if acao == 1:
            self.procurar()

        elif acao == 2:
            self.cadastrar()

        elif acao == 3:
            self.editar()

        elif acao == 4:
            self.visualizar()

        elif acao == 5:
            self.deletar()

        elif acao == 6:
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
