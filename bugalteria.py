# В этом файле собраны функции для работников бугалтерии
import database

def register_client():
    # Получение информации
    polis = input("Укажите полис: ")
    document = input("Укажите номер договора: ")
    ensurance_cases = input("Укажите страховые случаи, разделяя их знаком '|': ")
    timeframe = input("Укажите временной промежуток от начало до окончания работы договора: ")
    notes = input("Укажите примечание (если есть): ")

    # Добавление записей (клиент, договор, заморозка)
    client_database = database.read(database.CLIENTS)
    client_database[polis] = document
    database.write(database.CLIENTS, client_database)

    contracts_database = database.read(database.CONTRACTS)
    contracts_database[document] = {
        "ensurance_cases": ensurance_cases,
        "timeframe": timeframe,
        "notes": notes,
        "polis": polis
    }
    database.write(database.CONTRACTS, contracts_database)

    frozen_database = database.read(database.FROZEN)
    frozen_database[document] = "+"
    database.write(database.FROZEN, frozen_database)
    print("Операция завершена")

def delete_client_by_document():
    document = input("Укажите номер договора: ")

    contracts_database = database.read(database.CONTRACTS)
    polis = contracts_database[document]["polis"]
    del contracts_database[document]
    database.write(database.CONTRACTS, contracts_database)

    frozen_database = database.read(database.FROZEN)
    if frozen_database.get(document, None) is not None:
        del frozen_database[document]
    database.write(database.FROZEN, frozen_database)

    active_database = database.read(database.ACTIVE)
    if active_database.get(document, None) is not None:
        del active_database[document]
    database.write(database.FROZEN, active_database)

    clients_database = database.read(database.CLIENTS)
    del clients_database[polis]
    database.write(database.CLIENTS, clients_database)
    print("Операция завершена")

def freeze_document():
    document = input("Укажите номер договора: ")
    frozen_database = database.read(database.FROZEN)
    frozen_database[document] = "+"
    database.write(database.FROZEN, frozen_database)
    print("Операция завершена")

def unfreeze_document():
    document = input("Укажите номер договора: ")
    frozen_database = database.read(database.FROZEN)
    del frozen_database[document]
    database.write(database.FROZEN, frozen_database)
    print("Операция завершена")

def activate_document():
    document = input("Укажите номер договора: ")
    ecase = input("Укажите страховой случай: ")

    contracts_database = database.read(database.CONTRACTS)
    polis = contracts_database[document]["polis"]

    active_database = database.read(database.ACTIVE)
    active_database[document] = {
        "polis": polis,
        "ensurance_case": ecase
    }
    database.write(database.ACTIVE, active_database)
    print("Операция завершена")

def deactivate_document():
    document = input("Укажите номер договора: ")
    active_database = database.read(database.ACTIVE)
    del active_database[document]
    database.write(database.ACTIVE, active_database)
    print("Операция завершена")

def add_partner():
    inn = input("Укажите ИНН организации: ")
    name = input("Укажите название организации: ")
    sevices = input("Укажите перечень услуг через '|': ")

    partners_database = database.read(database.PARTNERS)
    partners_database[inn] = {
        "name": name,
        "services": sevices
    }
    database.write(database.PARTNERS, partners_database)
    print("Операция завершена")

def delete_partner():
    inn = input("Укажите ИНН организации: ")
    partners_database = database.read(database.PARTNERS)
    del partners_database[inn]
    database.write(database.PARTNERS, partners_database)
    print("Операция завершена")