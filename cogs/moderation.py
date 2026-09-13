import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a member from the server"""
        if member == ctx.author:
            await ctx.send("You can't kick yourself!")
            return
        
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="Member Kicked",
                description=f"{member.mention} has been kicked.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to kick this member.")

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban a member from the server"""
        if member == ctx.author:
            await ctx.send("You can't ban yourself!")
            return
        
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Member Banned",
                description=f"{member.mention} has been banned.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to ban this member.")

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Unban a member from the server"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
        
        await ctx.send("That member is not banned or was not found.")

    @commands.command(name='mute')
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, duration: int = 60, *, reason=None):
        """Mute a member for a specified duration (in seconds)"""
        if member == ctx.author:
            await ctx.send("You can't mute yourself!")
            return
        
        try:
            await member.timeout(discord.utils.utcnow() + discord.utils.timedelta(seconds=duration), reason=reason)
            embed = discord.Embed(
                title="Member Muted",
                description=f"{member.mention} has been muted for {duration} seconds.",
                color=discord.Color.orange()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permission to mute this member.")

    @commands.command(name='unmute')
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: discord.Member):
        """Unmute a member"""
        try:
            await member.timeout(None)
            await ctx.send(f'{member.mention} has been unmuted.')
        except discord.Forbidden:
            await ctx.send("I don't have permission to unmute this member.")

    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = 10):
        """Delete a specified number of messages"""
        if amount < 1 or amount > 100:
            await ctx.send("Please specify a number between 1 and 100.")
            return
        
        deleted = await ctx.channel.purge(limit=amount + 1))
        await ctx.send(f'Deleted {len(deleted) - 1} messages.', delete_after=5)

    @commands.command(name='warn')
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        """Warn a member"""
        embed = discord.Embed(
            title="Member Warned",
            description=f"{member.mention} has been warned.",
            color=discord.Color.yellow()
        )
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Warned by", value=ctx.author.mention, inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
