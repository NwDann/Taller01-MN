def make_distinct(arreglo):
    vistos = set()
    operaciones = 0

    for i in range(len(arreglo)):
        original = arreglo[i]
        incrementos = 0
        decrementos = 0

        while (original + incrementos) in vistos:
            incrementos += 1

        while (original - decrementos) in vistos:
            decrementos += 1

        if incrementos <= decrementos:
            arreglo[i] = original + incrementos
            operaciones += incrementos
        else:
            arreglo[i] = original - decrementos
            operaciones += decrementos

        vistos.add(arreglo[i])

    return arreglo, operaciones


def main():
    import sys

    n = int(input())

    arreglo = list(map(int, input().strip().split()))

    nuevo_arreglo, operaciones = make_distinct(arreglo)

    print(operaciones)


if __name__ == "__main__":
    main()
