fd1 = open("punts.txt","r")

linia = next(fd1,None)
while(linia!=None):
    linia=linia.strip('\n')
    x=linia.split('-')[0]
    y=linia.split('-')[1]
    print(f"({x},{y})")
    linia = next(fd1,None)