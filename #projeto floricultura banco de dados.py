#projeto floricultura banco de dados
# -*- coding: utf-8 -*-
#Para esse projeto de banco de dados, preciso criar um programa 
# que armazene dados de floricultura e coloque os dados, vendas, cliente, rg, produtos e estoque em um banco de dados.
# O banco de dados deve ser capaz de armazenar informações sobre os produtos,
# incluindo nome, preço, quantidade em estoque e descrição.
# Além disso, o banco de dados deve permitir a adição, remoção e atualização de produtos.
# O banco de dados também deve permitir a consulta de produtos por nome ou categoria.   


#preciso criar uma tabela para armazenar os clientes, com informações como nome, endereço, telefone e e-mail e rg.
#preciso criar uma outra tabela para armazer os produtos, com informações como nome, preço, quantidade em estoque e id_produto, 
#preciso criar uma tabela para armazenar as vendas, com informações como data da venda, valor total e produtos vendidos, nota fiscal, id_compra_ Id cliente
#preciso fazer com que essas tabelas se relacionem entre si,
#preciso criar um menu para o usuário interagir com o banco de dados,


from sqlite3 import connect, Error
from tabulate import tabulate 
conn = sqlite3.connect('floricultura.db')
c = conn.cursor() 

def create_table():
    # Cria a tabela de clientes
    c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    endereco TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    rg TEXT NOT NULL)''')
    
    # Cria a tabela de produtos
    c.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL,
                    descricao TEXT)''')
    
    # Cria a tabela de vendas
    c.execute('''CREATE TABLE IF NOT EXISTS vendas (
                    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_venda TEXT NOT NULL,
                    valor_total REAL NOT NULL,
                    id_cliente INTEGER NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente))''')
    
    conn.commit()
    print("Tabelas criadas com sucesso!")
    conn.close()