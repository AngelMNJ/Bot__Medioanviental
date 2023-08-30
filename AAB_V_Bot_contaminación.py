import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

lista_amarillo = ['envases de plástico', 'botella de agua', 'bote de champú', 'bote de yogurt', 'bolsa de plástico', 'bandeja de corcho', 'plastico', 'lata de metal', 'lata de refresco', 'lata de cerveza', 'brik de leche', 'zumos', 'desodorante', 'tapa de plástico', 'papel', 'cartón', 'envase', 'envoltorio metálico', 'papel de aluminio']
lista_azul = ['cajas de zapatos', 'cajas de cereales', 'cajas de galletas', 'rollos de cartón de papel higiénico', 'rollos de cartón de cocina', 'cajas de pizza', 'periódicos', 'revistas', 'catálogos', 'folletos', 'libros', 'cuadernos', 'libretas', 'hojas sueltas', 'sobres', 'fotocopias', 'bolsas de papel', 'cajas de cartón corrugado', 'cajas de cartón ondulado', 'cajas de cartón', 'papel de envolver', 'papel de escribir', 'papel de imprimir', 'cartulinas', 'cartones', 'rollos de papel de cocina', 'rollos de papel de envolver']
lista_gris = ['bricks', 'platos', 'tazas', 'vasos', 'botellas de cristal', 'frascos de cosméticos', 'frascos de perfume', 'espejos, bombillas', 'cerámica, loza', 'vidrio plano', 'vitrocerámica', 'cristalería']
lista_marrón = ['comida', 'restos de fruta', 'verdura', 'carne', 'pescado', 'marisco', 'huesos', 'cáscaras de huevo', 'posos de café', 'bolsitas de infusiones', 'papel de cocina', 'servilletas de papel', 'tapones de corcho', 'pelo', 'plumas', 'ceniza de la chimenea']
lista_verde = ['botellas de vidrio', 'botellas de vidrio de vino', 'botellas de vidrio de licores', 'botellas de vidrio de aceite', 'frascos de vidrio de mermeladas y conservas', 'frascos de perfume de vidrio', 'frascos de colonias de vidrio', 'tarros de cosméticos de vidrio']
lista_ropa = ['camisas', 'pantalones', 'faldas', 'vestidos', 'chaquetas', 'abrigos', 'jerseys', 'trajes', 'calzoncillos', 'calcetines', 'pijamas', 'sábanas, toallas', 'cortinas', 'manteles', 'zapatos', 'cinturones', 'bolsos', 'mochilas']


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')

@bot.command()
async def donde_va(ctx, item: str):
  if item in lista_amarillo:
    await ctx.send('It goes in the yellow bin')
  elif item in lista_azul:
    await ctx.send('It goes in the blue bin')
  elif item in lista_gris:
    await ctx.send('It goes in the grey bin')
  elif item in lista_marrón:
    await ctx.send('It goes in the brown bin')
  elif item in lista_verde:
    await ctx.send('It goes in the green bin')
  elif item in lista_ropa:
    await ctx.send('It goes in the rope bin')
  else:
    await ctx.send('Ponlo en minuscula, cambia de plural a sngular o al reves y si sigue sin funcionar no se que es')

bot.run('MTEwMTIwNTk4MDE1NjUzMDcxOQ.G5DtEY.VzIoofv3CtMBEgJ2swsrzYDf4aE6WLnbCNzjvU')