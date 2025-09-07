# Passo a passo

### 1. Instalar e configurar o Ollama
O Ollama é o servidor que roda o modelo de linguagem (LLM) responsável por gerar embeddings.

- Baixe e instale o Ollama: https://ollama.com/download
- Após a instalação, execute:

```bash
# Inicia o servidor Ollama
ollama serve

# Baixa o modelo de embeddings usado pelo projeto
ollama pull nomic-embed-text:latest
```

Recomenda-se criar e ativar um ambiente virtual antes de instalar dependências.
```
# Criar o ambiente virtual
python -m venv .venv

# Ativação (Mac / Linux)
source .venv/bin/activate

# Com o venv ativado
pip install -r requirements.txt
```

Execute
```
python3 main.py
```