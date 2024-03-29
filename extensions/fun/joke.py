import lightbulb
import hikari

joke_plugin = lightbulb.Plugin("joke", "Jokes! But be wary for the offensive ones!")

@joke_plugin.command()
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.option("lang", "The language of the joke", str, required=False, default = "en", choices = ["cs","de","en","es","fr","pt"])
@lightbulb.command("joke", "For all kinds of jokes! (Some might be offensive, be careful.)", auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def joke(ctx: lightbulb.Context, lang: str) -> None:
    parameters = {
        "format": "json",
        "amount": 1,
        "lang": lang
    }
    
    async with ctx.bot.d.aio_session.get('https://v2.jokeapi.dev/joke/Any', params = parameters) as resp:
        data = await resp.json()
        
    emb = hikari.Embed(title="Here comes a joke!")
        
    jokecategory = data["category"]
    thetype = data["type"]
    
    if thetype == "twopart":
        setup = data["setup"]
        delivery = data["delivery"]
        emb.add_field(name=f"Category: **{jokecategory}**", value=f"{setup}\n{delivery}")
    if thetype == "single":
        joke = data["joke"]
        emb.add_field(name=f"Category: **{jokecategory}**", value=joke)
    if data["error"] == "true":
        await ctx.respond("An Error has occured!")
        return
        
    await ctx.respond(embed=emb)
    

def load(bot):
    bot.add_plugin(joke_plugin)

def unload(bot):
    bot.remove_plugin(joke_plugin)
