import discord
from discord.ext import commands
import requests
import random as ran

print('bot')


class Neko:
    @staticmethod
    def nekoImg():
        r = requests.get('https://nekos.life/api/v2/img/neko')
        return r.json()['url']

    @staticmethod
    def nekoget():
        r = requests.get("https://neko-love.xyz/api/v1/neko")
        if r.status_code != 200:
            return None
        else:
            return r.json()["url"]


class NekoBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def neko(self, ctx):
        nekoUrl = Neko.nekoImg()
        embed = discord.Embed(color=0x2F3136)  # Создание Embed'a
        embed.set_image(url=nekoUrl)  # Устанавливаем картинку Embed'a
        await ctx.send(embed=embed)  # Отправляем Embed
        print(nekoUrl)

    @commands.command()
    async def newneko(self, ctx):
        nekoUrl = Neko.nekoget()
        embed = discord.Embed(color=0x2F3136)  # Создание Embed'a
        embed.set_image(url=nekoUrl)  # Устанавливаем картинку Embed'a
        await ctx.send(embed=embed)  # Отправляем Embed
        print(nekoUrl)

    @commands.command(pass_content=True)
    async def random(self, ctx, msg=None):
        YES = ran.randint(0, 1)
        embed = discord.Embed(color=0x2F3136)  # Создание Embed'a
        msgs = {
            'coin': ['Выпала решка', 'Выпал орёл'],
            'пидр': ['Ты пидр, пидарок, пидарас!', 'Ты не пидр ахахах'],
            'кс': ['Иди гамай в кс го даун', 'Сохрани свой мозг'],
        }
        print(msg)
        try:
            if msg != None:
                if msg == 'help':
                    keys = msgs.keys()
                    strkeys = '''ВОТ СПИСОК КОММАНД'''
                    for i in keys:
                        strkeys += str(i), '\n'
                    embed.set_footer(text=strkeys)
                else:
                    embed.set_footer(text=msgs[msg][YES])
            else:
                embed.set_footer(text=msgs['coin'][YES])
        except KeyError:
            embed.set_footer(text='НЕВЕРНАЯ КОМАНДА ДАУН')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(NekoBot(bot))
