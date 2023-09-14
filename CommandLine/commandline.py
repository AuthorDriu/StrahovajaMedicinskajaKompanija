class Command:
    def __init__(self, function, help=""):
        self.__func = function
        self.__help = help
    
    def __call__(self):
        self.__func()
    
    def __repr__(self):
        return self.__help

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__command_dict = {"помощь": Command(self.print_help, "Вывод этого сообщения"),
                               "выход": Command(self.exit, "Выйти из пользователя")}
    
    def check_password(self, password):
        return password == self.__password

    def add(self, command, function, help=""):
        self.__command_dict[command.lower()] = Command(function, help)

    def print_help(self):
        print("==============")
        print("Помощь:\n")
        for command_name in self.__command_dict.keys():
            print(f"[{command_name}]\n{self.__command_dict[command_name]}")
            print("\n")
        print("==============")

    def exit(self):
        self.is_running = False

    def run(self):
        self.is_running = True
        try:
            while self.is_running:
                command = input(f"[{self.__username}] ")
                command_to_exec = self.__command_dict.get(command.lower(), None)
                if command_to_exec is None:
                    print(f"Команды {command} не существует!")
                    continue
                command_to_exec()
        except KeyboardInterrupt:
            print("Выход из пользователя...")

class CommandLine:
    def __init__(self, prefix=">>> "):
        self.__prefix = prefix
        self.__message = "==== Default greeting message ===="
        self.__command_dict = {"помощь!": Command(self.print_help, "Показать это сообщение"),
                               "выход!": Command(self.exit, "Выйти из терминала"),
                               "вход!": Command(self.enter_user, "Авторизироваться"),
                               "пользователи!": Command(self.users, "Посмотреть список пользователей")}
        self.__userlist = {}

    def set_greeting_message(self, messgae):
        self.__message = messgae

    def add(self, command, function, help=""):
        self.__command_dict[command.lower()] = Command(function, help)
    
    def add_user(self, username, password):
        self.__userlist[username] = User(username, password)

    def get_user(self, username):
        return self.__userlist.get(username, None)

    def print_help(self):
        print("==============")
        print("Помощь:\n")
        for command_name in self.__command_dict.keys():
            print(f"[{command_name}]\n{self.__command_dict[command_name]}")
            print("\n")
        print("==============")
    
    def users(self):
        print("==============")
        print("Пользователи:\n")
        for username in self.__userlist.keys():
            print(f"[{username}]")
            print("")
        print("==============")

    def exit(self):
        print("Выход из терминала...")
        self.is_running = False

    def enter_user(self):
        username = input("Пользователь: ")
        user: User = self.get_user(username)
        if user is None:
            print("Такого пользователя не существует")
            return
        password = input("Пароль: ")
        if not user.check_password(password):
            print("Не правильный пароль")
            return
        user.run()

    def run(self):
        self.is_running = True
        print(self.__message)
        try:
            while self.is_running:
                command = input(self.__prefix)
                command_to_exec = self.__command_dict.get(command.lower(), None)
                if command_to_exec is None:
                    print(f"Команды {command} не существует!")
                    continue
                command_to_exec()
        except KeyboardInterrupt:
            print("Выход из терминала...")