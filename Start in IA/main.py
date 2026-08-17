import discord
import random
import asyncio
import os
import requests
import uuid
from urllib.parse import quote_plus
from discord.ext import commands
from comandos import get_class


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

class Google(discord.ui.View):
    def __init__(self, query: str):
        super().__init__()

        query = quote_plus(query)
        url = f'https://www.google.com/search?q={query}'

        self.add_item(discord.ui.Button(label="Pesquisar no Google 🔎", url=url))
# -------- Funções --------

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "cara"
    else:
        return "coroa"

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

# -------- Eventos --------

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')
    print('---------------------------------------')

# evento que detecta edição de mensagem
@bot.event
async def on_message_edit(before, after):
    msg = f'**{before.author}** editou a mensagem:\n{before.content} -> {after.content}'
    await before.channel.send(msg)
# -------- Comandos --------

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! Eu sou um bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def senha(ctx):
    await ctx.send(gen_pass(10))


@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())


@bot.command()
async def moeda(ctx):
    await ctx.send(flip_coin())


@bot.command()
async def entrada(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} entrou {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def google(ctx, *, pesquisa: str):
    await ctx.send(f'Resultado da busca para: `{pesquisa}`', view=Google(pesquisa))

@bot.command()
async def editme(ctx):
    msg = await ctx.send('10')
    await asyncio.sleep(3.0)
    await msg.edit(content='40')

@bot.command()
async def meme(ctx):
    memes = os.listdir("images")
    aleatorio = random.choice(memes)
    await ctx.send(file = discord.File(f"images/{aleatorio}"))


@bot.command('duck')
async def duck(ctx):
    #Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url
    image_url = get_duck_image_url()
    await ctx.send(image_url)


#specialbrother
@bot.command()
async def brother(ctx):
    await ctx.send("Paulo ou Rodrigo?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        resposta = await bot.wait_for('message', timeout=15.0, check=check)

        escolha = resposta.content.lower()

        if escolha == "paulo":
            await ctx.send("Homenagem ao Paulo 💙")
            await ctx.send(file=discord.File("brothers/paulo.mp4"))

        elif escolha == "rodrigo":
            await ctx.send("Homenagem ao Rodrigo 💙")
            await ctx.send(file=discord.File("brothers/ze.mp4"))

        else:
            await ctx.send("Escolha inválida 😅 Digite 'Paulo' ou 'Rodrigo'.")

    except asyncio.TimeoutError:
        await ctx.send("Você demorou para responder 😢")


@bot.command()
async def papai(ctx):

    await ctx.send(
        "💙 Papai...\n"
        "Essa é uma pequena homenagem para alguém tão importante.\n"
        "Obrigada por todas as experiências e memórias que vivemos juntos!\n"
        "Que Deus te abençoe muitooooo.\n"
        "Te amo muitooo, mesmo você sendo enjoado XD.\n"
        "Xoxo,\n"
        "Mari bebê"
    )

    await ctx.send("🎬 Agora um vídeo fofo com a NOSSA música! nhenhenhenhenhe🎬")
    await ctx.send(file=discord.File("papai/papai.mp4"))

@bot.command()
async def salvar(ctx):

    # Verifica se existe algum arquivo anexado
    if len(ctx.message.attachments) == 0:
        await ctx.send("❌ Você não enviou nenhuma imagem!")
        return

    attachment = ctx.message.attachments[0]

    # Verifica se o arquivo é uma imagem
    if not attachment.content_type or not attachment.content_type.startswith("image/"):
        await ctx.send("❌ O arquivo enviado não é uma imagem!")
        return

    # Cria a pasta caso ela não exista
    os.makedirs("imagens", exist_ok=True)

    # Gera um nome único
    extensao = os.path.splitext(attachment.filename)[1]
    nome_arquivo = f"{uuid.uuid4()}{extensao}"

    caminho = os.path.join("imagens", nome_arquivo)

    # Salva a imagem
    await attachment.save(caminho)

    await ctx.send("🤖 Analisando sua imagem...")

    # -----------------------------
    # IA CLASSIFICANDO A IMAGEM
    # -----------------------------

    classe = get_class(
        "modelo/keras_model.h5",
        "modelo/labels.txt",
        caminho
    )

    print("Classe identificada:", classe)

    # Limpa o nome da classe
    classe = str(classe).strip()

    # Remove o número do início caso exista
    # Exemplo: "0 Cachorro" → "Cachorro"
    #          "1 Gato"     → "Gato"
    if " " in classe:
        partes = classe.split(" ", 1)

        if partes[0].isdigit():
            classe = partes[1]

    print("Classe identificada após correção:", classe)
    
    # -----------------------------
    # DADOS DOS PERSONAGENS
    # -----------------------------

    personagens = {
        "Cachorro": {
            "poderes": ["Uivo Supremo", "Mordida Sombria", "Fúria Canina"],
            "funcoes": ["Guardião", "Caçador", "Companheiro"],
            "habilidades": ["Faro Aguçado", "Uivo Poderoso", "Investida Canina"],
            "vida": (700, 950),
            "ataque": (60, 85),
            "defesa": (65, 90)
        },

        "Gato": {
            "poderes": ["Sombra Felina", "Garras Lunares", "Olhar Hipnótico"],
            "funcoes": ["Espião", "Assassino", "Explorador"],
            "habilidades": ["Ataque Surpresa", "Passos Silenciosos", "Salto Felino"],
            "vida": (500, 800),
            "ataque": (65, 90),
            "defesa": (45, 75)
        },

        "Soldado": {
            "poderes": ["Ataque Tático", "Força Militar", "Golpe de Aço"],
            "funcoes": ["Guerreiro", "Protetor", "Comandante"],
            "habilidades": ["Ataque Estratégico", "Defesa Tática", "Contra-Ataque"],
            "vida": (750, 950),
            "ataque": (70, 90),
            "defesa": (70, 90)
        },

        "Princesa": {
            "poderes": ["Encanto Real", "Luz Imperial", "Magia Real"],
            "funcoes": ["Líder", "Curandeira", "Maga"],
            "habilidades": ["Cura Real", "Proteção Mágica", "Comando Imperial"],
            "vida": (600, 850),
            "ataque": (50, 80),
            "defesa": (60, 85)
        },

        "Dragão": {
            "poderes": ["Chama Ancestral", "Fogo Celestial", "Inferno Dragônico"],
            "funcoes": ["Guardião das Terras Mágicas", "Destruidor", "Guardião Ancestral"],
            "habilidades": ["Fúria Flamejante", "Sopro de Fogo", "Meteoro"],
            "vida": (850, 1000),
            "ataque": (85, 100),
            "defesa": (75, 100)
        }
    }

    # -----------------------------
    # CRIAÇÃO DO PERSONAGEM
    # -----------------------------

    if classe not in personagens:
        await ctx.send(f"❌ A IA identificou uma classe desconhecida")
        return

    personagem = personagens[classe]

    nomes = {
        "Cachorro": ["Thor", "Max", "Bolt", "Rex"],
        "Gato": ["Luna", "Mia", "Shadow", "Nina"],
        "Soldado": ["Marcus", "Arthur", "Leon", "Victor"],
        "Princesa": ["Aurora", "Sofia", "Elena", "Amélia"],
        "Dragão": ["Ignis", "Draco", "Fênix", "Azir"]
    }

    nome = random.choice(nomes[classe])
    poder = random.choice(personagem["poderes"])
    funcao = random.choice(personagem["funcoes"])
    habilidade = random.choice(personagem["habilidades"])

    vida = random.randint(*personagem["vida"])
    ataque = random.randint(*personagem["ataque"])
    defesa = random.randint(*personagem["defesa"])

    raridades = [
        "Comum",
        "Incomum",
        "Raro",
        "Épico",
        "Lendário"
    ]

    raridade = random.choice(raridades)

    # -----------------------------
    # HISTÓRIA
    # -----------------------------

    historias = {
        "Cachorro": f"{nome} é um fiel guardião que percorre as terras mágicas protegendo aqueles que precisam de ajuda.",

        "Gato": f"{nome} é uma criatura misteriosa que se move pelas sombras e conhece segredos que ninguém mais conhece.",

        "Soldado": f"{nome} é um guerreiro treinado que jurou proteger o reino contra qualquer ameaça.",

        "Princesa": f"{nome} é uma princesa poderosa que utiliza sua magia para proteger seu povo e manter a paz.",

        "Dragão": f"{nome} é um antigo dragão responsável por proteger as Terras Mágicas contra criaturas que ameaçam o reino."
    }

    historia = historias[classe]

    # -----------------------------
    # CARTA
    # -----------------------------

    carta = f"""
🐉 **PERSONAGEM CRIADO!**

👤 **Nome:** {nome}
🔥 **Poder:** {poder}
🛡️ **Função:** {funcao}

📖 **História:**
{historia}

🛡️ **Classe:** {classe}
❤️ **Vida:** {vida}
⚔️ **Ataque:** {ataque}
🛡️ **Defesa:** {defesa}
✨ **Habilidade:** {habilidade}
⭐ **Raridade:** {raridade}
"""

    await ctx.send(carta)


bot.run("")