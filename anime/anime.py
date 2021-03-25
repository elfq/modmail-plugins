import discord
from discord.ext import commands

import aiohttp

class AnimePlugin(commands.Cog):
  """A plugin to browse through various animes and find stats about them!"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name = "anime")
  async def anime_(self, ctx : commands.Context, *, anime):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://api.jikan.moe/v3/search/anime?q={anime}") as r:
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


def setup(bot: commands.Bot):
  bot.add_cog(AnimePlugin(bot))
