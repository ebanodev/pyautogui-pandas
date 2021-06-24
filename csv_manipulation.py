import pandas as pd
from IPython.display import display

tabela = pd.read_excel(r"/home/ebano/Downloads/Vendas - Dez.xlsx")

somavf = tabela["Valor Final"].sum()
print('a soma da coluna Valor FInal é: ', somavf)
somaqt = tabela["Quantidade"].sum()
print('a soma da quantidade de vendas é: ', somaqt)