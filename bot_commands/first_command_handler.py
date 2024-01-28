class FirstCommandHandler:
    first_user = ""

    @staticmethod
    def process_first_command(user):
        if FirstCommandHandler.first_user == "":
            FirstCommandHandler.first_user = user
            if user == "pythonesa":
                return "¡Pythonesa siempre es la primera!"
            else:
                return f"Felicidades {user}, eres el primero!"
        else:
            if FirstCommandHandler.first_user == "pythonesa":
                return f"¡Pythonesa siempre es la primera! Toma ejemplo {user}!"
            elif user == "pythonesa":
                return f"¡Pythonesa siempre es la primera! Aunque hoy le haya ganado {FirstCommandHandler.first_user}."
            else:
                return f"Cálmate {user}, {FirstCommandHandler.first_user} llegó antes."
        