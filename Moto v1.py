import requests as req
import time
import csv

def primeiralinha(link_save_txt):
    texto_write = str(
        '\"' + 'id' + "\";\"" + 'ano_modelo' + "\";\"" + 'marca' + "\";\"" + 'name' + "\";\"" + 'veiculo' + "\";\"" + 'preco' + "\";\"" + 'combustivel' + "\";\"" + 'referencia' + "\";\"" + 'fipe_codigo' + "\";\"" + 'key' + '\"')
    # if str(dict_info['name']) == str(r'A1 Sportback 1.4 TFSI 5p S-tronic'):
    #    y = 0
    try:
        with open(link_save_txt, 'a') as txtfile:
            txtfile.write(texto_write + "\n")
            txtfile.close()
    except:
        pass

i = 0
link_save_txt = str(r'Moto.txt')
url = req.get('http://fipeapi.appspot.com/api/1/motos/marcas.json')
dict_marcas = url.json()
print(type(dict_marcas))
for marca in dict_marcas:
    if i >= 0:
        time.sleep(5)
        print(marca['fipe_name'], marca['id'])
        id = marca['id']
        url = req.get('http://fipeapi.appspot.com/api/1/motos/veiculos/' + str(id) + '.json')
        dict_veiculo = url.json()
        j = 0
        for veiculo in dict_veiculo:
            if j > 0:
                print(marca['name'], veiculo['name'], veiculo['id'])
                id2 = veiculo['id']
                time.sleep(4)
                url = req.get('http://fipeapi.appspot.com/api/1/motos/veiculo/' + str(id) + '/' + str(id2) + '.json')
                dict_modelo = url.json()
                for modelo in dict_modelo:
                    id3 = modelo['key']
                    try:
                        time.sleep(4)
                        url = req.get(
                            'http://fipeapi.appspot.com/api/1/motos/veiculo/' + str(id) + '/' + str(id2) + '/' + str(
                                id3) + '.json')
                        dict_info = url.json()
                        if i == 0:
                            primeiralinha(link_save_txt)
                        i += 1
                        texto_write = str(
                            '\"' + str(dict_info['id']) + "\";\"" + str(dict_info['ano_modelo']) + "\";\"" + str(
                                dict_info['marca']) + "\";\"" + str(dict_info['name'])
                            + "\";\"" + str(dict_info['veiculo']) + "\";\"" + str(dict_info['preco']) + "\";\"" + str(
                                dict_info['combustivel']) + "\";\""
                            + str(dict_info['referencia']) + "\";\"" + str(dict_info['fipe_codigo']) + "\";\"" + str(
                                dict_info['key']) + '\"')
                        # if str(dict_info['name']) == str(r'A1 Sportback 1.4 TFSI 5p S-tronic'):
                        #    y = 0
                        try:
                            with open(link_save_txt, 'a') as txtfile:
                                txtfile.write(texto_write + "\n")
                                txtfile.close()
                        except:
                            continue
                        # csvfile =r'C:\Users\felipe.antoneli\Desktop\Estudo\Estudo\arquivo.csv'
                        # c = csv.writer(open(csvfile, "a",encoding='utf-8'))
                        # c.writerow([dict_info['id'],dict_info['ano_modelo'],dict_info['marca'],dict_info['name'],dict_info['veiculo'],dict_info['preco'],dict_info['combustivel'],dict_info['referencia'],dict_info['fipe_codigo'],dict_info['key']])
                        print(dict_info['id'], dict_info['ano_modelo'], dict_info['marca'], dict_info['name'],
                              dict_info['veiculo'], dict_info['preco'], dict_info['combustivel'],
                              dict_info['referencia'],
                              dict_info['fipe_codigo'], dict_info['key'])
                    except:
                        continue
            j += 1
    i += 1