 Curso Python Mundo 1

# Aula 06 - Tipos Primitivos
- int
- float
- boolean
- str

# Aula 07 - Operadores Aritméticos
### Tipos de operadores:
  - adicao +
  - substracao -
  - multiplicacao *
  - divisao /
  - potencia **
  - divisao inteira //
  - resto da divisao %
  
###   Ordem de precediencia dos operadores:
  1. `()`
  2. `**`
  3. `*` `/` `//` `%`
  4. `+`  `-`

# Aula 08 - Utilizando Módulos
Dica: pra ver as opcoes do import basta colocar import e ctrl+space

Bonus: biblioteca pra emoji hahahhaha
   
```python
import emoji
    print(emoji.emojize('ola :earth_americas:', use_aliases=True))
```

# Aula 09 - Manipulando Cadeias de Texto
Operações com string:
`Frase de exemplo: frase = "curso em video python" 21 chars (de 0 a 20)`

1. Fatiamento:
    - `frase[9]` >>> 'v' (mostra o char de index 9 na string)
    - `frase[9:13]` >>> 'vide' (mostra os chars de index 9 a 12 - ele reduz 1 da última coordenada)
    - `frase[9:21:2]` >>> 'vdopto' (mostra os chars de index 9 a 20 pulando de 2 em 2)
    - `frase[:5]` >>> 'curso' (mostra os chars de index 0 a 4)
    - `frase[15:]` >>> 'python' (mostra os chars de index 15 até o final)
    - `frase[9::3]` >>> 'veph' (mostra os chars do index 9 até o final pulando de 3 em 3)

2. Análise
      - `len(frase)` >>> 21 (mostra a quantidade de chars na string)
      - `frase.count('0',0,13)` >>> 1 (mostra a quantidade de chars 'o' na string já fatiando nos index de 0 a 12)
      - `frase.find('deo')` >>> 11 (mostra o index da primeira letra do find)
      - `frase.find('android')` >>> -1 (indica que essa string não existe na string pesquisada)
      - `'curso' in frase` >>> True (mostra se tem 'curso' na string)

3. Transformação
      - `frase.replace('python','android')` >>> 'curso em video android'
      - `frase.upper()` >>> 'CURSO EM VIDEO PYTHON'
      - `frase.lower()` >>>> 'curso em video python'
      - `frase.capitalize()` >>> 'Curso em video python'
      - `frase.title()` >>> 'Curso em Video Python' (primeiras letras em upper)
      - `frase.strip()` >>> 'curso em video' (remove os espaços inúteis no começo e no final da string)
      - `frase.rstrip()` >>> 'curso em video' (remove os espaços inúteis no final da string - ATENCAO A ESSA LOGICA DO R)
      - `frase.lstrip()` >>> 'curso em video' (remove os espaços inúteis no começo da sting - ATENCAO A ESSA LOGICA DO L)

4. Divisão
   - `frase.split()` >>> ['curso','em','video','python'] (separa uma string em outras usando o espaço - mas pode ser outro char)
   -  `'-'.join(frase.split())` >>> 'curso-em-video-python' 



# Aula 10 - Condições

```python
if condicao == True:
    bloco True
  else:
    bloco False
```
ou
```python
print('True' if condicao == True else 'False') # esse metodo é meio ruim
```

# Aula 11 - Cores no Terminal
ANSI - Escape Sequence

`\033[ estilo; texto; backgroud m "o texto vai depois desse código"`

Isso mesmo, abre com \033[ e feixa com 'm'

Exemplo:
  `print("\033[0;33;44mOlá, Mundo")` >>> nada de estilo + texto amarelo + bg azul

Opções:
  - Estilo
  - Texto
  - Backgroud

---

<div align='center'>

| Estilo    | Código |
|-----------|--------|
| nada      | 0      |
| bold      | 1      |
| underline | 2      |
| negative  | 3      |

</div>

---

<div align='center'>

| Texto  | Código |
|--------|--------|
| white  | 30     |
| red    | 31     |
| gree   | 32     |
| yellow | 33     |
| blue   | 34     |
| purple | 35     |
| cian   | 36     |
| gray   | 37     |

</div>

---

<div align='center'>

| Background | Código |
|------------|--------|
| white      | 40     |
| red        | 41     |
| gree       | 42     |
| yellow     | 4      |
| blue       | 44     |
| purple     | 45     |
| cian       | 46     |
| gray       | 47     |

</div>

---

Da pra criar um dicionario pra facilitar o código:
  
```python
cores = {
    'limpa' : '\033[m',
    'azul' : '\033[34m'
  }
```


  depois é só usar `cores['limpa']`

  