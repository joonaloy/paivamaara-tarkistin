def pvm(p):
    #päivä,kk,vuosi muuttujat
    pv=""
    k=""
    v=""
    #karkausvuosi muuttuja
    kv=0
    #erittelee inputin päiviin kuukausiin ja vuosiin
    pv+=p[0]+p[1]
    k+=p[2]+p[3]
    v+=p[4]+p[5]+p[6]+p[7]
    pv=int(pv)
    k=int(k)
    v=int(v)
    #tarkistaa onko vuosi karkausvuosi
    if v%400==0 and v%100==0:
        kv=1
    elif v%4==0 and v%100!=0:
        kv=1
    else:
        kv=0
    #tarkistaa onko päivä suurempi kuin kuukauden viimeinen päivä ja printtaa vastauksen sen perusteella
    if k==1 or k==3 or k==5 or k==7 or k==8 or k==10 or k==12:
        if pv<32:
            print(pv,k,v,"On oikea päivämäärä")
        else:
            print(pv,k,v,"Ei ole oikea päivämäärä")
    if k==4 or k==6 or k==9 or k==11:
        if pv<31:
            print(pv,k,v,"On oikea päivämäärä")
        else:
            print(pv,k,v,"Ei ole oikea päivämäärä")
    if k==2:
        if kv==1:
            if pv<30:
                print(pv,k,v,"On oikea päivämäärä")
            else:
                print(pv,k,v,"Ei ole oikea päivämäärä")
                
        if kv==0:
            if pv<29:
                print(pv,k,v,"On oikea päivämäärä")
            else:
                print(pv,k,v,"Ei ole oikea päivämäärä") 
    #tarkistaa onko kuukausi suurempi tai pienempi kuin mahdollista
    if k<1 or k>12:
        print(pv,k,v,"Ei ole oikea päivämäärä")

pvm("14062006")
pvm("29022024")
pvm("29022023")
pvm("01132020")
