import discord
from discord.ext import commands


class Nick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  
  @commands.command(name="nickr", aliases=["nickrequest", "nrequest", "nr"])
  async def nickname_(self, ctx, name):
    
    
    if len(name) > 32: # Check if a nickname is over the length of 32.
      await ctx.send(":x: You cannot have a nickname this long!")
      
    if len(name) < 2: # Check if a name is shorter then 2.
      await ctx.send(":x: Your nickname cannot be this short.")
      
    await ctx.send("Sent a nickname request!")
    embed = discord.Embed(description = f"**{ctx.author} ({ctx.author.id})** wants their nickname changed to **{name}**.", color = 0x02FF00)
    embed.set_author(name = "New Nickname Request", icon_url = ctx.author.avatar_url)
    embed.set_footer(text = "React with ✅ to approve this nickname, or ❌ to decline it.")
    channel = self.bot.get_channel(824852550649249792)
    msg = await channel.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")
    
    def check(r, u):
            return (
                u.id == ctx.author.id
                and r.message.channel.id == ctx.channel.id
                and str(r.emoji) in ["✅", "❌"]
            )

    try:
        reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=99999999999.0)
        
    except TimeoutError:
            await ctx.send("_ _")
            return
    else:
        if str(reaction.emoji) == "✅":
              await ctx.author.edit(nick=name)
              await ctx.author.send(f"✅ Your nickname has been changed to `{name}`")
                                    
            
        if str(reaction.emoji) == "❌":
              await ctx.author.send(f"❌ Your nickname request has been declined!")

                

def setup(bot):
  bot.add_cog(Nick(bot))
