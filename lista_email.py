import csv
def retorno_email():
    cliente_email = []
    with open('dados.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=["nome", "emailcliente", "data"])
        reader.__next__()
        for row in reader:
            #print(str(row["nome"]) + ', ' + str(row["emailcliente"]) + ', ' + str(row["data"]))
            cliente_email.append(str(row["emailcliente"]))
    return cliente_email
def retorno_nome():
    cliente_nome = []
    with open('dados.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=["nome", "emailcliente", "data"])
        reader.__next__()
        for row in reader:
            #print(str(row["nome"]) + ', ' + str(row["emailcliente"]) + ', ' + str(row["data"]))
            cliente_nome.append(str(row["nome"]))
    return cliente_nome
