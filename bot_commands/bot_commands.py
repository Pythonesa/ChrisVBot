from twitchio.ext import commands
from bot_commands.first_handler import FirstHandler as fch
from bot_commands.second_hadler import SecondHandler as sch
from bot_commands.hug_handler import get_hug, get_hug_without_to_user, get_hug_to_self
from bot_commands.bugs_handler import BugsHandler as bh
from bot_commands.sape_handler import SapeHandler as sh
from bot_commands.hit_handler import get_hit, get_hit_without_to_user, get_hit_to_self


@commands.command(name='help')
async def help(ctx):
    await ctx.send(f"Acepto los siguientes comandos: !streams !first !francia !hug !leak !bug !sape !porro !carritos !encuesta !pythonesa !sensei !padauchi !hamster")


@commands.command(name='streams')
async def streams(ctx):
    await ctx.send(f"Hay streams los lunes, miércoles y viernes a partir de las 20:00 hora Argentina. Además, los Sábados a la noche jugamos.")


@commands.command(name='first')
async def first(ctx):
    await ctx.send(fch.process_first_command(ctx.author.name))


@commands.command(name='francia')
async def francia(ctx):
    await ctx.send(sch.process_francia_command(ctx.author.name))


@commands.command(name="hug")
async def hug(ctx, *, nick: str = None):
    if not nick:
        await ctx.send(get_hug_without_to_user(ctx.author.name))
        return
    elif nick.lower() == ctx.author.name.lower():
        await ctx.send(get_hug_to_self(ctx.author.name))
    else:
        await ctx.send(get_hug(ctx.author.name, nick))


@commands.command(name="leak")
async def leak(ctx):
    await ctx.send("¡Póngase una toalla señor que se le ve todo!")


@commands.command(name="bug")
async def bug(ctx):
    await ctx.send(bh.add_bug(ctx.author.name))


@commands.command(name="porro")
async def porro(ctx):
    await ctx.send("¡Armate uno Chris!")


@commands.command(name="carritos")
async def carritos(ctx):
    await ctx.send("Dale Chris! Juguemos unos carritos! No te pongas la gorra!")


@commands.command(name="encuesta")
async def encuesta(ctx):
    await ctx.send("La democracia no sirve... pero decidan igual!")


@commands.command(name="pythonesa")
async def pythonesa(ctx):
    await ctx.send("Aprende de verdad con pythonesa y su blog: https://blognesa.netlify.app/")


@commands.command(name="sensei")
async def sensei(ctx):
    await ctx.send("Toma, aquí tienes las sagradas escrituras del código, la ManzPedia: https://manz.dev/")


@commands.command(name="padauchi")
async def padauchi(ctx):
    await ctx.send("¿Querés aprender desarrollo web y PHP? https://twitch.tv/padawanstrainer Ahora, si querés falopa y conocer la intimidad entre Chris y un Castor, anda a https://twitch.tv/radioauchi")


@commands.command(name="sape")
async def sape(ctx, *, nick: str = None):
    if not nick:
        await ctx.send(sh.sape())
    else:
        await ctx.send(sh.sape_to_user(ctx.author.name, nick))


@commands.command(name="hamster")
async def hamster(ctx):
    await ctx.send("No puedes ser feliz si no sigues a Afor! Siguela en su canal de twitch https://twitch.tv/afor_digital quizás hasta llegues a formar parte de la élite que sabe que HTML es un lenguaje de programación!")


@commands.command(name="hit")
async def hit(ctx, *, nick: str = None):
    if not nick:
        await ctx.send(get_hit_without_to_user(ctx.author.name))
        return
    elif nick.lower() == ctx.author.name.lower():
        await ctx.send(get_hit_to_self(ctx.author.name))
    else:
        await ctx.send(get_hit(ctx.author.name, nick))
