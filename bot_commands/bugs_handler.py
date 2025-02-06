class BugsHandler:
    bugs_counter = 0

    @staticmethod
    def add_bug(user):
        BugsHandler.bugs_counter += 1
        return f"{user} añadió un nuevo bug, ya tenemos {BugsHandler.bugs_counter} bugs."
