def texto_a_binario(texto):
    bytes_texto = texto.encode('ascii')
    binario = ''.join(f"{byte:08b}" for byte in bytes_texto)
    return binario

def main():
    continuar = '1'
    while continuar == '1':
        texto = input("Introduce el texto: ")
        binario = texto_a_binario(texto)
        print(f"El texto en binario es: {binario}")
        continuar = input("Si deseas continuar introduce el numero 1: ")

if __name__ == "__main__":
    main()
