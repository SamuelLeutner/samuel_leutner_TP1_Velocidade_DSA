import math


# 1. List Comprehension (Caracteres não-espaço)
def extrair_caracteres_validos(texto):
    # Retorna lista de chars ignorando espaços e quebras de linha (\n)
    return [c for c in texto if not c.isspace()]


# 2. Algoritmo de Ordenação de Cartas (Simulação)
def ordenar_cartas_insertion(baralho):
    """
    Simula o algoritmo descrito:
    - A 'mão esquerda' começa vazia.
    - Pegamos uma carta por vez do topo da pilha original.
    - Inserimos na posição correta na 'mão esquerda'.
    """
    mao = []  # Representa as cartas seguradas entre os dedos

    for carta in baralho:
        # Se a mão estiver vazia ou a carta for maior que a última, adiciona ao fim
        if not mao or carta > mao[-1]:
            mao.append(carta)
        else:
            # Procura onde inserir (entre os dedos)
            for i in range(len(mao)):
                if carta < mao[i]:
                    mao.insert(i, carta)
                    break
    return mao


# 5. Otimização de Complexidade (Maior Número)
def encontrar_maior_linear(array):
    """
    Sai de O(N^2) para O(N).
    Basta percorrer a lista uma única vez mantendo o maior valor visto.
    """
    if not array:
        return None
    maior = array[0]
    for item in array:
        if item > maior:
            maior = item
    return maior


# 6. Tabuleiro de Xadrez e Arroz
def calcular_quadrado_arroz(graos):
    """
    Padrão: 1, 2, 4, 8, 16... (Potências de 2)
    Fórmula inversa: log2(graos) + 1
    Complexidade: O(1) (Cálculo matemático direto, sem loops)
    """
    if graos <= 0:
        return 0
    return int(math.log2(graos)) + 1


# 7. Filtrar Strings 'a' (Complexidade)
def filtrar_strings_a(lista_strings):
    """
    Complexidade: O(N)
    Motivo: É necessário iterar por cada elemento da lista original uma vez.
    """
    return [s for s in lista_strings if s.startswith("a")]


# 8. Bubble Sort Bidirecional 
def bubble_sort_bidirecional(lista):
    n = len(lista)
    esquerda = 0
    direita = n - 1
    trocou = True

    while trocou:
        trocou = False

        # Direção: Esquerda -> Direita (leva o maior para o fundo)
        for i in range(esquerda, direita):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True

        if not trocou:
            break  # Se não houve troca, está ordenado

        direita -= 1  # O último elemento já está no lugar certo

        # Direção: Direita -> Esquerda (traz o menor para o início)
        for i in range(direita, esquerda, -1):
            if lista[i - 1] > lista[i]:
                lista[i - 1], lista[i] = lista[i], lista[i - 1]
                trocou = True

        esquerda += 1  # O primeiro elemento já está no lugar certo

    return lista


# 9 e 10. Bubble Sort Clássico (Números e Strings)
def bubble_sort_classico(lista):
    """
    Ordena tanto números quanto strings (ordem alfabética)
    devido ao polimorfismo dos operadores > e <.
    """
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista


if __name__ == "__main__":
    print("--- Q1: List Comprehension ---")
    texto = "Sítio do pica-pau amarelo \n 2023"
    print(extrair_caracteres_validos(texto))

    print("\n--- Q2: Ordenação de Cartas (Insertion Sort) ---")
    cartas_desordenadas = [10, 2, 5, 13, 1]
    print(f"Mão Inicial: {cartas_desordenadas}")
    print(f"Mão Final:   {ordenar_cartas_insertion(cartas_desordenadas)}")

    print("\n--- Q3 e Q4: Análise de Passos ---")
    array_busca = [2, 4, 6, 8, 10, 12, 13]
    alvo = 8
    # Q3: Busca Linear
    # Percorre: 2(não), 4(não), 6(não), 8(sim) -> 4 passos
    print(f"Q3 (Passos Busca Linear para {alvo}): 4")

    # Q4: Busca Binária
    # Meio do array (índice 3) é o 8. Acerta de primeira.
    print(f"Q4 (Passos Busca Binária para {alvo}): 1")

    print("\n--- Q5: Maior Número O(N) ---")
    print(encontrar_maior_linear([10, 50, 99, 2, 5]))

    print("\n--- Q6: Tabuleiro de Arroz ---")
    # Para 16 grãos: log2(16) = 4 -> 4+1 = 5º quadrado
    print(f"Q6 (16 grãos): Quadrado nº {calcular_quadrado_arroz(16)}")
    print("Complexidade: O(1)")

    print("\n--- Q7: Strings com 'a' ---")
    print(filtrar_strings_a(["amor", "bola", "casa", "azul"]))
    print("Complexidade: O(N)")

    print("\n--- Q8: Bubble Sort Bidirecional ---")
    lista_bi = [5, 1, 4, 2, 8, 0]
    print(f"Ordenado: {bubble_sort_bidirecional(lista_bi)}")

    print("\n--- Q9: Bubble Sort (Números) ---")
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort_classico(nums))

    print("\n--- Q10: Bubble Sort (Strings) ---")
    nomes = ["Zebra", "Ana", "Carro", "Bola"]
    print(bubble_sort_classico(nomes))
