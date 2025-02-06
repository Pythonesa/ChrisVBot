from bot_commands.first_handler import FirstHandler as fh


class SecondHandler:
    second_user = ""

    @staticmethod
    def process_francia_command(user):
        if fh.first_user == "":
            return f"{user}, no puedes reclamar el segundo lugar si no hay un primero."
        else:
            if fh.first_user == user:
                return f"{user}, no puedes reclamar el segundo lugar si eres el primero."
            elif SecondHandler.second_user == "":
                SecondHandler.second_user = user
                return f"Felicidades {user}, eres el segundo!"
            elif SecondHandler.second_user == user:
                return f"{user}, cálmate que la medalla ya te la dieron!"
            else:
                return f"Cálmate {user}, {SecondHandler.second_user} llegó antes."
