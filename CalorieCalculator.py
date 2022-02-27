def user_info():
    kön = input('Vad är ditt kön? ')
    ålder = int(input('Vad är din ålder? '))
    längd = int(input('Hur lång är du i centimeter? '))
    vikt = int(input('Hur mycket väger du? '))

    if kön.lower() == 'man':
        c1 = 66
        hm = 5.0 * längd
        wm = 13.7 * vikt
        am = 6.8 * ålder
    elif kön.lower() == 'kvinna':
        c1 = 655 
        hm = 1.8 * längd
        wm = 9.6 * vikt
        am = 4.7 * ålder

    #bmr = 66 + (13,7 * vikt) + (5 * längd) - (6,8 * ålder)
    bmr_resultat = c1 + hm + wm - am
    return(int(bmr_resultat))

def kalkylera_träning(bmr_resultat):
    tränings_nivå = input('Hur många gånger tränar du i veckan? (0, 1-2, 3-4, 5-6, 7 ): ')
    
    if tränings_nivå == '0':
        tränings_nivå = 1.2 * bmr_resultat
    elif tränings_nivå == '1-2':
        tränings_nivå = 1.375 * bmr_resultat
    elif tränings_nivå == '3-4':
        tränings_nivå = 1.55 * bmr_resultat
    elif tränings_nivå == '5-6':
        tränings_nivå = 1.725 * bmr_resultat
    elif tränings_nivå == '7':
        tränings_nivå = 1.9 * bmr_resultat
    
    return(int(tränings_nivå))

def gå_upp_eller_gå_ner(tränings_nivå):
    mål = input('Vill du gå upp, ner eller hålla i vikt? ')

    if mål.lower() == 'gå ner':
        kalorier = tränings_nivå - 500
    elif mål.lower() == 'hålla':
        kalorier = tränings_nivå
    elif mål.lower() == 'gå upp':
        gå_upp = int(input('Gå upp 0,5 eller 1 kilo i veckan? Skriv 0.5 eller 1 '))
        if gå_upp == 0.5:
            kalorier = tränings_nivå + 500
        elif gå_upp == 1:
            kalorier = tränings_nivå + 1000

    print('för att kunna ', mål, 'vikt, ditt dagliga kalori intag borde vara', int(kalorier), '!')
    
gå_upp_eller_gå_ner(kalkylera_träning(user_info()))

def tränings_pass(tränings_övningar):
    träningspass = input('Vad vill du träna idag? Välj mellan rygg, bröst, ben, armar och axlar, rygg och bröst ')

    if träningspass.lower() == 'rygg':
        print('Stående rod, T-bar rod, Lats, En arms hantel rod, Rep pullover ')
    elif träningspass.lower() == 'bröst':
        print('Bänkpress, Snebänk med hantlar, Kabel flys, Hantel flys, Peckdeck ')
    elif träningspass.lower() == 'ben':
        print('Benböj, RDLs, Benpress, Vader ')
    elif träningspass.lower() == 'armar och axlar':
        print('Axelpress, Kabellyft åt sidan, Militärpress, Biceps curls, Hammer curls, Triceps pushdown, Dips ')
    elif träningspass.lower() == 'rygg och bröst':
        print('Snehantel press, Kabel flys, pecdeck, Stående rodd, Lats pulldown, Rep pullover ')

tränings_pass(tränings_pass(user_info))

