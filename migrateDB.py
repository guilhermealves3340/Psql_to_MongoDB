from pymongo import MongoClient
import json


client = MongoClient('mongodb://localhost:27017')

db = client['aulasBD']

mydict = '{"_id":"","titulo":"","nome":"","sobrenome":"","endereco":"","numero":"","complemento":"","estado":"","fone_fixo":"","fone_movel":"","fg_ativo":""}'

col = db['clientes']

values = [
    (1, 'Sra', 'Jessica', 'Mendes', 'Avenida Acelino de Leao', '89', '', '68900 300', 'Macapá', 'AP', '3565 1243', '8765 8999' ,1),
    (2, 'Sr', 'Andrei', 'Junqueira', 'Rua Tabaiares', '1024', '', '30150 040', 'Belo Horizonte', 'BH', '3676 1209', '8876 4543', 1),
    (3, 'Sr', 'Alex', 'Matheus', 'Rua Eva Terpins', 's/n', '', '05327 030', 'São Paulo', 'SP', '6576 0099', '9358 7676', 1),
    (4, 'Sr', 'Andre', 'Lopes', 'Rua Fortaleza', '552', '', '11436 360', 'Guarujá', 'SP', '5654 4343', '9821 4321', 1),
    (5, 'Sr', 'Vitor', 'Silva', 'Estrada Aguá Chata', 's/n', 'Rodovia 356', '07251 000', 'Guarulhos', 'SP', '4343 6712', '831 3411', 1),
    (6, 'Sr', 'Claudinei', 'Safra', 'Avenida José Osvaldo Marques', '1562', '', '14173 010', 'Sertãozinho', 'SP', '3698 8100', '8131 6409', 1),
    (7, 'Sr', 'Ricardo', 'Ferreira', 'Alameda Assunta Barizani Tienghi', '88', '', '18046 705', 'Sorocaba', 'SP', '6534 7099', '9988 1251', 1),
    (8, 'Sra', 'Anna', 'Kelly', 'Rua das Acacias', '1089', '', '13187 042', 'Hortolândia', 'SP', '6432 440043', '9465 0023' ,1),
    (9, 'Sra', 'Cristiane', 'Hickman', 'Rua Agenir Martinhon Scachetti', '300', '', '13341 633', 'Indaiatuba', 'SP', '3512 1243', '9987 0001' ,1),
    (10, 'Sr', 'Marcos', 'Augusto', 'Avenida Australia', 's/n', '', '06852 100', 'Itapecerica da Serra', 'SP', '3623 8821', '8891 2333' ,1),
    (11, 'Sr', 'David', 'Silva', 'Rua Arcy Prestes Ruggeri', '24', 'Esquina do Mercado', '18201 720', 'Itapetininga', 'SP', '4565 9240', '7765 4029' ,1),
    (12, 'Sr', 'Ricardo', 'Cunha', 'Rua Jose Fortunato de Godoy', '889', '', '13976 121', 'Itapira', 'SP', '5467 1959', '9244 9584' ,1),
    (13, 'Sra', 'Laura', 'Batista', 'Rua Villa Lobos', '76', '', '13976 018', 'Ribeirão Preto', 'SP', '2111 8710', '9991 2324' ,1),
    (14, 'Sr', 'Valmil', 'Feliciano', 'Rua Professor Emilton Amaral', '961', 'Loteamento Novo Horizonte', '58053 223', 'João Pessoa', 'PB', '4431 8740', '9766 0033' ,1),
    (15, 'Sr', 'Agnaldo', 'Aparecido', 'Rua Soldado Celio Tonelli', '778', '', '09240 320', 'Santo André', 'SP', '2386 8092', '99625 3683' ,1)]

keys = '"_id" "titulo" "nome" sobrenome" endereco" numero" complemento" estado" "fone_fixo" fone_movel" fg_ativo"'.split()

saida = []
for i in range(len(values)):

    y = json.loads(mydict)

    c = 0
    for j in keys:
        y[j] = values[i][c]
        c += 1
    
    saida.append(y)


x = col.insert_many(saida)

print(x.inserted_ids)

col = db['codigo_barras']

keys = 'id_item ds_item preco_custo preco_venda fg_ativo'.split()

values = [
    (1, 'Quebra-cabeça de Madeira', 15.23, 21.95, 1),
    (2, 'Cubo X', 7.45, 11.49, 1),
    (3, 'CD Linux', 1.99, 2.49, 1),
    (4, 'Tecidos', 2.11, 3.99, 1),
    (5, 'Moldura', 7.54, 9.95, 1),
    (6, 'Ventilador Pequeno', 9.23, 15.75, 1),
    (7, 'Ventilador Grande', 13.36, 19.95, 1),
    (8, 'Escova de Dentes', 0.75, 1.45, 1),
    (9, 'Papel A4', 2.34, 2.45, 1),
    (10, 'Saco de Transporte', 0.01, 0.0, 1),
    (11, 'Alto-Falantes', 19.73, 25.32, 1)]

saida = []
for i in range(len(values)):

    y = json.loads(mydict)

    c = 0
    for j in keys:
        y[j] = values[i][c]
        c += 1
    
    saida.append(y)

x = col.insert_many(saida)
