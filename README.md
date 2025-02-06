# YouTube Video Downloader

Este projeto é um script em Python que permite baixar vídeos do YouTube diretamente para a sua máquina utilizando a biblioteca `yt-dlp`.

## 🚀 Funcionalidades
- Download de vídeos do YouTube
- Suporte a diferentes formatos e qualidades
- Fácil de usar

## 📦 Dependências
Para rodar o projeto, você precisa das seguintes bibliotecas:

- `yt-dlp`

## 📥 Instalação
Antes de executar o script, instale as dependências necessárias rodando o seguinte comando:

```bash
pip install yt-dlp
```

Se estiver utilizando um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate  # No Windows
pip install yt-dlp
```

## ▶️ Como Usar
1. Certifique-se de ter o Python instalado.
2. Execute o script com o comando:

```bash
python ytDownload.py
```

3. Insira a URL do vídeo do YouTube quando solicitado.
4. O vídeo será baixado para a pasta do projeto.

## 🛠 Possíveis Problemas
Se receber um erro de módulo não encontrado, tente reinstalar a biblioteca:

```bash
pip install --upgrade yt-dlp
```

Caso o download falhe, atualize o `yt-dlp` com:

```bash
yt-dlp -U
```

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!

---
Feito com ❤️ por [Ygor Gomes]

