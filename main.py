import api
from discord.ext import commands

# Not very secure, but it's whatever
TOKEN = "ODIzNjI5ODE1Nzk3MTIxMDQ1.YFjnCg.oUrS_c1s7Jztut2-d3nCwx62GR0"
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f"Connected to bot: {client.user.name}")
    print(f"Bot ID: {client.user.id}")


@client.command()
async def vaccines(context, state: str = None):
    if state is None:
        await context.send(api.total_vaccines())
    else:
        await context.send(api.vaccines(state.upper()))


@client.command()
async def deaths(context, state: str = None):
    if state is None:
        await context.send(api.total_deaths())
    else:
        await context.send(api.deaths(api.abbrev_to_us_state[state.upper()]))


@client.command()
async def cases(context, state: str = None):
    if state is None:
        await context.send(api.total_cases())
    else:
        await context.send(api.cases(api.abbrev_to_us_state[state.upper()]))

client.run(TOKEN)
