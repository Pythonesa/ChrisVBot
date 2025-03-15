import random


def get_hit_without_to_user(nick):
    WITHOUT_TO_USER = [
        f"{nick} intentó golpear, pero la física dijo 'no'.",
        f"¡Golpe fallido! {nick} acaba de abofetear una brisa de aire.",
        f"{nick} lanzó un puñetazo... y se autogolpeó con el retroceso.",
        f"El aire ha esquivado tu golpe, {nick}. Nivel de habilidad: Ultra Instinto.",
        f"{nick} está peleando contra sus demonios internos... y perdiendo.",
        f"¡Golpe crítico al vacío! {nick} está practicando contra enemigos invisibles.",
        f"{nick} intentó atacar, pero activó el modo espectador sin querer.",
        f"¡Ojo! {nick} ha desbloqueado la técnica secreta: 'Puñetazo en la Nada'.",
        f"El viento le susurra a {nick}: 'Ni lo intentes, mortal'.",
        f"{nick}, hasta un saco de boxeo imaginario se ríe de ti en este momento.",
        f"{nick} intentó golpear... pero se olvidó de equipar el ataque.",
        f"¡Increíble! {nick} acaba de darle un uppercut a su autoestima.",
        f"{nick}, pegándole a la nada como si le debiera plata.",
        f"Golpe fallido. {nick} pierde 5 puntos de dignidad.",
        f"{nick} está practicando para la próxima pelea contra el aire.",
        f"Los físicos cuánticos aún intentan explicar el golpe de {nick}.",
        f"{nick} lanzó un puñetazo y entró en otra dimensión.",
        f"{nick}, al menos avísale al vacío antes de pegarle.",
        f"¡Golpe al aire! El oxígeno presenta cargos contra {nick}.",
        f"{nick} activó el modo Jedi y golpeó a la Fuerza misma."
    ]

    return random.choice(WITHOUT_TO_USER)


def get_hit_to_self(nick):
    TO_SELF = [
        f"{nick} intentó golpear a alguien... pero terminó pegándose a sí mism@. Bravo.",
        f"¡Auto-golpe crítico! {nick} se daña a sí mism@ en su confusión.",
        f"{nick} practicó una técnica de combate... en su propia cara.",
        f"{nick}, ¡eso fue un uppercut de amor propio! ...¿O de odio?",
        f"El enemigo más peligroso de {nick}... es {nick} mism@.",
        f"{nick} probó la técnica secreta del auto-ko. ¡Efectividad del 100%!",
        f"{nick} quiso demostrar su fuerza, pero solo demostró que duele mucho.",
        f"¡Golpe autoinfligido! {nick} necesita urgentemente un manual de instrucciones.",
        f"{nick}, si querías pelear, al menos elige a alguien que no seas tú.",
        f"¡Wow! {nick} acaba de desbloquear el arte marcial más raro: el autogolpe.",
        f"{nick} se golpeó a sí mism@... el espejo lo miró con decepción.",
        f"¡Plot twist! {nick} siempre fue su peor enemigo.",
        f"{nick} pensó que esquivaría el golpe... pero no contó con su propia torpeza.",
        f"Autoataque exitoso. {nick} ha aprendido a no pelear consigo mism@.",
        f"{nick}, no sé si eso fue un golpe o un intento de autodescubrimiento.",
        f"{nick} intentó esquivar, pero su otro yo estaba preparado.",
        f"{nick}, golpearte a ti mism@ no te da puntos de experiencia, solo de vergüenza.",
        f"¿Nuevo reto? {nick} se reta a un duelo consigo mism@.",
        f"{nick} descubrió que el enemigo final... estaba en el espejo.",
        f"{nick}, autoagredirse no es la solución. Mejor ve por un snack."
    ]

    return random.choice(TO_SELF)


def get_hit(nick, to_user):
    TO_USER = [
        # Golpes épicos
        f"¡{nick} lanza un puñetazo directo a {to_user}! ¡Impacto crítico!",
        f"{nick} le da una patada voladora a {to_user}, ¡como en las películas!",
        f"{nick} carga contra {to_user} y lo manda a volar.",
        f"¡BOOM! {nick} conecta un gancho de derecha a {to_user}.",
        f"{nick} le da un golpe tan fuerte a {to_user} que ahora ve en 4K.",
        f"¡Fatality! {nick} golpea a {to_user} con un combo imparable.",
        f"{nick} le lanza un codazo a {to_user}. ¡Eso tuvo que doler!",
        f"{nick} usa un puño giratorio contra {to_user}. ¡Parece sacado de un anime!",
        f"{nick} le da una bofetada a {to_user}. ¡Qué agresividad!",
        f"{nick} aplica un golpe de kárate a {to_user}. ¡Wax on, wax off!",

        # Fails épicos y cómicos
        f"{nick} intentó golpear a {to_user}... pero se tropezó y besó el suelo.",
        f"{nick} le lanzó un puñetazo a {to_user}, pero se resbaló y cayó de espaldas.",
        f"{nick} intentó una patada giratoria contra {to_user}, pero terminó girando solo y mareado.",
        f"{nick} cargó contra {to_user}, pero calculó mal y se estrelló contra la pared.",
        f"{nick} quiso darle un golpe a {to_user}, pero su zapato salió volando y golpeó a otro.",
        f"{nick} intentó un ataque sorpresa, pero se enredó en su propia ropa y cayó.",
        f"{nick} fue a golpear a {to_user}, pero se distrajo y se pegó solo.",
        f"{nick} intentó una llave de lucha contra {to_user}, pero terminó abrazándolo por error.",
        f"{nick} le lanzó un golpe a {to_user}... pero {to_user} ya no estaba ahí. Golpe al aire.",
        f"{nick} iba a golpear a {to_user}, pero se acalambró en el intento. ¡Fail!",
        f"{nick} le tiró un puñetazo a {to_user}, pero se le enganchó la manga y terminó pegándose en la cara.",
        f"{nick} intentó una patada alta contra {to_user}, pero perdió el equilibrio y aterrizó de culo.",
        f"{nick} fue a golpear a {to_user}, pero en su emoción, golpeó el aire y se cayó de frente.",
        f"{nick} intentó una técnica de lucha impresionante, pero se pisó los cordones y cayó como un saco de papas.",
        f"{nick} le lanzó un puñetazo a {to_user}, pero erró tan feo que hasta un espectador sintió vergüenza ajena.",
        f"{nick} intentó una llave de judo, pero terminó abrazando el suelo con amor.",
        f"{nick} quiso imitar a un luchador de la WWE, saltó y… se olvidó de dónde aterrizar. Epic fail.",
        f"{nick} intentó un movimiento ninja, pero terminó rodando por el piso como croqueta mal hecha.",
        f"{nick} cargó contra {to_user}, pero calculó mal y terminó dándole un cabezazo a la pared.",
        f"{nick} lanzó un golpe tan fuerte que perdió el equilibrio y cayó con estilo… en cámara lenta.",
        f"{nick} le tiró una patada a {to_user}, pero la inercia lo llevó directo al suelo.",
        f"{nick} fue a dar un golpe, pero su pantalón se rompió y ahora tiene un nuevo problema.",
        f"{nick} intentó golpear a {to_user}, pero resbaló con una cáscara de banana como en los dibujos animados.",
        f"{nick} se lanzó contra {to_user}, pero olvidó que había una silla en el camino. La silla ganó.",
        f"{nick} intentó dar una patada de kung fu, pero se quedó trabado como robot con batería baja.",
        f"{nick} trató de sorprender a {to_user}, pero tropezó y cayó con todo el drama de una telenovela.",
        f"{nick} intentó pegarle a {to_user}, pero falló tan mal que hasta la física se sintió insultada.",
        f"{nick} se lanzó con toda su fuerza… y se desvió tanto que golpeó a un espectador por accidente.",
        f"{nick} fue a golpear a {to_user}, pero en el proceso le pegó a su propio reflejo en el espejo. ¿Quién ganó?",
        f"{nick} intentó un golpe de karate, pero olvidó calentar y ahora está haciendo estiramientos forzados.",
        f"{nick} trató de hacer una entrada épica para pelear, pero se enredó con su propia capa y se cayó.",

        # Golpes con estilo
        f"{nick} le lanza un golpe épico a {to_user}, con pose de superhéroe incluida.",
        f"{nick} golpea a {to_user} con la fuerza de mil soles. ¡KA-BOOM!",
        f"¡Super combo! {nick} ataca a {to_user} con una serie de golpes veloces.",
        f"{nick} salta en el aire y lanza una patada giratoria digna de un videojuego contra {to_user}.",
        f"{nick} usa una técnica de lucha secreta contra {to_user}. ¡Efectividad del 100%!",
        f"{nick} carga energía y lanza un golpe destructivo a {to_user}. ¡KO!",
        f"{nick} y {to_user} intercambian golpes como si fuera una pelea de anime.",
        f"{nick} le da un golpe con tanto poder a {to_user} que lo manda a la estratósfera.",
        f"¡{nick} usa el golpe del dragón contra {to_user}! ¡Animación especial incluida!",
        f"{nick} lanza un golpe perfecto a {to_user}, al más puro estilo de un maestro de artes marciales."
    ]

    return random.choice(TO_USER)
