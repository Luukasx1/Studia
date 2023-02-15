# Napisać dwie funkcje konwertujące km->mile oraz mile->km. Funkcje powinny posiadać
# zabezpieczenie przed wprowadzeniem danych nie liczbowych oraz wartości mniejszej lub równej
# zero.

#funkcja konwertująca mile na km.
def mile_na_km():
    try:
        mila = int(input('Podaj ilosc mili: '))
        if mila < 0:
            print('Podaj wartość większą od 0.')
        else:
            km = mila * 1.6
            print(mila, 'mil to: ', km, 'kilometrów.')
    except ValueError:
        print('Podaj zmienną typu int!')

#funkcja konwertująca km na mile.
def km_na_mile():
    try:
        km = int(input('Podaj ilosc mili: '))
        if km < 0:
            print('Podaj wartość większą od 0.')
        else:
            mila = km / 1.6
            print(km, 'mil to: ', round(mila, 1), 'kilometrów.')
    except ValueError:
        print('Podaj zmienną typu int!')


mile_na_km()
km_na_mile()