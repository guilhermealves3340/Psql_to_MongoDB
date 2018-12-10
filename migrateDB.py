from pymongo import MongoClient
import json


client = MongoClient('mongodb://localhost:27017')

db = client['aulasBD']

col = db['clientes']

docs = [
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
    {'_id': 'sobrenome': 'endereco': 'numero': 'complemento': 'estado': 'fone_fixo': 'fone_movel': 'fg_ativo':}
]

id = ''
sobrenome = ''
endereco = ''
numero = ''
complemento = ''
estado = ''
fone_fixo = ''
fone_movel = ''
fg_ativo = ''

keys = '{"_id":"{}","sobrenome":"{}","endereco":"{}","numero":"{}","complemento":"{}","estado":"{}","fone_fixo":"{}","fone_movel":"{}","fg_ativo":"{}"}'.format(id,sobrenome,endereco,numero,complemento,estado,fone_fixo, fone_movel,fg_ativo)


values = [
    ('1', 'Sra', 'Jessica', 'Mendes', 'Avenida Acelino de Leao', '89', '', '68900 300', 'Macapá', 'AP', '3565 1243', '8765 8999' ,'1'),
    ('2', 'Sr', 'Andrei', 'Junqueira', 'Rua Tabaiares', '1024', '', '30150 040', 'Belo Horizonte', 'BH', '3676 1209', '8876 4543', '1'),
    ('3', 'Sr', 'Alex', 'Matheus', 'Rua Eva Terpins', 's/n', '', '05327 030', 'São Paulo', 'SP', '6576 0099', '9358 7676', '1'),
    ('4', 'Sr', 'Andre', 'Lopes', 'Rua Fortaleza', '552', '', '11436 360', 'Guarujá', 'SP', '5654 4343', '9821 4321', '1'),
    ('5', 'Sr', 'Vitor', 'Silva', 'Estrada Aguá Chata', 's/n', 'Rodovia 356', '07251 000', 'Guarulhos', 'SP', '4343 6712', '831 3411', '1'),
    ('6', 'Sr', 'Claudinei', 'Safra', 'Avenida José Osvaldo Marques', '1562', '', '14173 010', 'Sertãozinho', 'SP', '3698 8100', '8131 6409', '1'),
    ('7', 'Sr', 'Ricardo', 'Ferreira', 'Alameda Assunta Barizani Tienghi', '88', '', '18046 705', 'Sorocaba', 'SP', '6534 7099', '9988 1251', '1'),
    ('8', 'Sra', 'Anna', 'Kelly', 'Rua das Acacias', '1089', '', '13187 042', 'Hortolândia', 'SP', '6432 440043', '9465 0023' ,'1'),
    ('9', 'Sra', 'Cristiane', 'Hickman', 'Rua Agenir Martinhon Scachetti', '300', '', '13341 633', 'Indaiatuba', 'SP', '3512 1243', '9987 0001' ,1),
    ('10', 'Sr', 'Marcos', 'Augusto', 'Avenida Australia', 's/n', '', '06852 100', 'Itapecerica da Serra', 'SP', '3623 8821', '8891 2333' ,1),
    ('11', 'Sr', 'David', 'Silva', 'Rua Arcy Prestes Ruggeri', '24', 'Esquina do Mercado', '18201 720', 'Itapetininga', 'SP', '4565 9240', '7765 4029' ,1),
    ('12', 'Sr', 'Ricardo', 'Cunha', 'Rua Jose Fortunato de Godoy', '889', '', '13976 121', 'Itapira', 'SP', '5467 1959', '9244 9584' ,1),
    ('13', 'Sra', 'Laura', 'Batista', 'Rua Villa Lobos', '76', '', '13976 018', 'Ribeirão Preto', 'SP', '2111 8710', '9991 2324' ,1),
    ('14', 'Sr', 'Valmil', 'Feliciano', 'Rua Professor Emilton Amaral', '961', 'Loteamento Novo Horizonte', '58053 223', 'João Pessoa', 'PB', '4431 8740', '9766 0033' ,1),
    ('15', 'Sr', 'Agnaldo', 'Aparecido', 'Rua Soldado Celio Tonelli', '778', '', '09240 320', 'Santo André', 'SP', '2386 8092', '99625 3683' ,1)]