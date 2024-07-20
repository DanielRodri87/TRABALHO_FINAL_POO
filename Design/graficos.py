import PySimpleGUI as sg
from Scripts.new_chart import NewChart

# Layout
class Graficos:
    def menu_graficos():
        sg.theme('Default1')
        layout = [
            [sg.Frame("Opções de gráficos", 
                [
                    [
                        sg.Button(image_filename="Design/Images/tipo_de_bolo.png", button_color=("#E8E5EA", "#E8E5EA"), key="-TIPO_BOLO-",image_size=(150, 100), pad=(5, 5)),
                        sg.Button(image_filename="Design/Images/status_dos_pedidos.png", button_color=("#E8E5EA", "#E8E5EA"), key="-STATUS_PEDIDO-",image_size=(150, 100), pad=(5, 5))
                    ],
                    [
                        sg.Button(image_filename="Design/Images/pedidos_mensais.png", button_color=("#E8E5EA", "#E8E5EA"), key="-MENSAIS-",image_size=(150, 100), pad=(5, 5)),
                        sg.Button(image_filename="Design/Images/tipo_de_salgado.png", button_color=("#E8E5EA", "#E8E5EA"), key="-TIPO_SALGADO-",image_size=(150, 100), pad=(5, 5))
                    ],
                    [
                        sg.Button(image_filename="Design/Images/lucro_mensal.png", button_color=("#E8E5EA", "#E8E5EA"), key="-LUCRO_MENSAL-",image_size=(150, 100), pad=(5, 5)),
                        sg.Button(image_filename="Design/Images/lucro_por_tipo_de_festa.png", button_color=("#E8E5EA", "#E8E5EA"), key='-LUCRO_POR_TIPO_DE_FESTAS-',image_size=(150, 100), pad=(5, 5))
                    ],
                    [sg.Button("Voltar", size=(100, 2), button_color=("White", "#FF8C01"), key="-VOLTAR-")]
                ]
            )],
        ]
        return sg.Window("Gráficos", layout=layout, finalize=True, size=(370, 420))

