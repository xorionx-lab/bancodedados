import flet as ft
from models import Cliente
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.page):
    page.title = "Cadastro de clientes"
    
    lista_pessoas = ft.ListView()
    
    def cadastrar(e):
        try:  
            novo_cliente = Cliente(titulo=pessoa.value, valor=valor.value)
            session.add(novo_cliente)
            session.commit()
            lista_pessoas.controls.append(ft.Container(
                    ft.Text(pessoa.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=5,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=8
                ))
            txt_erro.visible = False
            txt_acerto.visible = True
        except:
            txt_erro.visible = True
            txt_acerto.visible = False
            
        page.update()
        print("Produto salvo com sucesso")
    txt_erro = ft.Container(ft.Text("Erro ao salvar o cliente!"), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text("Cliente cadastrado com sucesso"), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center) 
    txt_titulo = ft.Text("Nome da pessoa: ")
    pessoa = ft.TextField(label="Digite o nome do cliente...", text_align=ft.TextAlign.LEFT)
    txt_valor = ft.Text("Valor cobrado: ")
    valor = ft.TextField(value="0", label="Digite o valor", text_align=ft.TextAlign.LEFT)
    btn_pessoa = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    
    page.add(
        txt_acerto,
        txt_erro,
        txt_titulo,
        pessoa,
        txt_valor,
        valor,
        btn_pessoa
    )

    for p in session.query(Cliente).all():
        lista_pessoas.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=5,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=8
            )
        )
        
    page.add(
        lista_pessoas,  
    )

ft.app(target=main)