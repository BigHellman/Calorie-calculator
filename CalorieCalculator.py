from kivy import kivy_register_post_configuration


def user_info():
    kön = input('Vad är ditt kön?: ')
    ålder = int(input('Vad är din ålder?: '))
    längd = int(input('Hur lång är du i centimeter?: '))
    vikt = int(input('Hur mycket väger du?: '))

    if kön == 'man':
        c1 = 66
        hm = 6.2 * längd
        wm = 12.7 * vikt
        am = 6.76 * ålder
    elif kön == 'kvinna':
        c1 = 655.1 
        hm = 4.35 * längd
        wm = 4.7 * vikt
        am = 4.7 * ålder

    #bmr = 665 + (9.6 X 69) + (1.8 X 178) - (4.7 X 27)
    bmr_resultat = c1 + hm + wm - am
    return(int(bmr_resultat))

def kalkylera_träning(bmr_resultat):
    
