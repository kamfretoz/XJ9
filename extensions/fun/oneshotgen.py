import lightbulb
import hikari
from PIL import Image, ImageFont, ImageDraw
from textwrap import fill
from io import BytesIO
from pathlib import Path

faces = []

for path in Path("./res/oneshot/faces/").glob("*.png"):
    faces.append(path.name[:-4])

oneshot_plugin = lightbulb.Plugin("oneshot", "OneShot TextBox Generator")

@oneshot_plugin.command()

@lightbulb.option("text", "The text you want to write", str, required=True)
@lightbulb.option("expression", "The expression you want Niko to be", str, required=True, choices=faces)
@lightbulb.command("oneshot", "Generate a custom OneShot Textbox")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def oneshotgen(ctx: lightbulb.Context) -> None:
    text = ctx.options.text
    expr = ctx.options.expression
    await ctx.respond("Loading... Please Wait!")
    with Image.open("res/oneshot/template.png") as template:
        template = template.convert("RGBA")
        with Image.open("res/oneshot/textboxArrow.png") as arrow:
            arrow = arrow.convert("RGBA")
            template.alpha_composite(arrow, (300, 118))
            with Image.open(f"res/oneshot/faces/{expr}.png") as sprite:
                sprite = sprite.convert("RGBA")
                template.alpha_composite(sprite, (496, 16))
                font = ImageFont.truetype("res/oneshot/font-b.ttf", 24)
                draw = ImageDraw.Draw(template)
                stuff = fill(text ,width=40)
                draw.multiline_text((20, 8), stuff, fill=(255,255,255,255), font=font, align = "left")
                with BytesIO() as image_binary:
                    template.save(image_binary, format="PNG")
                    image_binary.seek(0)
                    await ctx.edit_last_response("Here you go!",attachment = image_binary)
    
def load(bot):
    bot.add_plugin(oneshot_plugin)

def unload(bot):
    bot.remove_plugin(oneshot_plugin)
