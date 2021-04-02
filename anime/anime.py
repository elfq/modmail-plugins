import discord
from discord.ext import commands

import aiohttp


class AnimePlugin(commands.Cog):
    """A plugin for various anime commands!"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        @commands.command()
        async def hug(self, ctx: commands.Context, user: discord.Member):
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://shiro.gg/api/images/hug") as r:
                    re = await r.json()
                    if user == ctx.author:
                        embed = discord.Embed(
                            description=f"**{ctx.author.name}** hugs themselves!",
                            color=discord.Colour.random(),
                        )
                        embed.set_image(url=re["url"])
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            description=f"**{ctx.author.name}** hugs **{user.name}**",
                            color=discord.Colour.random(),
                        )
                        embed.set_image(url=re["url"])
                        await ctx.send(embed=embed)

        @commands.command()
        async def pat(self, ctx: commands.Context, user: discord.Member):
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://shiro.gg/api/images/pat") as r:
                    re = await r.json()
                    if user == ctx.author:
                        embed = discord.Embed(
                            description=f"**{ctx.author.name}** gives themselves a pat on the back!",
                            color=discord.Colour.random(),
                        )
                        embed.set_image(url=re["url"])
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            description=f"**{ctx.author.name}** pats **{user.name}**",
                            color=discord.Colour.random(),
                        )
                        embed.set_image(url=re["url"])
                        await ctx.send(embed=embed)

        @commands.group(invoke_without_command=True)
        async def anime(self, ctx: commands.Context):
            await ctx.send("_ _")

        @anime.command()
        async def search(self, ctx: commands.Context, *, name):
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                    f"https://api.jikan.moe/v3/search/anime?q={name}"
                ) as r:
                    re = await r.json()
                    embed = discord.Embed(
                        description=re["results"][0]["synopsis"], color=0x7289DA
                    )
                    embed.set_author(
                        name=re["results"][0]["title"], icon_url=ctx.author.avatar_url
                    )
                    embed.add_field(
                        name="Information",
                        value=f"**Episodes**: {re['results'][0]['episodes']}\n**Age Rating**: {re['results'][0]['rated']}\n**Start Date**: {re['results'][0]['start_date'][:-15]}\n**End Date**: {re['results'][0]['end_date'][:-15]}\n**Type:** {re['results'][0]['type']}",
                    )
                    embed.set_thumbnail(url=re["results"][0]["image_url"])
                    embed.set_footer(
                        text=f"⭐ score: {re['results'][0]['score']} | {re['results'][0]['members']} viewers"
                    )
                    await ctx.send(embed=embed)

        @anime.command()
        async def image(self, ctx: commands.Context):
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://shiro.gg/api/images/avatars") as r:
                    re = await r.json()
                    embed = discord.Embed(
                        description=f"**Here's your anime image!**", color=0x7289DA
                    )
                    embed.set_image(url=re["url"])
                    await ctx.send(embed=embed)

        @anime.command(aliases=["background"])
        async def wallpaper(self, ctx: commands.Context):
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://shiro.gg/api/images/wallpapers") as r:
                    re = await r.json()
                    embed = discord.Embed(
                        description=f"**Here's your background!**", color=0x7289DA
                    )
                    embed.set_image(url=re["url"])
                    await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(AnimePlugin(bot))
