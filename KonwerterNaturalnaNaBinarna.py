# Napisać funkcję konwertującą podaną liczbę naturalną z wybranego przedziału np 0..255 na
# wartość binarną w postaci łańcucha znaków. Kolejno tak otrzymany łańcuch konwertować na
# liczbę dziesiętną

def naturalna_na_binarna():
    try:
        libc = int(input("Podaj liczbę naturalną: "))
        lista = []
        while True:
            if libc == 0:
                break
            else:
                if libc % 2 == 0:
                    lista.append(0)
                    libc = libc / 2
                else:
                    lista.append(1)
                    libc = libc - 1
                    libc = libc / 2

        ciag_znakow = ''
        lista = str(lista[::-1])

        for cyfra in lista:
            ciag_znakow = ciag_znakow + cyfra

        print(f'Wartość binarna = {ciag_znakow}')

    except ValueError:
        print('Podaj liczbę naturalną!')


naturalna_na_binarna()