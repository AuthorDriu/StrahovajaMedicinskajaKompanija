import database

def get_list():
    tablename = input("Укажите таблицу [клиенты | партнёры | контракты | активные договоры | замороженные договоры]: ")
    arg = {
        "клиенты": database.CLIENTS,
        "партнёры": database.PARTNERS,
        "контракты": database.CONTRACTS,
        "активные договоры": database.ACTIVE,
        "замороженные договоры": database.FROZEN
    }.get(tablename, None)
    if arg is None:
        print("Нет такой таблицы")
        return
    some_database = database.read(arg)
    print(f"Вывод: {[x for x in some_database.keys()]}")

def client():
    polis = input("Укажите полис: ")
    clients_database = database.read(database.CLIENTS)
    client = clients_database.get(polis, None)
    if client is None:
        print("Нет такого клиента")
        return
    print(f"Полис: {polis}\nНомер договора: {client}")

def partner():
    inn = input("Укажите ИНН: ")
    partners_database = database.read(database.PARTNERS)
    partner = partners_database.get(inn, None)
    if partner is None:
        print("Нет такой организации")
        return
    print(f"ИНН: {inn}\nНазвание: {partner['name']}\nУслуги {partner['services']}")

def contract():
    document = input("Укажите номер договора: ")
    contracts_database = database.read(database.CONTRACTS)
    contract = contracts_database.get(document, None)
    if contract is None:
        print("Нет такого договора")
        return
    print(f"Номер договора: {document}\nСтраховые случаи: {contract['ensurance_cases']}\nСроки: {contract['timeframe']}\nПримечания: {contract['notes']}\nПолис: {contract['polis']}")

def active():
    document = input("Укажите номер договора: ")
    active_database = database.read(database.ACTIVE)
    if active_database.get(document, None) is None: print("-")
    else: print("+")

def frozen():
    document = input("Укажите номер договора: ")
    frozen_database = database.read(database.FROZEN)
    if frozen_database.get(document, None) is None: print("-")
    else: print("+")