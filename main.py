from CommandLine import CommandLine
import bugalteria, read_database


command_line = CommandLine()

command_line.add_user("Бугалтерия", "Бугалтерия")
command_line.get_user("Бугалтерия").add("регистрация пользователя", bugalteria.register_client, "Зарегистрировать нового пользователя")
command_line.get_user("Бугалтерия").add("удалить пользователя", bugalteria.delete_client_by_document, "Удалить пользователя")
command_line.get_user("Бугалтерия").add("заморозить", bugalteria.freeze_document, "Заморозить документ")
command_line.get_user("Бугалтерия").add("разморозить", bugalteria.unfreeze_document, "Разморозить документ")
command_line.get_user("Бугалтерия").add("активировать", bugalteria.activate_document, "Активировать документ")
command_line.get_user("Бугалтерия").add("деактивировать", bugalteria.deactivate_document, "Деактивировать документ")
command_line.get_user("Бугалтерия").add("добавить партнёра", bugalteria.add_partner, "Добавить партнёрскую организацию")
command_line.get_user("Бугалтерия").add("удалить партнёра", bugalteria.delete_partner, "Удалить партнёрскую организацию")
command_line.get_user("Бугалтерия").add("список", read_database.get_list, "Посмотреть список записей в таблице")
command_line.get_user("Бугалтерия").add("инфо пользователь", read_database.client, "Посмотреть информацию о пользователе")
command_line.get_user("Бугалтерия").add("инфо партнёр", read_database.partner, "Посмотреть информацию о партнёре")
command_line.get_user("Бугалтерия").add("инфо договор", read_database.contract, "Посмотреть информацию о договоре")
command_line.get_user("Бугалтерия").add("активен ли", read_database.active, "Узнать активен ли договор")
command_line.get_user("Бугалтерия").add("заморожен ли", read_database.frozen, "Узнать заморожен ли договор")

command_line.add_user("Инспектор", "Инспектор")
command_line.get_user("Инспектор").add("инфо пользователь", read_database.client, "Посмотреть информацию о пользователе")
command_line.get_user("Инспектор").add("инфо партнёр", read_database.partner, "Посмотреть информацию о партнёре")
command_line.get_user("Инспектор").add("инфо договор", read_database.contract, "Посмотреть информацию о договоре")

command_line.run()