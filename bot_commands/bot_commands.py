from twitchio.ext import commands

@commands.command(name='help')
async def help(ctx):
    await ctx.send(f"Acepto los siguientes comandos: !streams")

@commands.command(name='streams')
async def streams(ctx):
    await ctx.send(f"Los Lunes hacemos Frontend, los Miércoles Backend y los Viernes Infra. Empezando a las 19:30 hora Argentina. Además, los Sábados a la noche jugamos.")