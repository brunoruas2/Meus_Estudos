# -*- coding: utf-8 -*-
import re

string = r'''
\begin{chapquote}{página 65}
	``Counting can become quite subtle, and in this chapter we explore some of its more sophisticated aspects. Our goal is still to answer the question 'How many?' but we introduce mathematical techniques that bypass the actual process of counting individual objects''
\end{chapquote}

\section{Listas}
Uma \textbf{lista} é uma sequência ordenada de objetos. Esses objetos são mantidos entre um par de parênteses e separados por vírgulas. Os objetos dentro de uma lista são chamados de \textbf{entradas}\footnote{Do original, \textbf{entries}}. Já que uma lista é uma sequência ordenada, é evidente que a ordem dos seus elementos é suficiente para distinguir listas que contenham os mesmo objetos.

$$ (a,b,c) \neq (c,b,a) $$

\textbf{Comentário}: Também é comum escrever uma lista sem os parênteses e as vírgulas. Esse formato de escrita se chama \textbf{string}. Nesse caso $(a,b,c)$ é a mesma coisa de $abc$. Essa outra maneira só é usada quando não há risco de confusão entre as entradas da lista. Fica ligado e mantém essas duas formas de escrita como padrão.
\\
\\
Como já vimos conjuntos no capítulo 01, podemos usá-los para comparação. No caso dos conjuntos a ordem dos elementos não importa na comparação. Ou seja, $\{a,b,c\} = \{c,b,a\}$. Já vimos acima que essa propriedade não é mantida nas listas. 
\\
\\
Diferentemente dos conjuntos, uma lista pode ter entradas repetidas sem nenhum problema. A lista $(a,a,a,a,b)$, por exemplo, é perfeitamente aceitável.
\\
\\
Tal qual a cardinalidade dos conjuntos, nós contamos quantas entradas existem em uma lista. Chamamos essa medida de \textbf{comprimento}. A lista $(a,a,a,a,b)$ possui um comprimento de 5.
\\
\\
\textbf{Regra}: Duas listas são \textbf{iguais} se possuírem exatamente as mesmas entradas nas mesmas posições. Ou seja, também possuem o mesmo comprimento.
\\
\\
Só existe uma lista cujo comprimento é igual a zero. Denominamos essa lista de \textbf{lista vazia}. Denotada por $()$.\footnote{Sim, lembra muito o conceito de conjunto vazio.}

\section{O Princípio da Multiplicação}

Existem muitos problemas práticos que envolvem a contagem do número possível de listas que satisfazem uma determinada condição ou propriedade. Por causa disso, vamos aprender uma maneira de trabalharmos essa questão sem precisar ficar escrevendo todas as listas possíveis antes de contar os resultados.

\begin{fact}[Princípio da Multiplicação]
Suponha que em uma lista de comprimento $n$ exista $a_1$ escolhas possíveis para a primeira entrada, $a_2$ escolhas possíveis para a segunda entrada, $a_3$ escolhas possíveis para a terceira entrada e etc. Então, o total de listas diferentes que podem ser geradas por essas entradas será igual ao produto entre $a_1 \times a_2 \times a_3 \times \dots \times a_n$. 
\end{fact}

\textbf{Dica}: Nas páginas 67 e 68 do livro, o professor coloca dois exemplos que tornarão esse conceito abaixo bem mais entendível. Se você não entender como esse fato é evidente, dá uma olhada no livro e volta aqui.
\\
\\
Embora no livro não seja dada uma demonstração desse princípio. Eu acho que podemos tentar provar que essa afirmação é verdadeira. Não se preocupe se você não conseguir entender essa demonstração agora. Volte quando estiver mais adiantado no curso e tente novamente.

\begin{demonstration}[Princípio da Multiplicação\footnote{A ideia da primeira parte da demonstração para $m \leq 2$ veio desse livro: JOHNSTON, William; MCALLISTER, Alex. A transition to advanced mathematics: a survey course. OUP USA, 2009. p. 365. Pra segunda parte, onde $m > 2$, a inspiração veio desse link do 
\href{https://math.stackexchange.com/questions/3053969/using-induction-to-prove-the-multiplication-rule}{StackExchange.}}]

Começaremos com a proposição $P(m)$: "Se existirem $m \in \mathbb{N}$ conjuntos $A_i$ com $n_i$ elementos em cada conjunto onde $i \in \{1,2,\dots,m\}$. O Cardinal do produto cartesiano de todos os $m$ conjuntos será igual à multiplicação de todos os $m$ cardinais $| A_i|$, ou seja, $ |A_1 \times A_2 \times \dots \times A_m | = \prod_{i = 1}^{m}\limits | A_i | $"\footnote{O nome desse símbolo é \href{https://en.wikipedia.org/wiki/Multiplication\#Product_of_a_sequence}{"Produtório"}}.
\\
\\
Essa proposição é equivalente ao enunciado do princípio da multiplicação.\footnote{Você consegue ver essa equivalência?}
\\
\\
Quando $m = 1$, temos apenas o conjunto $A_1$ que possui $n_1$ elementos. Portanto, o cardinal de todos os $m = 1$ conjuntos é igual ao cardinal do único conjunto ($|A_m| = |A_1|$). Com isso, vemos que $P(1)$ é verdadeira.
\\
\\
$P(2)$: "Se $A_1$ e $A_2$ são conjuntos finitos onde $A_1$ contém $n_1$ elementos e $A_2$ contém $n_2$ elementos, então, o conjunto $A_1 \times A_2$ possui $n_1 \cdot n_2$ elementos".
\\
\\
A demonstração dessa proposição é simples. Para cada um dos $n_1$ elementos $a \in A_1$ na primeira coordenada do par ordenado $(a,b) \in A_1 \times A_2$, existem exatamente $n_2$ elementos $b \in A_2$. Uma vez que existem $n_1$ elementos em $A_1$ que podem ser essa primeira coordenada do par ordenado $(a,b)$, então, existem ao todo $n_1 \cdot n_2$ possíveis pares ordenados no produto cartesiano $A_1 \times A_2$.
\\
\\
Agora vamos fazer uma pequena adaptação nessa demonstração para qualquer quantidade de conjuntos, ou seja, para qualquer $P(m)$ cujo $m > 2$.
\\
\\
Suponha que agora temos 3 conjuntos: $A_1$, $A_2$ e $A_3$. Para podermos demonstrar $P(3)$: "Se $A_1 \times A_2 \times A_3$, então o cardinal será  $n_1 \cdot n_2 \cdot n_3$"\  só precisamos da seguinte linha de pensamento: Podemos definir um novo conjunto $B = A_1 \times A_2$. Desse modo, podemos reescrever o cardinal anterior como $B \times A_3$. Essa nova reescrita possui apenas dois elementos. Portanto, podemos usar a proposição já demonstrada $P(2)$ sem nenhum prejuízo.
\\
\\
Aplicando esse mesmo procedimento para qualquer $m > 2$ fica demonstrado que o cardinal de quaisquer conjuntos $A_i$ para qualquer $i \in \{1,2,\dots,m\}$ será a multiplicação do cardinal dos conjuntos $A_i$. Aplicando a equivalência da proposição $P(m)$ com o princípio da multiplicação, finalizamos a demonstração. $\blacksquare$
\end{demonstration}

Existem dois tipos de problemas que envolvem contagem de listas: Problemas que possuem entradas repetidas e Problemas que não permitem entradas repetidas. Nós podemos chamar as listas do segundo tipo de problema de \textbf{listas não repetitivas}.
\\
\\
Usando o princípio da multiplicação você é capaz de resolver todos os problemas envolvendo contagens de listas sem precisar ficar escrevendo as soluções possíveis, ao invés disso, você só precisa interpretar as opções de entradas na lista e usar a multiplicação.
\\
\\
\textbf{Dica}: Tente fazer os exemplos 3.1, 3.2 e 3.3 da página 69 até a 72.

\section{Os Princípios da Adição e Subtração}

Vamos ver mais dois princípios de contagem. Você já está familiarizado com eles mas agora definiremos esses princípios usando a linguagem dos conjuntos.

\begin{fact}[Princípio da Adição]
Suponha que um conjunto finito $X$ pode ser decomposto na união $X = \bigcup_{i = 1}^{n}\limits X_i$ onde $ X_i \cap X_j = \emptyset \ \forall \ i \neq j$. Então, $|X| = \sum_{i = 1}^{n}\limits |X_i|$.
\end{fact}

Calma. Não é difícil de entender. O que estamos dizendo ai é: "Se $X$ é um conjunto formado por $n$ outros conjuntos menores de modo que nenhum desses conjuntos possui interseção entre si. Então, o cardinal de $X$ será a soma dos cardinais de todos os $n$ subconjuntos. A única novidade nessa notação é o sigma para denominar somatório.\footnote{Já vimos essa notação no capítulo 01.}
\\
\\
\textbf{Dica}: Veja os exemplos 3.5 e 3.6 na página 75 para ter uma ideia da aplicação desses conceitos na prática.
\\
\\
Agora vamos ver o princípio da subtração. Você não deve ter grandes dificuldades de entender esse conceito.

\begin{fact}[Princípio da Subtração]
Se $X$ é um subconjunto de um conjunto finito $U$, então $|\overline{X}| = |U| - |X|$. Ou seja, se $X \subseteq U$, então $|U - X| = |U| - |X|$.
\end{fact}

Existem situações onde é mais fácil contar o total de um conjunto maior, e retirar uma parte desse total que não queremos, do que contar diretamente a parte desejada. Eu sei, tá um pouco confuso. Mas a ideia é simples: Usamos esse método para computar o que sobra após a retirada de algumas opções.

\textbf{Dica}: Dá uma lida no exemplo 3.7 novamente. A gente usa exatamente essa abordagem pra chegar no resultado.

\section{Fatoriais e Permutações}
O processo de contagem para listas não repetitivas de tamanho $n$ é tão comum que criamos um conceito especial para lidar com esse tipo de problema. O conceito em questão é o \textbf{Fatorial} ($n!$). Antes de formalizarmos o que é o fatorial, observe o quadro abaixo.
\\
\\
\begin{center}
\begin{tabular}{ | c | c | c | c | }
\hline
n & Elementos & Listas não repetidas de tamanho $n$ & $n!$ \\ 
\hline
0 & $\{\}$ & $()$ & 1 \\
1 & $\{a\}$ & $(a)$ & 1 \\
2 & $\{a,b\}$ & $(a,b), (b,a)$ & 2 \\
3 & $\{a,b,c\}$ & $(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a) $ & 6 \\
\vdots & \vdots & \vdots & \vdots \\
\end{tabular}
\end{center}

Consegue ver como a quantidade de listas não repetitivas cresce rápido com apenas o incremento de 1 elemento no exemplo?. O número da última coluna é obtido pela aplicação do princípio da multiplicação. Nós chamamos esse número de \textbf{Fatorial} de $n$. Seu símbolo é esse ponto de exclamação ao lado direito do número "$n!$"\footnote{Lemos como "$n$ fatorial".}.

\begin{definition}[Fatorial]
Se $n$ é um número inteiro não negativo, então $n!$ será o número de listas de tamanho $n$ que podem ser formadas com $n$ símbolos, sem repetições. Desse modo, temos que $0! = 1, 1! = 1$. Para qualquer $n > 1$, então $n! = n \times (n - 1) \times (n - 2) \times \dots \times 3 \times 2 \times 1 $.
\end{definition}

\textbf{Dica}: O exemplo 3.8 na página 79 é ótimo pra exercitar esses conceitos vistos até agora.
\\
\\
Outro conceito importante\footnote{Que eu aposto que você viu no ensino médio e achou que nunca ia usar.} é o conceito de \textbf{Permutação}. Quando computamos um fatorial, estamos, na verdade, contando a quantidade de listas de comprimento $n$ que podem ser geradas a partir da mudança da ordem dos $n$ elementos.
\\
\\
\textbf{Atenção}: Guarde na memória que o \textbf{Fatorial} conta o número de \textbf{Permutações} possíveis para $n$ elementos via aplicação do \textbf{princípio da multiplicação}.
\\
\\
Agora vamos estender um pouco mais esse pensamento. Se temos um total de $n$ elementos. Uma permutação é uma lista de comprimento $n$. Mas e se não quisermos usar todos os elementos disponíveis na composição dessas listas? Para isso o autor usa o conceito de \textbf{k-permutação}\footnote{Do original: k-permutation.}. Uma k-permutação será uma lista de tamanho $k$ formada por um subconjunto dos $n$ elementos anteriores.
\\
\\
Para facilitar (ou não) a nossa vida, vamos definir uma notação para situações onde queremos fazer permutações de comprimento $k$ de um conjunto qualquer de tamanho $n$. Escreveremos $P(n,k)$ para denotar essa situação.\footnote{Perceba que se $k = n$ teremos que $P(n,k) = n!$. Não tem problema nenhum se não entender. Vamo bater um papo no \href{https://twitter.com/bruno_ruas2}{twitter} que eu te explico com mais calma.} 
\\
\\
Para o caso onde $k = 0$ só precisamos pensar em quantas listas de comprimento $0$ conseguiríamos fazer a partir de um conjunto com $n$ elementos. Isso mesmo, só temos uma lista possível - a lista vazia $()$. 
\\
\\
Para todos os casos onde $k \leq n$ podemos calcular o número de k-permutações usando o princípio da multiplicação. Na página 81 tem uns exemplos sobre isso.
\\
\\
Nos casos onde $k > n$ seria como responder algo parecido com: "Quantas lista de 4 elementos podemos fazer com 3 números". A resposta é "zero listas".
\\
\\
De modo mais geral, via princípio da multiplicação, temos que para a primeira entrada da lista de comprimento $k$ temos sempre $(n)$ opções. Para a segunda entrada, teremos $(n - 1)$ opções. Para a terceira entrada teremos $(n - 2)$ opções. Podemos ver claramente um padrão se formando. Podemos definir que o número de escolhas para a posição $i \in \{1,2,\dots,k\}$ será $(n - i + 1)$\footnote{Por exemplo: \\ $i = 1 \implies (n - 1 + 1) = (n)$ opções \\ $i = 2 \implies (n - 2 + 1) = (n - 1)$ opções}. Quando $i = k$ teremos então $(n - k + 1)$ opções.
\\
\\
Com isso podemos chegar em uma equação:
\begin{center}
$ P(n,k) = n . (n - 1) . (n - 2) \dots (n - k + 1) $
\end{center}

Podemos ainda transformar essa relação em outra equação. Primeiro pensemos no que essa parte direta da equação acima quer dizer. Ela se parece com a fórmula do fatorial de $n$ mas com a diferença de "parar" \ em $(n - k + 1)$. Para recuperar o formato do fatorial podemos multiplicar a equação acima por $ (n - k) . (n - k - 1) \dots 3 . 2 . 1 $ e dividir pela mesma expressão.
\ 
\\
\ 
\\

\begin{center}
\small $ P(n,k) = \dfrac{n . (n - 1) . (n - 2) \dots (n - k + 1) . (n - k) . (n - k - 1) \dots 3 . 2 . 1}{(n - k) . (n - k - 1) \dots 3 . 2 . 1} = \dfrac{n!}{(n-k)!}$
\end{center}

Depois de todas essas manipulações, podemos formalizar o conceito de k-permutações.

\begin{fact}[K-Permutações]
Uma \textbf{k-permutação} de um conjunto com $n$ elementos é uma lista de comprimento $k$ feita com elementos desse conjunto. Informalmente, podemos pensar nessa lista como fruto do "rearranjo"\ dos elementos desse conjunto.
\\
\\
O número de k-permutações de um conjunto com $n$ elementos é denotado por $P(n,k)$ e é dado por:\\
\begin{center}
$ P(n,k) = n . (n - 1) . (n - 2) \dots (n - k + 1) $
\end{center}

Se $0 \leq k \leq n$, então temos que:\\
\begin{center}
$ P(n,k) = \dfrac{n!}{(n - k)!} $
\end{center}
\end{fact}


\section{Contando Subconjuntos}
Parte do Luiz

Selecionando $k$ elementos de um conjunto $A$ com $|A| = n$, quantos subconjuntos $A_i$ serão formados dessa permutação?
\\
Lembre-se:
\\
$$\frac{n!}{(n-k)!} > i$$
\\
Isso ocorre pois em listas que contenham os mesmo elementos a ordem que esses elementos são dispostos dentro de cada uma faz com que sejam listas diferentes,então $(a,b)\neq(b,a)$. O que é diferente nos conjuntos, pois dados dois conjuntos $A = \lbrace a,b \rbrace$ e $B = \lbrace b,a \rbrace$, $A=B$.
\\
\begin{definition}
	Se $k,n \in \mathbb{Z}$, então $n \choose k$ denota o número de subconjuntos que podem ser feitos escolhendo $k$ elementos de um conjunto com $n$ elementos. Lemos $n \choose k$ como o "número de permutações de $n$ termos $k$ a $k$ \footnote{Provavelmente você na escola você ouviu assim também, o autor usa \textit{$n$ choose $k$}, porém não sabia exatamente como traduzir de maneira adequada.}"
\end{definition}
Suponha um conjunto $D = \bigcup_{i = 1}^{j}\limits D_i$, onde $|D| = n$. Agora permute cada subconjuntos $D_i$ em listas de $k$ elementos, montando uma tabela temos:
\begin{center}
\begin{tabular}{|c || c || c || c || c|}
$D_1$ & $D_2$ & $D_3$ & $\cdots$ & $D_j$ \\
\hline
$Lista_1^{D_1}$ & $Lista_1^{D_2}$ & $Lista_1^{D_3}$ & $\cdots$ & $Lista_1^{D_j}$\\
$Lista_2^{D_1}$ & $Lista_2^{D_2}$ & $Lista_2^{D_3}$ & $\cdots$ & $Lista_2^{D_j}$\\
$Lista_3^{D_1}$ & $Lista_3^{D_2}$ & $Lista_3^{D_3}$ & $\cdots$ & $Lista_3^{D_j}$\\
$\vdots$ & $\vdots$ & $\vdots$ & $\vdots$ & $\vdots$\\
$Lista_{k!}^{D_1}$ & $Lista_{k!}^{D_2}$ & $Lista_{k!}^{D_3}$ & $\cdots$ & $Lista_{k!}^{D_j}$\\
\end{tabular}
\end{center}
A tabela acima possui dimensões de $k! \times$ $ n \choose k$. Perceba que pelo \textbf{princípio da adição}:
\\
$$P(n,k) = \sum\limits_{i=1}^j P(|D_i|, k) = k! \times {n \choose k}$$ \footnote{Calma, sei que a notação do somatório assusta um pouco, já passei por isso, mas é bem simples na verdade. O que estamos dizendo é que somando o número de permutações de cada subconjunto de $D$ com $k$ elementos é a maneira com a qual chegamos ao número de permutações $k$ a $k$ do conjunto $D$}
\\
Portanto:
\\
$$\frac{n!}{(n-k)!} = k! \times {n \choose k}$$
\\
Dividimos ambos os lados por $k!$ para chegarmos à uma fórmula geral para calcularmos o número de subconjuntos com $k$ elementos de um conjunto qualquer com $n$ elementos.
$$\frac{n!}{k!(n-k)!} = {n \choose k}$$
\\
Se ficou confuso lembre que uma divisão de frações (falando \textbf{MUITO} informalmente) a multiplicação da de cima multiplicado pelo inverso da baixo, para que consiga ver melhor:
\\
O mesmo ocorre 
$$\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a}{b} \frac{d}{c}$$
\begin{fact}[Contagem de subconjuntos]
Se $0 \leqslant k \leqslant n$, então ${n \choose k} = \frac{n!}{k!(n-k)!}$. Caso contrário ${n \choose k} = 0$
\end{fact}
'''

## manipulations
# removendo quebras de linhas e outras marcas de edicao
for i in range(0,100):
	string = string.replace('\\\\','')
	string = string.replace('\\','')

for i in range(0,100):
	string = string.replace('\\n','')
	string = string.replace('\n','')

for i in range(0,100):
	string = string.replace('\t','')

for i in range(0,100):
	string = string.replace('$$','$')

for i in range(0,100):
	string = string.replace(r'\\\'','')

#  changing the $ tokens to [latex] [/latex]
def find_all(string,char):
	return [
		index
		for index in range(len(string) - len(char) + 1)
		if string[index:].startswith(char)
	]


index = find_all(string=string,char='$')
index_even = index[::2]
for i in range(len(index_even)):
	text = list(string)
	text[i] = '[/latex]'
	text = ''.join(text)
	index = find_all(string=string,char='$')
	index_even = index[::2]

