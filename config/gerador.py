import os


class Repositorio:
    def __init__(self, file):
        self.file = file
        self.dict_users = None
        self.pre_percentual = None
        self.new = None
        self.list_users = None
        self.espaco_total = None
        self.media = None
        self.linhas = None

    def open_file(self):
        file_user = open(self.file)
        self.linhas = file_user.readlines()
        self.list_users = []
        i = 0
        while i <= len(self.linhas):
            for linha in self.linhas:
                linha_numero = linha.split('  ')
                self.list_users.append(linha_numero)

                while len(self.list_users[i]) > 2:
                    if len(self.list_users[i]) > 2:
                        self.list_users[i].remove('')

                self.list_users[i][1] = self.list_users[i][1][0:]
                self.list_users[i][1] = self.list_users[i][1][:-1]
                i += 1

        self.dict_users = dict(self.list_users)
        self.pre_percentual = dict(self.list_users)
        total = 0
        v = 0
        for chave, valor in self.dict_users.items():
            valor_int = int(valor)
            total += valor_int
            self.dict_users[chave] = valor_int
            v += 1
        for chave, valor in self.pre_percentual.items():
            valor_int = int(valor)
            total += valor_int
            self.pre_percentual[chave] = valor_int
            v += 1

        self.espaco_total = round(total / (1024 ** 2), 2)
        self.media = round(self.espaco_total / len(self.linhas), 2)

        return self.dict_users

    def b_to_mb(self):
        for chave, valor in self.dict_users.items():
            megabyte = valor / (1024 ** 2)
            novo_valor = str(round(megabyte, 2)) + ' MB'
            self.dict_users[chave] = novo_valor

        for chave1, valor1 in self.pre_percentual.items():
            megabyte = valor1 / (1024 ** 2)
            novo_valor = round(megabyte, 2)
            self.pre_percentual[chave1] = novo_valor

        return self.dict_users

    def repositorio_file(self):
        diretorio = r'C:\Users\Gabriel\Desktop\relatorio.txt'
        with open(diretorio, 'w') as novo_arquivo:
            novo_arquivo.write('ACME Inc.              Uso do espaço em disco pelos usuários \n')
            novo_arquivo.write('-'*90 + '\n')
            novo_arquivo.write('Nr  |  Usuário     |   Espaço utilizado  |     % do uso\n')
            nr = 1
            percentual = round(self.espaco_total / 100, 2)
            for key, val in self.pre_percentual.items():
                val_porcentagem = val / percentual
                self.pre_percentual[key] = str(round(val_porcentagem, 2)) + '%'

            for chave, valor in self.dict_users.items():
                for keys, vals in self.pre_percentual.items():
                    if chave == keys:
                        novo_arquivo.write(f'{nr:<5} {chave:<20} {valor:<20} {vals}\n')
                        nr += 1
            novo_arquivo.write(f'\n')
            novo_arquivo.write(f'Espaço total ocupado: {self.espaco_total} MB\n')
            novo_arquivo.write(f'Espaço médio ocupado: {self.media} MB\n')














