import pandas as pd

from analisis import (
    mostrar_estadisticas_numpy,
    mostrar_top_5,
    mostrar_generos,
    mostrar_estadisticas_scipy,
    grafico_generos,
    grafico_canciones
)


def main() -> None:
    """
    Función principal del programa.
    """

    try:
        canciones = pd.read_csv(
            "canciones_rock.csv"
        )

        reproducciones = canciones[
            "Reproducciones_millones"
        ].to_numpy()

    except FileNotFoundError:
        print("Error: no se encontró canciones_rock.csv")
        return

    while True:

        print("\n===== MENÚ =====")
        print("1 - Top 5 canciones")
        print("2 - Reproducciones por género")
        print("3 - Gráfico por género")
        print("4 - Gráfico canciones más escuchadas")
        print("0 - Salir")

        opcion = input("\nElegí una opción: ")
        
        if opcion == "1":
            mostrar_top_5(canciones)
        
        elif opcion == "2":
            mostrar_generos(canciones)
            
        elif opcion == "3":
            grafico_generos(canciones)
            
        elif opcion == "4":
             grafico_canciones(canciones)
        
        elif opcion == "0":
            print("Programa finalizado.")
            break
        
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()