import random


def get_hug_without_to_user(nick):
    WITHOUT_TO_USER = [
        f"No puedes abrazar al aire, {nick}. ¿Lo sabes, verdad?",
        f"¡Oye, {nick}! No puedes simplemente abrazar a la nada. ¡Elige a alguien!",
        f"¿A quién intentas abrazar, {nick}? ¡Dímelo!",
        f"Parece que {nick} está practicando abrazos imaginarios.",
        f"¡Vamos, {nick}! Elige a alguien real para ese abrazo.",
        f"{nick} está intentando abrazar su imaginación.",
        f"Si intentas abrazar al aire, {nick}, al menos hazlo con estilo.",
        f"{nick}, ¡la nada también necesita abrazos!",
        f"¿Practicando tus técnicas de abrazo, {nick}?",
        f"{nick} intentó abrazar a alguien, pero parece que se volvió invisible.",
        f"¡Es un abrazo fantasma, {nick}!",
        f"{nick}, ¿estás abrazando a tus amigos imaginarios?",
        f"Creo que {nick} está intentando inventar el abrazo aéreo.",
        f"¡Ups! Parece que {nick} se olvidó de elegir a alguien para abrazar.",
        f"¿Estás bien, {nick}? Pareces estar abrazando a un fantasma.",
        f"¡Abrazos invisibles cortesía de {nick}!",
        f"{nick}, ese abrazo parece un poco... vacío.",
        f"¿Un abrazo al aire, {nick}? ¡Eso es nuevo!",
        f"Parece que {nick} quiere abrazar a todo el chat de una vez.",
        f"¡Tal vez {nick} vio algo que nosotros no vimos!"
    ]

    return random.choice(WITHOUT_TO_USER)


def get_hug_to_self(nick):
    TO_SELF = [
        f"Eh, {nick}, es raro que te abraces a ti mism@. ¿Estás bien?",
        f"¿Necesitas un abrazo, {nick}? ¡Aquí estamos para apoyarte!",
        f"¡A veces, todos necesitamos auto-abrazarnos, verdad {nick}?",
        f"Parece que {nick} necesita un poco de amor propio. ¡Eso está bien!",
        f"{nick}, ¡darte un auto-abrazo es una gran forma de mostrarte amor propio!",
        f"¡Es bueno amarse a uno mismo, {nick}!",
        f"¡Vaya! {nick} se está dando un poco de cariño propio.",
        f"Todos necesitamos un abrazo de vez en cuando, ¿verdad {nick}?",
        f"{nick} está mostrando cómo amarse a uno mismo.",
        f"Un poco de amor propio nunca viene mal, ¿eh {nick}?",
        f"¡Eso es un poco solitario, {nick}! ¿Quieres que te demos un abrazo grupal?",
        f"{nick}, recuerda que siempre puedes contar con el chat para recibir abrazos.",
        f"¡No te preocupes, {nick}! Aquí todos te queremos y te abrazamos virtualmente.",
        f"¿Todo está bien, {nick}? ¡Estamos aquí para ti!",
        f"Parece que {nick} está practicando el arte del auto-abrazo.",
        f"{nick} muestra que a veces, todo lo que necesitas es darte un poco de cariño a ti mism@.",
        f"¡Hey, {nick}! Siempre puedes pedir un abrazo aquí.",
        f"{nick}, abrazarte a ti mism@ es un recordatorio de que eres amado.",
        f"¡Eso es amor propio, {nick}!",
        f"{nick} sabe que a veces, tienes que ser tu propio héroe."
    ]

    return random.choice(TO_SELF)


def get_hug(nick, to_user):
    TO_USER = [
        f"¡{nick} da un fuerte abrazo a {to_user}!",
        f"{nick} envuelve a {to_user} en un cálido abrazo.",
        f"{to_user}, ¡{nick} te ha dado un abrazo sorpresa!",
        f"{nick} y {to_user} comparten un tierno momento de abrazo.",
        f"¡Qué lindo ver a {nick} abrazando a {to_user}!",
        f"{nick} abraza a {to_user} como si no hubiera un mañana.",
        f"¡Abrazo alerta! {nick} ha atrapado a {to_user} en un abrazo.",
        f"¡{to_user}! {nick} te ha dado un abrazo especial.",
        f"¡Es un abrazo de oso de {nick} a {to_user}!",
        f"{nick} corre hacia {to_user} y le da un abrazo épico.",
        f"{nick} y {to_user} están en modo abrazo total.",
        f"¡Es un abrazo en equipo entre {nick} y {to_user}!",
        f"{nick} se acerca sigilosamente y... ¡abraza a {to_user}!",
        f"{nick} da un abrazo cariñoso a {to_user}. ¡Qué dulce!",
        f"{to_user}, parece que {nick} te extrañaba. ¡Abrazo!",
        f"¡Momento de abrazo! {nick} y {to_user} están en ello.",
        f"¡{nick} ha elegido a {to_user} para su abrazo del día!",
        f"{nick} y {to_user}, demostrando que los abrazos son la mejor medicina.",
        f"¡Alerta de ternura! {nick} está abrazando a {to_user}.",
        f"Es un abrazo de amistad entre {nick} y {to_user}. ¡Hermoso!",
        f"¡{nick} lanza un abrazo aéreo a {to_user}!",
        f"¡{to_user}, {nick} ha decidido que mereces un super abrazo!",
        f"¡Nada como un abrazo entre amigos! Bien hecho, {nick} y {to_user}.",
        f"¡Es un abrazo mágico de {nick} a {to_user}!",
        f"{nick} ha atrapado a {to_user} en un abrazo inesperado.",
        f"{nick} da un abrazo de osito a {to_user}. ¡Tan reconfortante!",
        f"{nick} y {to_user} demuestran que los abrazos hacen el día mejor.",
        f"¡{nick} abraza a {to_user} en un momento perfecto!",
        f"{nick} le da a {to_user} el abrazo que tanto necesitaba.",
        f"¡Momento épico! {nick} da un abrazo poderoso a {to_user}.",
        f"¡Qué momento! {nick} ha dado el abrazo perfecto a {to_user}.",
        f"{nick} y {to_user}, compartiendo un momento abrazo.",
        f"¡Es un abrazo lleno de energía de {nick} a {to_user}!",
        f"{nick} abraza a {to_user} con toda su fuerza. ¡Qué pasión!",
        f"¡{nick} sorprende a {to_user} con un abrazo desde atrás!",
        f"¡Es un abrazo lleno de sonrisas entre {nick} y {to_user}!",
        f"{nick} da un abrazo super especial a {to_user}.",
        f"¡Abrazo a la vista! {nick} y {to_user} están en ello.",
        f"¡{nick} abraza a {to_user} levantando el espíritu del chat!",
        f"{nick} le da un abrazo reconfortante a {to_user}.",
        f"¡{to_user}, parece que {nick} realmente quería darte un abrazo!",
        f"{nick} ha decidido que {to_user} merece un gran abrazo.",
        f"¡Momento especial! {nick} y {to_user} comparten un abrazo mágico.",
        f"{nick} se lanza en un abrazo aventurero hacia {to_user}.",
        f"El amor está en el aire: ¡{nick} abraza a {to_user}!",
        f"{nick} da un abrazo relajante a {to_user}. ¡Justo lo que necesitaban!",
        f"¡Qué tierno! {nick} da un abrazo suave a {to_user}.",
        f"{to_user}, ¡siente el calor del abrazo de {nick}!",
        f"Es un abrazo lleno de felicidad entre {nick} y {to_user}.",
        f"¡{nick} ha dado un abrazo inolvidable a {to_user}!",
        f"¡Alerta de amistad! {nick} y {to_user} están compartiendo un abrazo.",
        f"{nick} da un abrazo lleno de amor a {to_user}. ¡Qué dulce!",
        f"¡Momento memorable! {nick} abrazando a {to_user}.",
        f"¡Es un abrazo lleno de risas entre {nick} y {to_user}!",
        f"{nick} y {to_user} comparten un abrazo lleno de alegría.",
        f"¡{nick} le da a {to_user} un abrazo que ilumina el día!",
        f"¡Es un abrazo encantador de {nick} a {to_user}!",
        f"{nick} da un abrazo a {to_user} lleno de buenas vibras.",
        f"{nick} y {to_user}, ¡compartiendo un abrazo que vale oro!",
        f"¡{nick} da un abrazo sorpresa a {to_user}!",
        f"{nick} y {to_user}, ¡celebrando con un gran abrazo!",
        f"¡{nick} da un abrazo que dura una eternidad a {to_user}!",
        f"{nick} y {to_user}, ¡demostrando que un abrazo dice más que mil palabras!",
        f"¡Es un abrazo legendario entre {nick} y {to_user}!",
        f"{nick} da el abrazo perfecto a {to_user}. ¡Bella conexión!",
        f"¡{nick} abraza a {to_user} como nunca antes!",
        f"{nick} y {to_user}, ¡el dúo dinámico del abrazo!",
        f"¡{nick} lanza un abrazo cariñoso a {to_user}!",
        f"¡{nick} y {to_user} crean el momento abrazo perfecto!",
        f"{nick} y {to_user}, ¡abrazándose como campeones!",
        f"¡{nick} da un abrazo que podría derretir corazones a {to_user}!",
        f"{nick} y {to_user} compartiendo un abrazo que todos envidiarían.",
        f"¡Es un abrazo maratón entre {nick} y {to_user}!",
        f"{nick} abraza a {to_user} con toda la felicidad del mundo.",
        f"¡{nick} da un abrazo a {to_user} que se siente como una suave brisa!",
        f"¡{nick} y {to_user}, haciendo del chat un lugar más cálido con ese abrazo!",
        f"Es un abrazo lleno de risas y alegría entre {nick} y {to_user}.",
        f"{nick} da un abrazo a {to_user} que siente como un rayo de sol.",
        f"¡{nick} y {to_user}, compartiendo un abrazo que dura toda una vida!",
        f"{nick} y {to_user}, demostrando que un abrazo puede cambiar el día.",
        f"¡{nick} da un abrazo a {to_user} que siente como una suave melodía!",
        f"¡Es un abrazo que todos querrían! Bien hecho, {nick} y {to_user}.",
        f"{nick} y {to_user}, ¡el dúo perfecto para un abrazo!",
        f"¡Es un abrazo que se siente como un abrazo! {nick} a {to_user}.",
        f"{nick} da un abrazo a {to_user} que todos recordarán.",
        f"¡{nick} y {to_user}, creando recuerdos con ese abrazo!",
        f"¡{nick} da un abrazo a {to_user} que ilumina el chat!",
        f"{nick} y {to_user}, unidos por un abrazo inquebrantable.",
        f"¡{nick} da un abrazo a {to_user} que siente como un cuento de hadas!",
        f"{nick} y {to_user}, ¡la combinación perfecta para un abrazo perfecto!",
        f"¡Es un abrazo que vale la pena recordar entre {nick} y {to_user}!"
    ]

    return random.choice(TO_USER)
