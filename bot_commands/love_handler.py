import random


def get_love_with_user(nick, to_user):
    LOVE_WITH_TARGET = [
        f"{nick} le envía amor a {to_user} porque hoy se nota que lo necesita. 💜",
        f"{nick} lanza un corazón volador directo a {to_user}. 💘 ¡Catch it!",
        f"{nick} no lo dudó y llenó de amor a {to_user}, porque a veces eso es justo lo que falta.",
        f"{nick} le tiró un abrazo con glitter a {to_user}. 🌈✨",
        f"{nick} vio a {to_user} medio bajón... y dijo: ¡AMOR EN 3, 2, 1! 💥💖",
        f"{nick} hackeó el sistema para mandar amor directamente a {to_user}. 💾💕",
        f"{nick} le mandó un 'te banco fuerte' a {to_user}. Porque no todo se soluciona con código.",
        f"{nick} abrió un PR de cariño para {to_user}. Esperando merge emocional. 🥺👉👈",
        f"{nick} recargó la energía de {to_user} con puro cariño. 🔋💗",
        f"{nick} sintió que {to_user} lo necesitaba, y le mandó un paquete comprimido de amor. 📦💞",
        f"{nick} le mandó un sticker mental a {to_user}. Todo corazón, cero bugs. ❤️🐞",
        f"{nick} puso pausa al caos y soltó un abrazo para {to_user}. ⏸️🤗",
        f"{nick} le mandó a {to_user} un hotfix de ánimo. Funciona en producción. 🚑💖",
        f"{nick} escribió una función especial: def amor({to_user}): return 💝",
        f"{nick} invocó una lluvia de amor sobre {to_user}. 🌧️💓",
        f"{nick} conectó con el servidor del corazón y envió un ping de ternura a {to_user}. 📡💕",
        f"{nick} detectó que {to_user} tenía el corazón en 10% y mandó un cargador emocional. 🔌❤️",
        f"{nick} le regaló a {to_user} una taza de ternura caliente. ☕💖",
        f"{nick} llenó el buffer emocional de {to_user} con puro cariño. 🧠💗",
        f"{nick} tiró un hechizo de amor nivel 99 sobre {to_user}. ✨🧙‍♀️💘",
        f"{nick} encontró a {to_user} bajito de energía y dijo: 'Toma un poco del mío'. 🔁💞",
        f"{nick} reinició el sistema de {to_user} con un abrazo. 🖥️🤍",
        f"{nick} le mandó un stream de amor sin latencia a {to_user}. 📡💓",
        f"{nick} le mandó a {to_user} una docena de galletitas pixeladas. 🍪💗",
        f"{nick} le hizo un push directo al corazón de {to_user}. 💻➡️❤️",
        f"{nick} descubrió que {to_user} tenía el firewall emocional activado… y lo desactivó con amor. 🔥💓",
        f"{nick} llenó el log de {to_user} con mensajes de cariño. 📝💖",
        f"{nick} le dedicó su ancho de banda emocional a {to_user}. 🌐💘",
        f"{nick} le mandó un commit de afecto a {to_user}. No hay rollback posible. 🔥💌",
        f"{nick} desencriptó el alma de {to_user} y le inyectó ternura. 🛡️🔓💝",
        f"{nick} mandó un ping a {to_user}... y fue respondido con lagrimitas de felicidad. 💧💘",
        f"{nick} puso a compilar todo su cariño y se lo mandó a {to_user}. ⏳❤️",
        f"{nick} creó una variable solo para almacenar amor para {to_user}. 🧪💞",
        f"{nick} le escribió a {to_user} un poema binario: 01100001 01101101 01101111 01110010 ❤️",
        f"{nick} usó un iframe mágico para mostrarle a {to_user} cuánto lo quiere. 🌐💝",
        f"{nick} cacheó el amor para {to_user} y lo sirvió con baja latencia. ⚡💓",
        f"{nick} convirtió un bug emocional en feature de cariño para {to_user}. 🐛➡️💖",
        f"{nick} reescribió todo su código interno solo para poder amar más a {to_user}. 💻❤️",
        f"{nick} mandó una request POST con body lleno de amor para {to_user}. 🔁💘",
        f"{nick} desplegó un contenedor con puro apapacho para {to_user}. 🐳💓",
        f"{nick} seteó el estado de ánimo de {to_user} a 'amado'. 🧠✅",
        f"{nick} hizo un deploy de abrazos para {to_user}. Producción nunca estuvo tan estable. 💞",
        f"{nick} encontró el breakpoint emocional de {to_user}... y lo arregló con cariño. 🧠🛠️💖",
        f"{nick} hizo un GET de sonrisas y un POST de amor directo a {to_user}. 🔁😄",
        f"{nick} le mandó un `console.log('te quiero {to_user}')` porque a veces hay que decirlo claro. 💬💘",
        f"{nick} llamó a la API del cariño y pasó a {to_user} como parámetro. 📲💝",
        f"{nick} hizo un refactor de emociones y puso el amor hacia {to_user} como constante. 🔄💖",
        f"{nick} desplegó una CDN de abrazos en la región más cercana a {to_user}. 🌍🤗",
        f"{nick} hizo que el universo hiciera un try-catch del malestar de {to_user} y lo reemplazó por puro bien. 🌀✨",
        f"{nick} configuró su router interno para que todas las rutas lleven a {to_user} con amor. 🛣️❤️"
    ]

    return random.choice(LOVE_WITH_TARGET)


def get_love_air(nick):
    LOVE_TO_AIR = [
        f"{nick} soltó amor en el aire como si fuera confeti. 💖🎉 Agarrá el tuyo antes que caiga al piso.",
        f"{nick} lanzó una explosión de ternura al chat. Si te pegó, ya está: estás más feliz. 💥💗",
        f"{nick} sintió que el ambiente estaba medio frío... y tiró un abrazo grupal. 🤗🔥",
        f"{nick} no sabía a quién dárselo... así que el amor va para TODO el chat. 💌🌍",
        f"{nick} apretó el botón rojo del cariño. BOOM. Amor para todes. 🧨💝",
        f"{nick} metió amor en la licuadora y lo sirvió para el chat entero. 🥤💞",
        f"{nick} abrió la válvula de los abrazos. Están saliendo a presión. 🚿🤍",
        f"{nick} dijo: '¿Para quién es el amor?' y el universo respondió: 'Para todos'. 🌌💓",
        f"{nick} mandó un update emocional. Todos recibieron +50 de afecto. 🔄💗",
        f"{nick} no se guardó nada. Amor sin destinatario, pero con alto impacto. 📡❤️",
    ]

    return random.choice(LOVE_TO_AIR)
