class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_huffman_tree(codes):
    nodes = [TreeNode(symbol) for symbol in codes.keys()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.value)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = TreeNode(left.value + right.value)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    return nodes[0]

def decode_huffman_message(message, codes):
    decoded_message = []
    current_code = ""
    root = build_huffman_tree(codes)
    node = root
    for bit in message:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.left is None and node.right is None:
            decoded_message.append(codes[node.value])  # Agregar jeroglífico a la lista
            node = root
    return " ".join(decoded_message)  # Unir jeroglíficos con espacios para formar una palabra

# Diccionario de jeroglíficos al alfabeto egipcio
alfabeto_egipcio = {
    'Ankh': '𓋴',
    'Lotus': '𓃀',
    'Scarab': '𓆑',
    'Obelisk': '𓍋',
    'Djed': '𓋜',
    'Sphinx': '𓅆',
    'Pyramid': '𓍯',
    'Eye of Horus': '𓂋'
}

# Mensaje codificado
mensaje_1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
mensaje_2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

# Decodificar mensajes
mensaje_decodificado_1 = decode_huffman_message(mensaje_1, alfabeto_egipcio)
mensaje_decodificado_2 = decode_huffman_message(mensaje_2, alfabeto_egipcio)

print("Mensaje 1 decodificado:", mensaje_decodificado_1)
print("Mensaje 2 decodificado:", mensaje_decodificado_2)

# Diccionario de jeroglíficos al alfabeto egipcio
alfabeto_egipcio = {
    'Ankh': '𓋴',
    'Lotus': '𓃀',
    'Scarab': '𓆑',
    'Obelisk': '𓍋',
    'Djed': '𓋜',
    'Sphinx': '𓅆',
    'Pyramid': '𓍯',
    'Eye of Horus': '𓂋'
}

# Imprimir interpretaciones de los jeroglíficos
for jeroglifico, interpretacion in alfabeto_egipcio.items():
    print(f"{jeroglifico}: {interpretacion}")




# Crear una frase espiritual con los símbolos egipcios
frase_espiritual = f"Como el {alfabeto_egipcio['Lotus']} que se abre a la luz del sol, " \
                   f"así también debes abrirte a la posibilidad de un nuevo comienzo después del divorcio. " \
                   f"El {alfabeto_egipcio['Scarab']}, símbolo de la resurrección, te recuerda que siempre hay una oportunidad para renacer. " \
                   f"El {alfabeto_egipcio['Djed']}, símbolo de la estabilidad, te insta a mantener la fortaleza en tiempos de cambio. " \
                   f"Y el {alfabeto_egipcio['Eye of Horus']}, símbolo de protección, te protegerá en tu camino hacia la sanación."

print(frase_espiritual)

# Crear una frase espiritual con los nombres de los símbolos egipcios
frase_espiritual = f"Como el 'Lotus' que se abre a la luz del sol, " \
                   f"así también debes abrirte a la posibilidad de un nuevo comienzo después del divorcio. " \
                   f"El 'Scarab', símbolo de la resurrección, te recuerda que siempre hay una oportunidad para renacer. " \
                   f"El 'Djed', símbolo de la estabilidad, te insta a mantener la fortaleza en tiempos de cambio. " \
                   f"Y el 'Eye of Horus', símbolo de protección, te protegerá en tu camino hacia la sanación."

print(frase_espiritual)

