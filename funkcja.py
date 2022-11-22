list_notowan = [('CCC', 122.55, 121.7, 123.5, 122.4),
                ('ERG', 43, 41.2, 44.8, 43.6),
                ('IMS', 2.99, 2.99, 3.05, 3.05),
                ('INTROL', 5.08, 4.84, 5.08, 4.94),
                ('PEPCO', 47.25, 46.945, 48.2, 48),
                ('ROPCZYCE', 31.4, 30.7, 31.4, 31.3),
                ('TSGAMES', 350.6, 348, 359.6, 352.6),
                ('WIRTUALNA', 151, 145.8, 155.4, 147.8)]

kursy_walut = {
    '1 USD': 3.9911,
    '1 AUD': 2.9424,
    '1 HKD': 0.5127,
    '1 CAD': 3.1997,
    '1 EUR': 4.6065,
    '100 HUF': 1.28,
    '1 CHF': 4.362,
    '1 GBP': 5.3604,
    '100 JPY': 3.5065,
    '10000 IDR': 2.7856,
    '1 CNY': 0.6235
}


def konwertuj_kurs(notowanie, kurs_otwarcia, kurs_minimalny, kurs_maksymalny, kurs_zamkniecia, kursy, waluta):
    for klucz, wartosc in kursy.items():
        if waluta in klucz:
            przelicznik = wartosc / int(klucz.split()[0])
            return notowanie, \
                   round(kurs_otwarcia / przelicznik, 4), \
                   round(kurs_minimalny / przelicznik, 4), \
                   round(kurs_maksymalny / przelicznik, 4), \
                   round(kurs_zamkniecia / przelicznik, 4)

    return notowanie, 0, 0, 0, 0


def maxZmGPW(notowania, kursy, waluta):
    if len(notowania) == 0:
        return None

    zmiennosc = -1
    inx_notowania = 0
    for i in range(0, len(notowania)):
        zmiennosc_notowania_i = (notowania[i][4] + notowania[i][3]) / (notowania[i][1] + notowania[i][2])
        if zmiennosc < zmiennosc_notowania_i:
            zmiennosc = zmiennosc_notowania_i
            inx_notowania = i

    return konwertuj_kurs(notowania[inx_notowania][0],
                          notowania[inx_notowania][1],
                          notowania[inx_notowania][2],
                          notowania[inx_notowania][3],
                          notowania[inx_notowania][4],
                          kursy,
                          waluta)


print(maxZmGPW(list_notowan, kursy_walut, 'JPY'))
