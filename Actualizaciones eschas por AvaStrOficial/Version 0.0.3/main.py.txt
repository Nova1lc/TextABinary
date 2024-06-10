from colorama import init, Fore, Style
import os

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

def mostrar_titulo(titulo):
    print(Fore.CYAN + Style.BRIGHT)
    print("╭────┈ ↷ By AvaStrOfical y Nova ")
    print("│╭──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print(f"││ {titulo}")
    print("│╰──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("╰────┈ ✦ ")
    print(Style.RESET_ALL)

def mostrar_github():
    print(Fore.CYAN + Style.BRIGHT)
    print("╭────┈ ↷ Siganos en GitHub ")
    print("│╭──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("││ AvaStrOficial: https://github.com/AvastrOficial")
    print("││ Nova1lc: https://github.com/Nova1lc")
    print("│╰──────────┈ ↷ · ✦ · ✦ · ✦ · ✦")
    print("╰────┈ ✦ ")
    print(Style.RESET_ALL)

def texto_a_binario(texto):
    """Convierte un texto en binario."""
    bytes_texto = texto.encode('ascii')
    binario = ''.join(f"{byte:08b}" for byte in bytes_texto)
    return binario

def binario_a_texto(binario):
    """Convierte una cadena binaria en texto."""
    bytes_texto = [binario[i:i+8] for i in range(0, len(binario), 8)]
    texto = ''.join(chr(int(byte, 2)) for byte in bytes_texto)
    return texto

def guardar_en_archivo(contenido, nombre_archivo):
    """Guarda el contenido en un archivo de texto."""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Contenido guardado en {nombre_archivo}")

def leer_desde_archivo(nombre_archivo):
    """Lee el contenido de un archivo de texto."""
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    else:
        print(f"El archivo {nombre_archivo} no existe.")
        return None

def validar_binario(binario):
    """Verifica si la cadena es un binario válido."""
    return all(char in '01' for char in binario)

def mostrar_instrucciones():
    """Muestra las instrucciones de uso del programa."""
    mostrar_titulo("Instrucciones de Uso")
    print("1. Para convertir texto a binario, seleccione la opción 1 e ingrese el texto.")
    print("2. Para convertir binario a texto, seleccione la opción 2 e ingrese la cadena binaria.")
    print("3. Puede guardar el resultado en un archivo seleccionando la opción correspondiente.")
    print("4. Puede leer texto o binario desde un archivo seleccionando la opción correspondiente.")
    print("5. Asegúrese de que la cadena binaria solo contenga '0' y '1'.")

def main():
    mostrar_banner()
    while True:
        print(Fore.CYAN + Style.BRIGHT)
        print("↷ · ✦ · ✦ · ✦ · ✦ · ✦ ↷")
        print("Seleccione una opción:")
        print("↷ · ✦ · ✦ · ✦ · ✦ · ✦ ↷")
        print(Style.RESET_ALL)
        print("0. Siganos en GitHub")
        print("1. Convertir texto a binario")
        print("2. Convertir binario a texto")
        print("3. Guardar resultado en un archivo")
        print("4. Leer desde un archivo y convertir")
        print("5. Mostrar instrucciones")
        print("6. Salir")
        opcion = input("Introduce el número de la opción deseada: ")

        if opcion == '0':
            mostrar_github()
        elif opcion == '1':
            mostrar_titulo("Convierte un texto en binario.")
            texto = input("Introduce el texto: ")
            binario = texto_a_binario(texto)
            print(f"El texto en binario es: {binario}")
        elif opcion == '2':
            mostrar_titulo("Convierte una cadena binaria en texto.")
            binario = input("Introduce el binario: ")
            if validar_binario(binario):
                texto = binario_a_texto(binario)
                print(f"El binario en texto es: {texto}")
            else:
                print("La cadena introducida no es un binario válido.")
        elif opcion == '3':
            contenido = input("Introduce el contenido a guardar: ")
            nombre_archivo = input("Introduce el nombre del archivo: ")
            guardar_en_archivo(contenido, nombre_archivo)
        elif opcion == '4':
            nombre_archivo = input("Introduce el nombre del archivo: ")
            contenido = leer_desde_archivo(nombre_archivo)
            if contenido is not None:
                print("Contenido del archivo:")
                print(contenido)
                tipo_conversion = input("¿Deseas convertir este contenido? (1: Texto a Binario, 2: Binario a Texto): ")
                if tipo_conversion == '1':
                    binario = texto_a_binario(contenido)
                    print(f"El texto en binario es: {binario}")
                elif tipo_conversion == '2':
                    if validar_binario(contenido):
                        texto = binario_a_texto(contenido)
                        print(f"El binario en texto es: {texto}")
                    else:
                        print("El contenido del archivo no es un binario válido.")
                else:
                    print("Opción no válida.")
        elif opcion == '5':
            mostrar_instrucciones()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
