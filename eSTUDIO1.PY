def main(): 
    vocales=["A", "E", "I", "O", "U"]
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0


    frase=input("Introduzca una frase: ")
    frase = frase.upper()
    for letra in frase: 
        if letra in vocales:
            if  letra == vocales[0]:
                a+=1
            if letra == vocales[1]:
                e+=1
            if letra == vocales[2]:
                i+=1
            if letra == vocales[3]:
                o+=1
            if letra == vocales[4]:
                u+=1
            
    print("Vocales: a({}), e({}), i({}), o({}), u({})".format(a,e,i,o,u))

if __name__ == '__main__':
    main()