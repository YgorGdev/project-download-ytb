YouTube Video Downloader

Este projeto é um script em Python que permite baixar vídeos do YouTube diretamente para a sua máquina utilizando a biblioteca yt-dlp.

🚀 Funcionalidades

Download de vídeos do YouTube

Suporte a diferentes formatos e qualidades

Fácil de usar

📦 Dependências

Para rodar o projeto, você precisa das seguintes bibliotecas:

yt-dlp

📥 Instalação

Antes de executar o script, instale as dependências necessárias rodando o seguinte comando:

pip install yt-dlp

Se estiver utilizando um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate  # No Windows
pip install yt-dlp

▶️ Como Usar

Certifique-se de ter o Python instalado.

Execute o script com o comando:

python ytDownload.py

Insira a URL do vídeo do YouTube quando solicitado.

O vídeo será baixado para a pasta do projeto.

🛠 Possíveis Problemas

Se receber um erro de módulo não encontrado, tente reinstalar a biblioteca:

pip install --upgrade yt-dlp

Caso o download falhe, atualize o yt-dlp com:

yt-dlp -U

📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!

Feito com ❤️ por [Seu Nome]
