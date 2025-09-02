# Uso de Linters em Python com Flake8

## 1. Instalação da Ferramenta
O **Flake8** é um dos linters mais populares para Python e ajuda a manter a qualidade do código seguindo padrões de estilo.

Instalação via **pip**:
```bash
pip install flake8
```

Para a formatação automática (topico: 3), usaremos o **Black**:
```bash
pip install black
```

---

## 2. O que é o Flake8
O **Flake8** na verdade funciona como um “wrapper” que combina várias bibliotecas de análise de código Python.
As principais bibliotecas que ele utiliza são:

- PyFlakes → faz análise estática de código para identificar erros como variáveis não utilizadas, importações desnecessárias ou variáveis não definidas.
- pycodestyle (antigo pep8) → verifica se o código segue as regras de estilo da PEP 8.
- McCabe → calcula a complexidade ciclomática do código (mede o número de caminhos lógicos dentro de funções/métodos).

## 2. Integração com o Ambiente de Desenvolvimento
- **VS Code**: 
    - instalar a extensão *Python* e configurar para usar o Flake8.
    - Vá em **Configurações** → Pesquise por **linting** → Habilite **Flake8**

- **Linha de comando**:
  ```bash
  flake8 nome_do_arquivo.py
  ```

---

## 3. Estilização Automática
O Flake8 apenas **aponta problemas**, mas não os corrige automaticamente. Para corrigir automaticamente, usamos o **Black**:
```bash
black nome_do_arquivo.py
```
Isso ajusta automaticamente o código para seguir o guia de estilo PEP 8

---

## 4. Guia de Estilo Utilizado no Python
- **PEP 8**: guia oficial de estilo do Python.

---

## 5. Configurando regras de estilo no Flake8
no arquivo `.flake8` ou `setup.cfg`:

```ini
[flake8]
max-line-length = 88
ignore = E203, W503
max-complexity = 10
```
1. **max-line-length**: define o tamanho máximo de caracteres por linha (ex: 79 ou 88).
2. **ignore**: permite ignorar regras específicas (ex: E203 – espaços antes de dois pontos).
3. **max-complexity**: controla a complexidade ciclomática (quantidade de caminhos lógicos em funções).

---

## 6. Exemplo de Código
### Código Original (não formatado):
```python
def soma (a,b): return a+b


print(soma(2,3))
```

```sh
exemplo.py:1:1: E704 multiple statements on one line (def)
exemplo.py:1:9: E211 whitespace before '('
exemplo.py:1:12: E231 missing whitespace after ','
exemplo.py:1:21: E501 line too long (26 > 20 characters)
exemplo.py:1:25: E226 missing whitespace around arithmetic operator
exemplo.py:4:13: E231 missing whitespace after ','
exemplo.py:4:17: W292 no newline at end of file
```

### Erros apontados pelo Flake8:
- Espaço desnecessário após o nome da função.
- Uso de `return` na mesma linha da definição.
- Linhas em branco extras.


### Código Corrigido pelo Black:
```python
def soma(a, b):
    return a + b


print(soma(2, 3))
```

# Aprensentação
https://gamma.app/docs/Padronizacao-de-Codigo-Python-Linter-e-Formatador-em-Acao-fizyv5cxwrob381?mode=doc
