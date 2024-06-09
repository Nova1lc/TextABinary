from colorama import init, Fore, Style

# Inicializa colorama
init()

def mostrar_banner():
    print(Fore.CYAN + Style.BRIGHT)
    print("╭────┈ ↷ By AvaStrOfical y Nova ")
    print("│╭──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("││ Convertidor de Texto y Binario")
    print("│╰──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("╰────┈ ✦ ")
    print(Style.RESET_ALL)

def texto_a_binario(texto):
    """Convierte un texto en binario."""
    print(Fore.CYAN + Style.BRIGHT)
    print("╭────┈ ↷ By AvaStrOfical y Nova ")
    print("│╭──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("││ Convierte un texto en binario.")
    print("│╰──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("╰────┈ ✦ ")
    print(Style.RESET_ALL)

    bytes_texto = texto.encode('ascii')
    binario = ''.join(f"{byte:08b}" for byte in bytes_texto)
    return binario

def binario_a_texto(binario):
    """Convierte una cadena binaria en texto."""
    print(Fore.CYAN + Style.BRIGHT)
    print("╭────┈ ↷ By AvaStrOfical y Nova ")
    print("│╭──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("││ Convierte una cadena binaria en texto.")
    print("│╰──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("╰────┈ ✦ ")
    print(Style.RESET_ALL)

    bytes_texto = [binario[i:i+8] for i in range(0, len(binario), 8)]
    texto = ''.join(chr(int(byte, 2)) for byte in bytes_texto)
    return texto

def main():
    mostrar_banner()
    while True:
        print(Fore.CYAN + Style.BRIGHT)
        print("↷ · ✦ · ✦ · ✦ · ✦ · ✦ ↷")
        print("Seleccione una opción:")
        print("↷ · ✦ · ✦ · ✦ · ✦ · ✦ ↷")
        print(Style.RESET_ALL)
        print("1. Convertir texto a binario")
        print("2. Convertir binario a texto")
        print("3. Salir")
        opcion = input("Introduce el número de la opción deseada: ")

        if opcion == '1':
            texto = input("Introduce el texto: ")
            binario = texto_a_binario(texto)
            print(f"El texto en binario es: {binario}")
        elif opcion == '2':
            binario = input("Introduce el binario: ")
            texto = binario_a_texto(binario)
            print(f"El binario en texto es: {texto}")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
