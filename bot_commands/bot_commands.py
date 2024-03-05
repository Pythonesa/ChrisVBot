from twitchio.ext import commands
from bot_commands.first_handler import FirstHandler as fch
from bot_commands.second_hadler import SecondHandler as sch
from bot_commands.hug_handler import get_hug, get_hug_without_to_user, get_hug_to_self
from bot_commands.bugs_handler import BugsHandler as bh
from bot_commands.sape_handler import SapeHandler as sh

@commands.command(name='help')
async def help(ctx):
    await ctx.send(f"Acepto los siguientes comandos: !streams !first !second !hug !leak !bug !sape")

@commands.command(name='streams')
async def streams(ctx):
    await ctx.send(f"Los Lunes hacemos Frontend, los Miércoles Backend y los Viernes Infra. Empezando a las 19:30 hora Argentina. Además, los Sábados a la noche jugamos.")

@commands.command(name='first')
async def first(ctx):
    await ctx.send(fch.process_first_command(ctx.author.name))

@commands.command(name='second')
async def second(ctx):
    await ctx.send(sch.process_second_command(ctx.author.name))

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

@commands.command(name="sape")
async def sape(ctx, *, nick: str = None):
    if not nick:
        await ctx.send(sh.sape())
    else:
        await ctx.send(sh.sape_to_user(ctx.author.name, nick))
    