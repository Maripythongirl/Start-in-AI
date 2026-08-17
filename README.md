🤖 Bot Discord com IA 🤖

Um bot multifuncional para Discord: 
Desenvolvido em Python, que combina comandos de diversão e utilidades com IA.

✨ Funcionalidades ✨

COMANDOS:
$hello — envia uma mensagem de boas-vindas.
$heh — gera uma sequência de "he".
$senha — gera uma senha aleatória.
$emoji — envia um emoji aleatório.
$moeda — realiza um lançamento de moeda.
$entrada — informa quando um membro entrou no servidor.
$google <pesquisa> — cria um botão para pesquisar no Google.
$editme — demonstra a edição de uma mensagem.
$meme — envia um meme aleatório da pasta de imagens.
$duck — envia uma imagem aleatória de pato.
$brother — realiza uma interação especial com o usuário.
$papai — envia uma homenagem acompanhada de um vídeo.
$salvar — utiliza Inteligência Artificial para analisar uma imagem e criar uma carta de personagem.

🖼️ CAPTURAS DE TELA 🖼️
<p align="center">
  <img src="imagens/comandos.png" width="400">
</p>



🧠 CLASSIFICAÇÃO COM IA 🧠
O comando $salvar é a principal funcionalidade de IA do projeto.

1- O usuário envia uma imagem junto com o comando. O bot verifica se existe um arquivo anexado e se ele é realmente uma imagem. Em seguida, a imagem é salva localmente com um nome único.

2- O bot utiliza o modelo 'modelo/keras_model.h5' e o arquivo 'modelo/labels.txt' para realizar a classificação da imagem.

3- A função responsável pela classificação carrega o modelo .h5, lê os nomes das classes e prepara a imagem para ser utilizada pela rede neural.

4- A imagem é ajustada para 224 × 224 pixels, convertida para um array NumPy e normalizada antes de ser enviada ao modelo.

5- Após a previsão, o modelo seleciona a classe com maior probabilidade e retorna o resultado.

🃏 CARTAS DE RPG 🃏

Atualmente, o bot trabalha com cinco classes:

🐶 Cachorro 🐶
🐱 Gato 🐱
🪖 Soldado 🪖
👸 Princesa 👸
🐉 Dragão 🐉

Depois que a IA identifica uma classe, o bot escolhe aleatoriamente características correspondentes àquela classe.

Por exemplo, um Cachorro pode receber diferentes poderes, funções e habilidades, além de valores aleatórios de vida, ataque e defesa.

O mesmo sistema é utilizado para Gato, Soldado, Princesa e Dragão.

A carta gerada contém:

👤 Nome 👤
🔥 Poder 🔥
🛡️ Função 🛡️
📖 História 📖
🛡️ Classe 🛡️
❤️ Vida ❤️
⚔️ Ataque ⚔️
🛡️ Defesa 🛡️
✨ Habilidade ✨
⭐ Raridade ⭐

Os valores de vida, ataque e defesa são sorteados dentro de intervalos definidos para cada classe, enquanto a raridade pode ser Comum, Incomum, Raro, Épico ou Lendário.

⚙️ TECNOLOGIAS UTILIZADAS ⚙️
Python
Discord.py
TensorFlow / tf-keras
Keras
Pillow
NumPy
Requests

👩‍💻 AUTORA - MARIANA 👩‍💻
Projeto desenvolvido como uma experiência de aprendizado em Python, Discord Bots e IA.
