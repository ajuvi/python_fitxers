nom = input("Entra el nom: ")

fitxer = open("/etc/passwd",'r')
home=""
trobat=False

linia = next(fd1,None)
while(linia!=None and not trobat):
    usuari=linia.split(":")
    if usuari[0]==nom:
        trobat=True
        home=usuari[5]
    else
        linia = next(fd1,None)