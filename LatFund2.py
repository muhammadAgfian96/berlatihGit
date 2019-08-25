def capitalize(kalimat='tidak ada'):
    kalimat = kalimat.lower()
    outGanjil = ''
    outGenap = ''
    for i in range(0, len(kalimat)):
        if(i%2==0):
            outGanjil += kalimat[i].upper()
            outGenap += kalimat[i].lower()
        else:
            outGanjil += kalimat[i].lower()
            outGenap += kalimat[i].upper()
    return [outGanjil, outGenap]

def sortString(kata1, kata2):
    out = aku = ''
    for prioritas in kata2:
        for i in range(len(kata1)):
            if(prioritas == kata1[i]):
                out += kata1[i]

    for i in range(len(kata1)):
        if(kata1[i] in out):
            aku +=''
        else:
            aku+=kata1[i]
    return out+aku

def likes(listAja=''):
    out=''
    if (len(listAja)==0):
        out+="no one likes this"
    elif(len(listAja)==1):
        out+= str(listAja[1]) + " likes this"
    elif(len(listAja)==2):
        out += str(listAja[1])+" and " +str(listAja[2])+ " likes this"
    elif(len(listAja)==3):
        out += str(listAja[1])+", " +str(listAja[2])+ " and "+str(listAja[3])+" likes this"
    elif(len(listAja)>=4):
        out += str(listAja[1])+", " +str(listAja[2])+ " and "+str(len(listAja)-2)+"others likes this"
    else:
        print("ERROR")
    return out

def pyramid(baris):
    i=j=0
    jumlah=0
    out = ''
    lebar = 1 + (baris*2)
    mid = (lebar//2)+1
    print_ini =0
    digit = len(str(baris*baris))
    digit =int(digit)
    kotak_kosong = " "*digit

    for i in range(0,baris):
        for j in range(0,lebar):
            if(mid-i-2<=j<=i+mid-2):
                print_ini +=1
                if(print_ini%2==1):
                #kotak isi
                    if( i ==0):
                        jumlah =1
                    else:
                        jumlah +=2
                    if(jumlah<=9):
                        out += str(jumlah)
                        out += " "*(digit-1)
                    elif(jumlah<100):
                        out+=str(jumlah)
                        out += " "*(digit-2)
                    elif(jumlah<1000):
                        out += str(jumlah)
                        out+=" "*(digit-3)
                    elif(jumlah<10000):
                        out+= str(jumlah)
                        out+=" "*(digit-4)
                    else:
                        out+=str(jumlah)
                else:
                    out+=kotak_kosong
            else:
                out+=kotak_kosong
        print_ini=0
        out+='\n'
    print(out)


berhasil=sortString("aakuu", "ku")
print(berhasil)
print(capitalize('aaaaaaaaaaaaaaaaaaa'))


listAja1=["aku", "Dia", "Kamu", "Mereka"]
hahah=likes(listAja1)
print(hahah)