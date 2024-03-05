class FirstHandler:
    first_user = ""

    @staticmethod
    def process_first_command(user):
        if FirstHandler.first_user == "":
            FirstHandler.first_user = user
            if user == "pythonesa":
                return "¡Pythonesa siempre es la primera!"
            else:
                return f"Felicidades {user}, eres el primero!"
        else:
            if FirstHandler.first_user == "pythonesa" and user == "pythonesa":
                return "¡Pythonesa siempre es la primera!"
            elif FirstHandler.first_user == "pythonesa":
                return f"¡Pythonesa siempre es la primera! Toma ejemplo {user}!"
            elif user == "pythonesa":
                return f"¡Pythonesa siempre es la primera! Aunque hoy le haya ganado {FirstHandler.first_user}."
            else:
                return f"Cálmate {user}, {FirstHandler.first_user} llegó antes."
        