# Chatbot de Suporte para ConquisTI

Este projeto implementa um chatbot simples e funcional que atua como atendente de suporte para o blog de tecnologia **ConquisTI**. O chatbot responde a dúvidas comuns dos usuários, como instruções para fazer login, postar ou editar artigos, e fornece suporte técnico quando necessário.

## Interface

<div align="center">
  <img src="img/logo.png" alt="Imagem do Projeto" width="100">
</div>

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Como Usar](#como-usar)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição

Este projeto utiliza Python para implementar um chatbot que responde a perguntas comuns sobre o blog ConquisTI. As respostas são baseadas em um arquivo de intenções JSON, que contém padrões de perguntas e respostas predefinidos. O chatbot também utiliza a biblioteca **difflib** para identificar padrões similares e melhorar a precisão na detecção das intenções.

## Funcionalidades

- Responde a perguntas sobre:
  - Como fazer login.
  - Como postar artigos no blog.
  - Como editar artigos publicados.
  - Suporte técnico para problemas no site.
- Detecta padrões similares usando **difflib**.
- Permite fácil expansão das intenções e respostas.

## Explicação

O chatbot funciona da seguinte maneira:
1. Recebe a entrada do usuário.
2. Procura correspondências exatas ou similares nas perguntas predefinidas no arquivo `intents.json`.
3. Retorna uma resposta apropriada com base na intenção identificada.

Caso não encontre uma correspondência, o chatbot retorna uma mensagem genérica solicitando ao usuário que reformule a pergunta.

## Como Usar

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-suporte-conquisti.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd chatbot-suporte-conquisti
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o chatbot:
   ```bash
   python main.py
   ```

6. Interaja com o chatbot no terminal, fazendo perguntas sobre as funcionalidades do blog.

## Autor

Desenvolvido por Diego Franco

