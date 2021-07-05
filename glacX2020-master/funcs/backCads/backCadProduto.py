from funcs.modulos import *

class CadProdutos:
    def add_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        tipser = 'Peça'
        hora = '1'

        self.cursor.execute("""
     		INSERT INTO servprod ( cod_sp, servprod, id_marcaprod, id_fornec, custo, valor, sp, descricao, tiposerv, hor)
     		VALUES ( ?, ?, ?, ?, ?, ?, "P", ?, ?, ?)""",
                       (cod_sp, servprod, id_marcaprod, id_fornec, custo, valor, descricao, tipser, hora))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
     		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Novo produto incluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def busca_produtoP(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()

        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
     		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
            self.entradaProd.delete(0, END)

        self.desconecta_Glac()
    def busca_marcaP(self):
        def add_autobind(event):
            self.conecta_Glac()

            listatec1.selection()

            for n in listatec1.selection():
                col1, col2 = listatec1.item(n, 'values')
                self.entradaIdMarcaprod.insert(END, col1)

            cod = self.entradaIdMarcaprod.get()

            addserv1cod = self.cursor
            addserv1cod.execute("""SELECT marca FROM marcaprod 
                WHERE cod_marca LIKE '%s'""" % cod)
            addservico1cod = self.cursor.fetchall()
            for i in addservico1cod:
                i = str(i)
                i = i.replace('(', '')
                i = i.replace(')', '')
                i = i.replace(',', '')
                i = i.replace("'", "")
                self.entradaMarcaprod.insert(END, i)

            self.desconecta_Glac()
            listatec.destroy()
        def OnTec(*args):
            listatec1.yview(*args)
            listatec12.yview(*args)
        ### Widgets - Listar tecnicos ###
        self.entradaMarcaprod.insert(END, '%')
        veicAuto = self.entradaMarcaprod.get()

        listatec = Toplevel()
        listatec.title("Marcas - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)
        listatec.transient(self.janelaProd)
        listatec.focus_force()
        listatec.grab_set()


        listatec1 = ttk.Treeview(listatec, height=10,
                            column=("col1", "col2"))
        listatec1.heading("#0", text="")
        listatec1.column("#0", width=0)
        listatec1.heading("#1", text="cod")
        listatec1.column("#1", width=50)
        listatec1.heading("#2", text="")
        listatec1.column("#2", width=220)
        listatec1.place(x=7, y=10)

        barra12 = Scrollbar(listatec, orient='vertical', command=OnTec)
        barra12.place(x=280, y=22, width=25, height=190)
        listatec1.configure(yscroll=barra12.set)

        # Binding da listbox
        listatec1.bind('<Double-1>', add_autobind)

        self.conecta_Glac()
        tec = self.cursor

        tec.execute("""SELECT cod_marca, marca 
            FROM marcaprod WHERE cod_marca LIKE '%s' 
            ORDER BY marca ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            listatec1.insert("", END, values=i)


        self.desconecta_Glac()

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
    def busca_fornecP(self):
        self.conecta_Glac()

        def add_autobind(event):
            self.conecta_Glac()

            listatec1.selection()

            for n in listatec1.selection():
                col1, col2 = listatec1.item(n, 'values')
                self.entradaIdFornec.insert(END, col1)

            cod = self.entradaIdFornec.get()

            addserv1cod = self.cursor
            addserv1cod.execute("""SELECT fornecedor FROM fornecedores 
            WHERE cod_forn LIKE '%s'""" % cod)
            addservico1cod = self.cursor.fetchall()
            for i in addservico1cod:
                i = str(i)
                i = i.replace('(', '')
                i = i.replace(')', '')
                i = i.replace(',', '')
                i = i.replace("'", "")
                self.entradaFornec.insert(END, i)

            listatec.destroy()

            self.desconecta_Glac()

        def OnTec(*args):
            listatec1.yview(*args)

        ### Widgets - Listar tecnicos ###

        self.entradaFornec.insert(END, '%')

        veicAuto = self.entradaFornec.get()

        listatec = Toplevel()
        listatec.title("Fornecedores - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)
        listatec.transient(self.janelaProd)
        listatec.focus_force()
        listatec.grab_set()

        listatec1 = ttk.Treeview(listatec, height=10,
                                 column=("col1", "col2"))
        listatec1.heading("#0", text="")
        listatec1.column("#0", width=0)
        listatec1.heading("#1", text="cod")
        listatec1.column("#1", width=50)
        listatec1.heading("#2", text="")
        listatec1.column("#2", width=220)
        listatec1.place(x=7, y=10)

        barra12 = Scrollbar(listatec, orient='vertical', command=OnTec)
        barra12.place(x=280, y=22, width=25, height=190)
        listatec1.configure(yscroll=barra12.set)

        # Binding da listbox
        listatec1.bind('<Double-1>', add_autobind)

        tec = self.cursor
        tec.execute(
            """SELECT cod_forn, fornecedor FROM fornecedores 
            WHERE fornecedor LIKE '%s' ORDER BY fornecedor ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            listatec1.insert("", END, values=i)

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)

        self.desconecta_Glac()
    def carrega_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        prod = self.cursor

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)

        prod.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaProd.insert(END, i)

        idmarca = self.cursor
        idmarca.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaIdMarcaprod.insert(END, i)

        mm = self.entradaIdMarcaprod.get()
        marca = self.cursor
        marca.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % mm)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarcaprod.insert(END, i)

        idfornec = self.cursor
        idfornec.execute("SELECT id_fornec FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaIdFornec.insert(END, i)

        ff = self.entradaIdFornec.get()
        fornec = self.cursor
        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFornec.insert(END, i)

        custo = self.cursor
        custo.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacusto = self.cursor.fetchall()
        for i in consultacusto:
            self.entradaCusto.insert(END, i)

        valor = self.cursor
        valor.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalor = self.cursor.fetchall()
        for i in consultavalor:
            self.entradaValor.insert(END, i)

        descrprod = self.cursor
        descrprod.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescrprod = self.cursor.fetchall()
        for i in consultadescrprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

            self.desconecta_Glac()
    def del_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""
     		DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" ORDER BY servprod ASC;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Produto excluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def limpa_produtoP(self):
        self.conecta_Glac()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)

        self.desconecta_Glac()
    def mud_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        tipser = 'Peça'
        hora = '1'

        self.cursor.execute("""
     		UPDATE servprod SET servprod = ?  WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
             		UPDATE servprod SET tiposerv = ? WHERE cod_sp = ?""", (tipser, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
                     		UPDATE servprod SET hor = ? WHERE cod_sp = ?""", (hora, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (id_marcaprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
             UPDATE servprod SET id_fornec = ? WHERE cod_sp = ?""", (id_fornec, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" ORDER BY servprod ASC;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Produto alterado com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def OnDoubleClickP(self, event):
        self.limpa_produtoP()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

        self.carrega_produtoP()

