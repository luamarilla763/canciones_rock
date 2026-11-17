import matplotlib.pyplot as plt
from scipy import stats


def mostrar_estadisticas_numpy(reproducciones) -> None:
    """
    Muestra estadísticas básicas usando NumPy.
    """

    print("\nANÁLISIS NUMPY")

    print("Total:", reproducciones.sum())
    print("Promedio:", reproducciones.mean())
    print("Máximo:", reproducciones.max())
    print("Mínimo:", reproducciones.min())

    mas_escuchadas = reproducciones[reproducciones > 2000]

    print("\nCanciones con más de 2000 millones:")
    print(mas_escuchadas)
    print("Cantidad:", len(mas_escuchadas))


def mostrar_top_5(canciones) -> None:
    """
    Muestra las 5 canciones más escuchadas.
    """

    print("\nTOP 5 MÁS ESCUCHADAS")

    top5 = canciones.sort_values(
        "Reproducciones_millones",
        ascending=False
    ).head(5)

    print(
        top5[
            ["Titulo",
             "Artista",
             "Reproducciones_millones"]
        ]
    )


def mostrar_generos(canciones) -> None:
    """
    Muestra las reproducciones agrupadas por género.
    """

    generos = canciones.groupby(
        "Genero"
    )["Reproducciones_millones"].sum()

    print("\nREPRODUCCIONES POR GÉNERO")
    print(generos)


def mostrar_estadisticas_scipy(reproducciones) -> None:
    """
    Muestra estadísticas usando SciPy.
    """

    print("\nANÁLISIS SCIPY")

    moda = stats.mode(reproducciones)

    print("Moda:", moda.mode)
    print("Cantidad:", moda.count)

    print(stats.describe(reproducciones))


def grafico_generos(canciones) -> None:
    """
    Genera gráfico por género.
    """

    generos = canciones.groupby(
        "Genero"
    )["Reproducciones_millones"].sum()

def grafico_generos(canciones) -> None:
    """
    Genera gráfico por género.
    """

    generos = canciones.groupby(
        "Genero"
    )["Reproducciones_millones"].sum()

    generos.sort_values(
        ascending=False
    ).plot(kind="bar")

    plt.title("Reproducciones por género")
    plt.ylabel("Reproducciones (millones)")
    plt.xlabel("Género")

    plt.show()


def grafico_canciones(canciones) -> None:
    """
    Genera gráfico de las canciones más escuchadas.
    """

    top10 = canciones.sort_values(
        "Reproducciones_millones",
        ascending=False
    ).head(10)

    plt.figure(figsize=(10, 5))

    plt.bar(
        top10["Titulo"],
        top10["Reproducciones_millones"]
    )

    plt.title("Canciones más escuchadas")
    plt.ylabel("Reproducciones (millones)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()