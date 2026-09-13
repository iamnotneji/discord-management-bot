import discord
from discord.ext import commands
import json
import os

WELCOME_FILE = 'welcome_config.json'

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_config = self.load_welcome_config()

    def load_welcome_config(self):
        if os.path.exists(WELCOME_FILE):
            with open(WELCOME_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_welcome_config(self):
        with open(WELCOME_FILE, 'w') as f:
            json.dump(self.welcome_config, f, indent=4)

    @commands.command(name='setwelcome')
    @commands.has_permissions(manage_guild=True)
    async def setwelcome(self, ctx, channel: discord.TextChannel, *, message):
        """Set a welcome message for new members"""
        guild_id = str(ctx.guild.id)
        self.welcome_config[guild_id] = {
            'channel_id': channel.id,
            'message': message
        }
        self.save_welcome_config()
        
        embed = discord.Embed(
            title="Welcome Message Set",
            description=f"Welcome message has been set for {channel.mention}",
            color=discord.Color.green()
        )
        embed.add_field(name="Message", value=message, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='removewelcome')
    @commands.has_permissions(manage_guild=True)
    async def removewelcome(self, ctx):
        """Remove the welcome message"""
        guild_id = str(ctx.guild.id)
        if guild_id in self.welcome_config:
            del self.welcome_config[guild_id]
            self.save_welcome_config()
            await ctx.send("Welcome message has been removed.")
        else:
            await ctx.send("No welcome message is set for this server.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Send welcome message when a member joins"""
        guild_id = str(member.guild.id)
        if guild_id in self.welcome_config:
            config = self.welcome_config[guild_id]
            channel = member.guild.get_channel(config['channel_id'])
            if channel:
                message = config['message'].replace('{member}', member.mention).replace('{server}', member.guild.name)
                embed = discord.Embed(
                    title="Welcome!",
                    description=message,
                    color=discord.Color.green()
                )
                embed.set_thumbnail(url=member.display_avatar.url)
                await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
