import pandas as pd
import os

def convert_to_woocommerce():
    try:
        woocommerce_csv = pd.read_csv(os.path.join(os.getcwd(), 'csv', 'produkty.csv'))
        # Zmiana nazw kolumn z otwartego arkusza na domyslne nazwy woocommerce
        woocommerce_csv = woocommerce_csv.rename(columns={"tw_Id": "ID", "tw_Symbol": "SKU", "tw_Nazwa": "Name", "tw_Opis": "Short description", "tc_CenaNetto7": "Regular price"})
        # Dodanie nowych kolumn
        woocommerce_csv.insert(loc=1, column='Type', value="simple")
        woocommerce_csv['Description'] = ''
        woocommerce_csv['Tax status'] = 'taxable'
        woocommerce_csv['Backorders allowed?'] = '0'
        woocommerce_csv['Allow customer reviews?'] = '0'
        woocommerce_csv.to_csv(os.path.join(os.getcwd(), 'csv', 'woocommerce_products.csv'), index=False)
        print(woocommerce_csv)
    except FileNotFoundError as err:
        print('Error!', err)

convert_to_woocommerce()