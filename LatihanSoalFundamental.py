#soal 1
def getSquare(number):
    number_s =str(number)
    out =''
    for item in number_s:
        item = int(item) * int(item)
        out += str(item)
    print(out)
    return(int(out))
# soal 2
def FilterName(tampung):
    bak =[]
    for item in tampung:
        if(len(item) == 4): 
            bak.append(item)
    return bak


# soal 3
def domainName(url):
    if ("www." in url):
        get_name = url.split('.')
        print(get_name[1])
    elif("://" in url):
        get_part = url.split('//')
        get_name = get_part[1].split('.')
        print(get_name[0])
    else:
        print("input bukan url lengkap")

# soal 4
def hitungKata(kalimat):
    list_kalimat = kalimat.split(" ")
    return len(list_kalimat)

# soal 5
def kecilKah(arr, val):
    jumlah = 0
    for item in arr:
        jumlah += item
    if(jumlah<=val):
        return True
    else:
        return False

# soal 6
def delDup(kalimat_6):
    item = kalimat_6.split()
    unik = []
    for i in range(len(item)):
        if(item[i] in unik):
            pass
        else:
            unik.append(item[i])
    return unik

#soal 7
def stringy(num):
    out = ''
    for i in range(num+1):
        if(i%2==0):
            out += '0'
        else:
            out += '1'
    out = int(out)
    return out

# soal 9
def wave(kata):
    kata = kata.lower()
    wave =[]
    for i in range(len(kata)):
        out =''
        up = kata[i].upper()
        for j in range(len(kata)):
            if(j==i):
                out+=up
            else:
                out+= kata[j]
        wave.append(out)
    return(wave)

print("\n# soal 1")
getSquare(423)

print("\n# soal 2")
tampung = ['kieraa', 'kevinn', 'fian', 'gogo','aji']
print(FilterName(tampung))

print("\n# soal 3")
url = "https://stackoverflow.com/questions/14675913/changing-image-size-in-markdown"
url1= "https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php"
domainName(url)
domainName(url1)
domainName("hahah")

print("\n# soal 4")
kalimat = "hari ini aku ketawa hahahahaha"
print(hitungKata(kalimat))

print("\n# soal 5")
arr = [213,123,4,32,23,12,3,123,123]
print(kecilKah(arr,500))

kalimat_6 = 'halo halo kamu siapa siapa kamu fian jika fian'
print("\n# soal 6")
print(delDup(kalimat_6))

print("\n# soal 7")
print(stringy(5))

print("\n# soal 8")
print(wave('aaaaaaaaaa'))