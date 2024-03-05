class SapeHandler:
    sapes = 0
    def sape_to_user(nick, to_user):
        return f"¡{nick} ha sapeado a {to_user}!"

    def sape():
        SapeHandler.sapes += 1
        return f"¡Pythonesa ha sapeado a ChrisVDev {SapeHandler.sapes} veces!"