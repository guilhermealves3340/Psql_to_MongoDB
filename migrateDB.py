from pymongo import MongoClient
import json


client = MongoClient('mongodb://localhost:27017')

db = client['aulasBD']

col = db['clientes']
docs = [
    {"_id":1,  "titulo":'Sra', "nome":'Jessica',   "sobrenome":'Mendes',    "endereco":'Avenida Acelino de Leao',          "numero":'89',   "complemento":'',                          "cep":'68900 300', "cidade":'Macapá',               "estado":'AP', "fone_fixo":'3565 1243', "fone_movel":'8765 8999' ,  "fg_ativo":1},
    {"_id":2,  "titulo":'Sr',  "nome":'Andrei',    "sobrenome":'Junqueira', "endereco":'Rua Tabaiares',                    "numero":'1024', "complemento":'',                          "cep":'30150 040', "cidade":'Belo Horizonte',       "estado":'BH', "fone_fixo":'3676 1209', "fone_movel":'8876 4543',   "fg_ativo":1},
    {"_id":3,  "titulo":'Sr',  "nome":'Alex',      "sobrenome":'Matheus',   "endereco":'Rua Eva Terpins',                  "numero":'s/n',  "complemento":'',                          "cep":'05327 030', "cidade":'São Paulo',            "estado":'SP', "fone_fixo":'6576 0099', "fone_movel":'9358 7676',   "fg_ativo":1},
    {"_id":4,  "titulo":'Sr',  "nome":'Andre',     "sobrenome":'Lopes',     "endereco":'Rua Fortaleza',                    "numero":'552',  "complemento":'',                          "cep":'11436 360', "cidade":'Guarujá',              "estado":'SP', "fone_fixo":'5654 4343', "fone_movel":'9821 4321',   "fg_ativo":1},
    {"_id":5,  "titulo":'Sr',  "nome":'Vitor',     "sobrenome":'Silva',     "endereco":'Estrada Aguá Chata',               "numero":'s/n',  "complemento":'Rodovia 356',               "cep":'07251 000', "cidade":'Guarulhos',            "estado":'SP', "fone_fixo":'4343 6712', "fone_movel":'831 3411',    "fg_ativo":1},
    {"_id":6,  "titulo":'Sr',  "nome":'Claudinei', "sobrenome":'Safra',     "endereco":'Avenida José Osvaldo Marques',     "numero":'1562', "complemento":'',                          "cep":'14173 010', "cidade":'Sertãozinho',          "estado":'SP', "fone_fixo":'3698 8100', "fone_movel":'8131 6409',   "fg_ativo":1},
    {"_id":7,  "titulo":'Sr',  "nome":'Ricardo',   "sobrenome":'Ferreira',  "endereco":'Alameda Assunta Barizani Tienghi', "numero":'88',   "complemento":'',                          "cep":'18046 705', "cidade":'Sorocaba',             "estado":'SP', "fone_fixo":'6534 7099', "fone_movel":'9988 1251',   "fg_ativo":1},
    {"_id":8,  "titulo":'Sra', "nome":'Anna',      "sobrenome":'Kelly',     "endereco":'Rua das Acacias',                  "numero":'1089', "complemento":'',                          "cep":'13187 042', "cidade":'Hortolândia',          "estado":'SP', "fone_fixo":'6432 440043',"fone_movel":'9465 0023' , "fg_ativo":1},
    {"_id":9,  "titulo":'Sra', "nome":'Cristiane', "sobrenome":'Hickman',   "endereco":'Rua Agenir Martinhon Scachetti',   "numero":'300',  "complemento":'',                          "cep":'13341 633', "cidade":'Indaiatuba',           "estado":'SP', "fone_fixo":'3512 1243',  "fone_movel":'9987 0001' , "fg_ativo":1},
    {"_id":10, "titulo":'Sr',  "nome":'Marcos',    "sobrenome":'Augusto',   "endereco":'Avenida Australia',                "numero":'s/n',  "complemento":'',                          "cep":'06852 100', "cidade":'Itapecerica da Serra', "estado":'SP', "fone_fixo":'3623 8821',  "fone_movel":'8891 2333' , "fg_ativo":1},
    {"_id":11, "titulo":'Sr',  "nome":'David',     "sobrenome":'Silva',     "endereco":'Rua Arcy Prestes Ruggeri',         "numero":'24',   "complemento":'Esquina do Mercado',        "cep":'18201 720', "cidade":'Itapetininga',         "estado":'SP', "fone_fixo":'4565 9240',  "fone_movel":'7765 4029' , "fg_ativo":1},
    {"_id":12, "titulo":'Sr',  "nome":'Ricardo',   "sobrenome":'Cunha',     "endereco":'Rua Jose Fortunato de Godoy',      "numero":'889',  "complemento":'',                          "cep":'13976 121', "cidade":'Itapira',              "estado":'SP', "fone_fixo":'5467 1959',  "fone_movel":'9244 9584' , "fg_ativo":1},
    {"_id":13, "titulo":'Sra', "nome":'Laura',     "sobrenome":'Batista',   "endereco":'Rua Villa Lobos',                  "numero":'76',   "complemento":'',                          "cep":'13976 018', "cidade":'Ribeirão Preto',       "estado":'SP', "fone_fixo":'2111 8710',  "fone_movel":'9991 2324' , "fg_ativo":1},
    {"_id":14, "titulo":'Sr',  "nome":'Valmil',    "sobrenome":'Feliciano', "endereco":'Rua Professor Emilton Amaral',     "numero":'961',  "complemento":'Loteamento Novo Horizonte', "cep":'58053 223', "cidade":'João Pessoa',          "estado":'PB', "fone_fixo":'4431 8740',  "fone_movel":'9766 0033' , "fg_ativo":1},
    {"_id":15, "titulo":'Sr',  "nome":'Agnaldo',   "sobrenome":'Aparecido', "endereco":'Rua Soldado Celio Tonelli',        "numero":'778',  "complemento":'',                          "cep":'09240 320', "cidade":'Santo André',          "estado":'SP', "fone_fixo":'2386 8092',  "fone_movel":'99625 3683' ,"fg_ativo":1}]
col.insert_many(docs)

col = db['item']
docs =[
    {"id_item":1,  "ds_item":'Quebra-cabeça de Madeira',"preco_custo":15.23, "preco_venda":21.95, "fg_ativo":1},
    {"id_item":2,  "ds_item":'Cubo X',                  "preco_custo":7.45,  "preco_venda":11.49, "fg_ativo":1},
    {"id_item":3,  "ds_item":'CD Linux',                "preco_custo":1.99,  "preco_venda":2.49,  "fg_ativo":1},
    {"id_item":4,  "ds_item":'Tecidos',                 "preco_custo":2.11,  "preco_venda":3.99,  "fg_ativo":1},
    {"id_item":5,  "ds_item":'Moldura',                 "preco_custo":7.54,  "preco_venda":9.95,  "fg_ativo":1},
    {"id_item":6,  "ds_item":'Ventilador Pequeno',      "preco_custo":9.23,  "preco_venda":15.75, "fg_ativo":1},
    {"id_item":7,  "ds_item":'Ventilador Grande',       "preco_custo":13.36, "preco_venda":19.95, "fg_ativo":1},
    {"id_item":8,  "ds_item":'Escova de Dentes',        "preco_custo":0.75,  "preco_venda":1.45,  "fg_ativo":1},
    {"id_item":9,  "ds_item":'Papel A4',                "preco_custo":2.34,  "preco_venda":2.45,  "fg_ativo":1},
    {"id_item":10, "ds_item":'Saco de Transporte',      "preco_custo":0.01,  "preco_venda":0.0,   "fg_ativo":1},
    {"id_item":11, "ds_item":'Alto-Falantes',           "preco_custo":19.73, "preco_venda":25.32, "fg_ativo":1}]
col.insert_many(docs)

col = db['pedido']
docs = [
    {"id_pedido":1, "id_cliente":3, "dt_compra":'03-12-2013',"dt_venda":'03-17-2013', "valor":2.99, "fg_ativo":1},
    {"id_pedido":2, "id_cliente":8, "dt_compra":'06-23-2013',"dt_venda":'06-24-2013', "valor":0.00, "fg_ativo":1},
    {"id_pedido":3, "id_cliente":15,"dt_compra":'02-09-2013',"dt_venda":'12-09-2013', "valor":3.99, "fg_ativo":1},
    {"id_pedido":4, "id_cliente":13,"dt_compra":'03-09-2013',"dt_venda":'10-09-2013', "valor":2.99, "fg_ativo":1},
    {"id_pedido":5, "id_cliente":8, "dt_compra":'07-21-2013',"dt_venda":'07-21-2013', "valor":0.00, "fg_ativo":1}]
col.insert_many(docs)

col = db['item_pedido']
docs = [
    {"id_pedido":1, "id_item":4, "quantidade":1},
    {"id_pedido":1, "id_item":7, "quantidade":1},
    {"id_pedido":1, "id_item":9, "quantidade":1},
    {"id_pedido":2, "id_item":1, "quantidade":1},
    {"id_pedido":2, "id_item":10,"quantidade":1},
    {"id_pedido":2, "id_item":7, "quantidade":2},
    {"id_pedido":2, "id_item":4, "quantidade":2},
    {"id_pedido":3, "id_item":2, "quantidade":1},
    {"id_pedido":3, "id_item":1, "quantidade":1},
    {"id_pedido":4, "id_item":5, "quantidade":2},
    {"id_pedido":5, "id_item":1, "quantidade":1},
    {"id_pedido":5, "id_item":3, "quantidade":1}]
col.insert_many(docs)

docs = [
    {"codigo_barras":624152783, "id_item":1 },
    {"codigo_barras":624157463, "id_item":2 },
    {"codigo_barras":626453783, "id_item":3 },
    {"codigo_barras":624152774, "id_item":3 },
    {"codigo_barras":746574384, "id_item":4 },
    {"codigo_barras":345345867, "id_item":5 },
    {"codigo_barras":643456456, "id_item":6 },
    {"codigo_barras":847673683, "id_item":7 },
    {"codigo_barras":624123458, "id_item":8 },
    {"codigo_barras":947362553, "id_item":8 },
    {"codigo_barras":947362746, "id_item":8 },
    {"codigo_barras":458726364, "id_item":9 },
    {"codigo_barras":987987983, "id_item":11},
    {"codigo_barras":223987237, "id_item":11}]
col.insert_many(docs)

docs = [
    {"id_tem":1, "quantidade":12},
    {"id_tem":2, "quantidade":2 },
    {"id_tem":4, "quantidade":8 },
    {"id_tem":5, "quantidade":3 },
    {"id_tem":7, "quantidade":8 },
    {"id_tem":8, "quantidade":18},
    {"id_tem":10,"quantidade":1 }]
col.insert_many(docs)

