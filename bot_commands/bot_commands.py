from twitchio.ext import commands

@commands.command(name='commands')
async def commands(ctx):
    await ctx.send(f"No tengo comandos, soy pobre...")