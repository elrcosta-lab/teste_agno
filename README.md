# Projeto Teste AGNO

Este é um projeto de demonstração que utiliza a biblioteca AGNO para criar um agente de pesquisa que responde perguntas dos usuários pesquisando na web com DuckDuckGo.

## Descrição

O projeto consiste em um agente de inteligência artificial chamado "Pesquisador DDG" que:
- Pesquisa na web usando DuckDuckGo para responder perguntas dos usuários
- Busca as principais fontes confiáveis sobre o tema
- Entrega uma saída concisa com 5-10 fatos em bullets e um quadro de fontes com título e URL
- Não inventa links, priorizando sites oficiais, artigos e referências robustas

## Tecnologias Utilizadas

- Python 3.12+
- Biblioteca AGNO
- OpenAI GPT-4o-mini
- DuckDuckGo Tools
- FastAPI (para o servidor web)

## Arquitetura

O projeto contém dois arquivos principais:

1. **main.py**: Executa o agente localmente, fazendo uma pesquisa sobre as principais novidades da inteligência artificial
2. **server.py**: Configura um servidor web com o AgentOS para disponibilizar o agente como um serviço

## Configuração e Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Uma chave de API da OpenAI

### Instalação

1. Clone este repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   Ou, se estiver usando Poetry:
   ```bash
   poetry install
   ```

### Configuração

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   OPENAI_API_KEY=sua_chave_de_api_aqui
   ```

## Uso

### Execução Local

Para executar o agente localmente com uma pergunta padrão:

```bash
python main.py
```

### Execução como Serviço Web

Para executar o servidor web com o agente:

```bash
python server.py
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NomeDaFeature`)
3. Faça commit de suas alterações (`git commit -m 'Adiciona NomeDaFeature'`)
4. Faça push para a branch (`git push origin feature/NomeDaFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autores

- [Seu Nome] - Desenvolvedor Principal

## Agradecimentos

- À comunidade AGNO por fornecer a biblioteca que torna este projeto possível