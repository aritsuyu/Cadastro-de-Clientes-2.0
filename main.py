#Imports
import customtkinter as ctk
import sqlite3
import os
import json

#System
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

##DEFS
#Banco de dados
def criar_banco():
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            cpf TEXT,
            sexo TEXT,
            data_nascimento TEXT,
            endereco TEXT,
            cidade TEXT,
            estado TEXT,
            cep TEXT,
            observacoes TEXT
        )
    ''')
    conn.commit()
    conn.close()
#Armazenamento
def mudar_armazenamento(armazenamento):
    if armazenamento == "SQL":
        print("Modo de armazenamento SQL selecionado")
        pass  # Implementar lógica para SQLite
    elif armazenamento == "JSON":
        print("Modo de armazenamento JSON selecionado")
        pass  # Implementar lógica para JSON
    elif armazenamento == "TXT":
        print("Modo de armazenamento TXT selecionado")
        pass  # Implementar lógica para TXT

#DEFs Salvar Cliente
def salvar_cliente():
    if mudar_armazenamento == "SQL":
        conn = sqlite3.connect("clientes.db")
        c = conn.cursor()
        c.execute('''
            INSERT INTO clientes (nome, email, telefone, cpf, sexo, data_nascimento, endereco, cidade, estado, cep, observacoes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            entry_nome.get(),
            entry_email.get(),
            entry_telefone.get(),
            entry_cpf.get(),
            sexo_var.get(),
            entry_data_nascimento.get(),
            entry_endereco.get(),
            entry_cidade.get(),
            entry_estado.get(),
            entry_cep.get(),
            entry_observacoes.get()
    ))
        conn.commit()
        conn.close()
        limpar_campos()
    if mudar_armazenamento == "JSON":
        dados_cliente = {
            "nome": entry_nome.get(),
            "email": entry_email.get(),
            "telefone": entry_telefone.get(),
            "cpf": entry_cpf.get(),
            "sexo": sexo_var.get(),
            "data_nascimento": entry_data_nascimento.get(),
            "endereco": entry_endereco.get(),
            "cidade": entry_cidade.get(),
            "estado": entry_estado.get(),
            "cep": entry_cep.get(),
            "observacoes": entry_observacoes.get()
        }
        with open("clientes.json", "a") as arquivo_json:
            json.dump(dados_cliente, arquivo_json)
        limpar_campos()
    if mudar_armazenamento == "TXT":
        dados_cliente = {
            "nome": entry_nome.get(),
            "email": entry_email.get(),
            "telefone": entry_telefone.get(),
            "cpf": entry_cpf.get(),
            "sexo": sexo_var.get(),
            "data_nascimento": entry_data_nascimento.get(),
            "endereco": entry_endereco.get(),
            "cidade": entry_cidade.get(),
            "estado": entry_estado.get(),
            "cep": entry_cep.get(),
            "observacoes": entry_observacoes.get()
        }
        with open("clientes.txt", "a") as arquivo_txt:
            arquivo_txt.write(str(dados_cliente) + "\n")
        limpar_campos()

def limpar_campos():
    for entry in entradas:
        entry.delete(0, ctk.END)

#Body
body = ctk.CTk()
body.geometry("600x600")
body.title("Cadastro de Clientes")

tabview = ctk.CTkTabview(body)
tabview.pack(expand=True, fill="both", padx=20, pady=20)

aba_cadastro = tabview.add("Cadastro")
aba_config = tabview.add("Configurações")

frame = ctk.CTkFrame(aba_cadastro)
frame.pack(padx=20, pady=20, fill="both", expand=True)

#Entrys
entradas = []

def criar_campo(label_text, row):
    label = ctk.CTkLabel(frame, text=label_text + ":")
    label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
    entry = ctk.CTkEntry(frame, width=250)
    entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
    entradas.append(entry)
    return entry

entry_nome = criar_campo("Nome", 0)
entry_email = criar_campo("Email", 1)
entry_telefone = criar_campo("Telefone", 2)
entry_cpf = criar_campo("CPF", 3)

ctk.CTkLabel(frame, text="Sexo:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
sexo_var = ctk.StringVar(value="Masculino")
ctk.CTkRadioButton(frame, text="Masculino", variable=sexo_var, value="Masculino").grid(row=4, column=1, sticky="w")
ctk.CTkRadioButton(frame, text="Feminino", variable=sexo_var, value="Feminino").grid(row=4, column=1, sticky="e")

entry_data_nascimento = criar_campo("Data de Nascimento", 5)
entry_endereco = criar_campo("Endereço", 6)
entry_cidade = criar_campo("Cidade", 7)
entry_estado = criar_campo("Estado", 8)
entry_cep = criar_campo("CEP", 9)
entry_observacoes = criar_campo("Observações", 10)

#Botões
botoes_frame = ctk.CTkFrame(frame)
botoes_frame.grid(row=11, column=0, columnspan=2, pady=20)

ctk.CTkButton(botoes_frame, text="Salvar", command=salvar_cliente).grid(row=0, column=0, padx=10)
ctk.CTkButton(botoes_frame, text="Limpar", command=limpar_campos).grid(row=0, column=1, padx=10)
ctk.CTkButton(botoes_frame, text="Sair", command=body.quit).grid(row=0, column=2, padx=10)

#Config
def mudar_tema(tema):
    ctk.set_appearance_mode(tema)

def mudar_escala(escala):
    ctk.set_widget_scaling(float(escala))

ctk.CTkLabel(aba_config, text="Tema:").pack(pady=10)
tema_combo = ctk.CTkOptionMenu(aba_config, values=["System", "Light", "Dark"], command=mudar_tema)
tema_combo.set("System")
tema_combo.pack()

ctk.CTkLabel(aba_config, text="Tamanho da Interface:").pack(pady=10)
escala_combo = ctk.CTkOptionMenu(aba_config, values=["0.8", "0.9", "1.0", "1.1", "1.2"], command=mudar_escala)
escala_combo.set("1.0")
escala_combo.pack()

#Armazenamento
ctk.CTkLabel(aba_config, text="Modo de Armazenamento:").pack(pady=10)
armazenamento_combo = ctk.CTkOptionMenu(aba_config, values=["SQL", "JSON", "TXT"], command=mudar_armazenamento)
armazenamento_combo.set("SQL")
armazenamento_combo.pack()

ctk.CTkLabel(aba_config, text="Versão: 2.5").pack(pady=10)

criar_banco()
body.mainloop()
print("SOFTWARE Fechado")