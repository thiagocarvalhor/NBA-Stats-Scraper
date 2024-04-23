# NBA Stats Scraper

Este é um script em Python para extrair dados estatísticos dos jogadores da NBA a partir do site oficial da NBA Stats (https://www.nba.com/stats/players/traditional).

## Variáveis Extraídas

O script extrai as seguintes variáveis para cada jogador listado:

- **PLAYER (Jogador):** Nome do jogador.
- **TEAM (Time):** Time ao qual o jogador pertence.
- **AGE (Idade):** Idade do jogador.
- **GP (Games Played):** Número de jogos em que o jogador participou.
- **W (Wins):** Número de vitórias do time com o qual o jogador está associado.
- **L (Losses):** Número de derrotas do time com o qual o jogador está associado.
- **MIN (Minutes):** Minutos jogados pelo jogador.
- **PTS (Points):** Pontos marcados pelo jogador.
- **FGM (Field Goals Made):** Número de arremessos de campo convertidos.
- **FGA (Field Goals Attempted):** Número de tentativas de arremessos de campo.
- **FG% (Field Goal Percentage):** Percentual de arremessos de campo convertidos.
- **3PM (3-Point Field Goals Made):** Número de arremessos de 3 pontos convertidos.
- **3PA (3-Point Field Goals Attempted):** Número de tentativas de arremessos de 3 pontos.
- **3P% (3-Point Field Goal Percentage):** Percentual de arremessos de 3 pontos convertidos.
- **FTM (Free Throws Made):** Número de lances livres convertidos.
- **FTA (Free Throws Attempted):** Número de tentativas de lances livres.
- **FT% (Free Throw Percentage):** Percentual de lances livres convertidos.
- **OREB (Offensive Rebounds):** Número de rebotes ofensivos.
- **DREB (Defensive Rebounds):** Número de rebotes defensivos.
- **REB (Total Rebounds):** Total de rebotes (ofensivos + defensivos).
- **AST (Assists):** Número de passes que resultam em cestas feitas por um companheiro de equipe.
- **TOV (Turnovers):** Número de vezes que o jogador perde a posse de bola para o outro time.
- **STL (Steals):** Número de vezes que o jogador rouba a bola do adversário.
- **BLK (Blocks):** Número de vezes que o jogador bloqueia um arremesso do adversário.
- **PF (Personal Fouls):** Número de faltas pessoais cometidas pelo jogador.
- **FP (Fantasy Points):** Pontuação utilizada em ligas de fantasia.
- **DD2 (Double Doubles):** Número de jogos em que o jogador atingiu dois dígitos em dois dos cinco principais estatísticas - pontos, rebotes, assistências, roubos de bola e bloqueios.
- **TD3 (Triple Doubles):** Número de jogos em que o jogador atingiu dois dígitos em três dos cinco principais estatísticas - pontos, rebotes, assistências, roubos de bola e bloqueios.
- **+/- (Plus-Minus):** A diferença de pontos marcados pelo time enquanto o jogador está em quadra e os pontos permitidos pelo time enquanto o jogador está em quadra.

## Temporada

- **SEASON (Temporada):** 2023-24
- **SEASON TYPE (Tipo de Temporada):** Regular Season
- **PER MODE (Modo):** Per Game
- **SEASON SEGMENT (Segmento da Temporada):** All Season Segments

## Requisitos

Para executar este script, é necessário ter o Python instalado, bem como as seguintes bibliotecas:

- pandas
- selenium

Além disso, é necessário baixar o driver do navegador Chrome (ChromeDriver) e configurar o caminho correto no script.

## Uso

Para executar o script, basta chamar a função `nbastats` passando a URL da página da NBA Stats como argumento. Por exemplo:

```python
results = nbastats('https://www.nba.com/stats/players/traditional')

## Sobre o Autor
Saiba mais sobre o autor deste projeto:
- [Thiago Ribeiro](https://www.linkedin.com/in/thiago-carvalho-ribeiro-a7ba64208/)
