fd1 = open("punts.txt","r")

linia = next(fd1,None)
while(linia!=None):
    linia=linia.strip('\n')
    print(linia)
    linia = next(fd1,None)