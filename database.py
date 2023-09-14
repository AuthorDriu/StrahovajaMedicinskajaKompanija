import json
import os
from os import path

DATABASE_ROOT = "database"

CLIENTS = "clients"
PARTNERS = "partners"
CONTRACTS = "contracts",
ACTIVE = "active",
FROZEN = "frozen"

paths = {
    CLIENTS: "database/clients.json",
    PARTNERS: "database/partners.json",
    CONTRACTS: "database/contracts.json",
    ACTIVE: "database/active.json",
    FROZEN: "database/frozen.json"
}

def create_database_if_not_exists():
    if not path.exists(DATABASE_ROOT):
        os.mkdir(DATABASE_ROOT)
        print("Создана директория базы данных")
    for table in paths.keys():
        if not path.exists(paths[table]):
            with open(paths[table], "w") as file:
                file.write("{}")
                #print("Создан файл {}.json".format(table))

def read(table):
    path_to = paths.get(table, None)
    if path_to is None:
        print("Нет такого файла {}".format(table))
        return
    content = {}
    with open(path_to, "r") as file:
        content = json.loads(file.read())
    return content

def write(table, new):
    path_to = paths.get(table, None)
    if path_to is None:
        print("Нет такого файла {}".format(table))
        return
    with open(path_to, "w") as file:
        file.write(json.dumps(new))

create_database_if_not_exists()