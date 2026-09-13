import discord
from discord.ext import commands
from datetime import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        """Get a member's avatar"""
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(
            title=f"{member.name}'s Avatar",
            color=discord.Color.blue()
        )
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='nickname')
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, new_nickname=None):
        """Change a member's nickname"""
        try:
            await member.edit(nick=new_nickname)
            if new_nickname:
                await ctx.send(f"Changed {member.mention}'s nickname to **{new_nickname}**")
            else:
                await ctx.send(f"Reset {member.mention}'s nickname.")
        except discord.Forbidden:
            await ctx.send("I don't have permission to change this member's nickname.")

    @commands.command(name='userinfo')
    async def userinfo(self, ctx, member: discord.Member = None):
        """Get information about a user"""
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(
            title=f"User Info - {member.name}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%B %d, %Y"), inline=False)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%B %d, %Y"), inline=False)
        embed.add_field(name="Roles", value=', '.join([role.mention for role in member.roles[1:]]) or 'No roles', inline=False)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo')
    async def serverinfo(self, ctx):
        """Get information about the server"""
        guild = ctx.guild
        embed = discord.Embed(
            title=f"Server Info - {guild.name}",
            color=discord.Color.green()
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="ID", value=guild.id, inline=False)
        embed.add_field(name="Owner", value=guild.owner.mention, inline=False)
        embed.add_field(name="Created", value=guild.created_at.strftime("%B %d, %Y"), inline=False)
        embed.add_field(name="Members", value=guild.member_count, inline=False)
        embed.add_field(name="Channels", value=len(guild.channels), inline=False)
        embed.add_field(name="Roles", value=len(guild.roles), inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check bot latency"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="Pong! 🏓",
            description=f"Latency: {latency}ms",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command(name='help')
    async def help(self, ctx):
        """Show bot commands"""
        embed = discord.Embed(
            title="Bot Commands",
            description="Here are all available commands:",
            color=discord.Color.blue()
        )
        embed.add_field(name="Moderation", value="`!kick`, `!ban`, `!unban`, `!mute`, `!unmute`, `!warn`, `!purge`", inline=False)
        embed.add_field(name="Utility", value="`!avatar`, `!nickname`, `!userinfo`, `!serverinfo`, `!ping`", inline=False)
        embed.add_field(name="Welcome", value="`!setwelcome`, `!removewelcome`", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
