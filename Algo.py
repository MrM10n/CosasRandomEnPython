Ingresos = 1000000000

if Ingresos > 1000000:
    print("""Hacienda te va a registrar por presunto trafico de drogas
    1.- Declararse Culpable
    2.- Oponerse e ir a juicio""")

    decision1 = input("Que camino tomarás? ")

    if decision1 == "1":
        print("Has ido a la carcel por narcotrafico - Final malo te sentencian a cadena perpetua")
        decision2 = input(""" Que camino tomaras ahora? 
        1.- Escapar de la carcel
        2.- Quedarte y aceptar tu castigo
        """)

        if decision2 == "1":
            print("Has escapado con exito - Final intermedio ya nadie te molestará decides vivir en una cabaña alejado de la sociedad ")
        elif decision2 ==  "2":
            print("Has vivido el resto de tu vida dentro de la carcel - Final sin culpa puedes morir sin culpa pues tus malos pasos no son por ti, si no por la sociedad y el ambiente en el que te criaste, ademas, fuiste honesto y viviste tu condena")


    elif decision1 == "2":
        print("Acabas de entrar en juicio - Final feliz te han declarado inocente pero realmente eres culpable")
        decision3 = input("""Que camino elegiras?
         1.- Seguir traficando drogas
         2.- Dejar de traficar drogas y arrepentirse """)
        
        if decision3 == "1":
            print("Te han descubierto, ahora viviras en la carcel")

        elif decision3 == "2":
            print("""Ahora de que vas a trabajar?
            1.- Trabajador del Soriana
            2.- Cajero del oxxo""")
            decision4 = input("Cual sera tu trabajo? ")
        if decision4 == "1":
            print("Te asaltaron y moriste")
        elif decision4 == "1":
            print("Te asaltaron y moriste")
            