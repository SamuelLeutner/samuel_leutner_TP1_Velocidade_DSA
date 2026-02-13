# Lista de Exercícios TP1

1. **List Comprehension em Python**
Escreva um código usando *list comprehension* em Python que retorne os caracteres individuais de uma string que não são caracteres de espaço em branco. Aplique-a à string:
`"Sítio do pica-pau amarelo \n 2023"`
2. **Algoritmo de Ordenação (Baralho de Cartas)**
Pegue um baralho de cartas: retire as 13 cartas de espadas, reserve o resto e embaralhe as cartas de espadas. Elabore um algoritmo para ordená-las por número sob as seguintes restrições:
   * Todas as cartas devem ser seguradas em uma mão. Esta é a "primeira" mão.
   * Inicialmente, as cartas embaralhadas estão todas empilhadas com as faces em uma direção, de modo que apenas uma carta seja visível.
   * Inicialmente, todas as cartas são seguradas entre o polegar e o indicador da primeira mão.
   * A carta visível na pilha pode ser retirada usando a outra mão e colocada entre quaisquer dedos da primeira mão. Ela só pode ser colocada na frente ou atrás das cartas na pilha de cartas entre esses dedos.
   * A outra mão pode segurar apenas uma carta por vez e deve colocá-la em algum lugar na primeira mão antes de pegar outra carta visível de uma das pilhas.
   * O algoritmo termina quando todas as cartas estão ordenadas em uma única pilha na mão.


1. **Busca Linear**
Quantos passos seriam necessários para realizar uma busca linear pelo número **8** no array ordenado: `[2, 4, 6, 8, 10, 12, 13]`?
1. **Busca Binária**
Quantos passos a busca binária levaria para o exemplo anterior?
1. **Otimização de Algoritmo (O(N²) para O(N))**
A seguinte função encontra o maior número único dentro de um array, mas tem uma eficiência de . Reescreva a função para que se torne uma eficiência .
*(Nota: O código da função original não foi fornecido no texto).*
1. **Grãos de Arroz (Potenciação)**
Imagine que você tem um tabuleiro de xadrez e coloca um único grão de arroz em um quadrado. No segundo quadrado, você coloca 2 grãos de arroz (dobro do anterior). No terceiro quadrado, 4 grãos. No quarto, 8 grãos, no quinto 16, e assim por diante.
* Escreva uma função em Python que calcula em qual quadrado do tabuleiro você precisará colocar uma determinada quantidade de grãos de arroz. Por exemplo, para 16 grãos, a função retornará 5.
* Use a Notação Big O para descrever a complexidade de tempo da função que você acabou de criar.


7. **Complexidade Big O (Strings)**
A seguinte função aceita um array de strings e retorna um novo array que contém apenas as strings que começam com o caractere "a". Use a Notação Big O para descrever a complexidade de tempo da função.
*(Nota: O código da função original não foi fornecido no texto).*
8. **Bubble Sort Bidirecional**
No algoritmo Bubble Sort abaixo:
```python
def bubbleSort(self):                       # Ordenar comparando valores adjs.
    for last in range(self.__nItems-1, 0, -1):  # e subir
        for inner in range(last):               # o loop interno vai até o último
            if self.__a[inner] > self.__a[inner+1]: # Se o item for menor
                self.swap(inner, inner+1)           # que o item adjacente, trocar

```

O índice interno sempre vai da esquerda para a direita, encontrando o maior item e levando-o para a direita.

**Tarefa:** Modifique o método `bubbleSort()` para que ele seja bidirecional. Isso significa que o índice interno primeiro levará o maior item da esquerda para a direita como antes, mas quando alcançar o último, ele se inverterá e levará o menor item da direita para a esquerda. Você precisará de dois índices externos, um à direita (o antigo último) e outro à esquerda.

9. **Implementação Bubble Sort (Números)**
Escreva uma função em Python que implemente o algoritmo Bubble Sort para ordenar uma lista de números em ordem crescente. Em seguida, teste a função com diferentes listas de números e verifique se ela está ordenando corretamente.

10. **Implementação Bubble Sort (Strings)**
Modifique a função `bubbleSort()` para que ela ordene uma lista de strings em ordem alfabética. Em seguida, teste a função com diferentes listas de strings e verifique se ela está ordenando corretamente.
