# M: gendernya
# J: huruf nama pertama (John)
# SI : huruf pertama sama huruf tengah dari nama kedua (kalo jumlah hurufnya genap, maka nilai tengahnya ada 2)
# 1 : digit terakhir tanggal
# 1 : jan
# 67 : 2 digit terakhir tahun

list_huruf = list("abcdefghijklmnopqrstuvwxyz ")

print(len(list_huruf))

def alphaSum(kalimat):
    out = ''
    jumlah = 0
    for index in (kalimat):
        angka =  list_huruf.index(index)+1
        out += str(angka) + " "
        jumlah += angka
    out+="\n"
    print(out + "hasil = " + str(jumlah))


def alphaNext(kalimat, number):
    out = ''
    print("awal  = " + kalimat + ", maju sebanyak "+str(number))
    for index in kalimat:
        angka = list_huruf.index(index)+1
        maju = angka-1+number
        out += list_huruf[maju]
    print("akhir = " + out)

def generateNum(data):
    list_bulan = ["JAN", "FEB", "MAR", "APR", "MEI", "JUN", "JUL", "AUG", "SEP", "OKT", "NOV", "DES"]
    out = ''
    out += data[3] # gender
    out += data[0][0] # nama depan
    nama_tengah = data[1]
    # nama tengah
    if(len(nama_tengah)%2==0):
        tengah1 = len(nama_tengah)//2
        tengah2 = tengah1-1
        out += (data[1][0] + data[1][tengah2] + data[1][tengah1]).upper()
    else:
        tengah = (len(nama_tengah)//2) 
        out+= data[1][0].upper()
        out += data[1][tengah].upper()
    out += "-"
    tanggal = data[2].split("-")
    tgl = tanggal[0][1]
    bulan = str(list_bulan.index(tanggal[1].upper())+1)
    tahun = tanggal[2][2:]
    out += tgl+bulan+tahun

    print(out)


def findUniq(the_data):
    unik = 0
    unik_list = []
    for i in range(len(the_data)):
        for j in range(len(the_data)-1, -1, -1):
            if (the_data[i]==the_data[j]):
                unik += 1
        if (unik==1):
            print("unik: ")
            print(the_data[i])
            unik_list.append(the_data[i])
        unik = 0
    
    if (len(unik_list) == 0):
        print("Nothing Unik")


    return unik_list            

def sumTwoSmallest(data):
    A = B = data[0]
    for i in range(len(data)):
        for j in range(len(data)):
            if (A >= data[j]):
                A = data[j]
            if (B>=data[j] and B < A):
                B = data[j]
    return A+B

def numOf_pair(data):
    #for untuk mencari nilai tunggal
    value = []
    count = 0
    count_dict= {}
    for i in range(len(data)):
        for j in range(len(data)):
            if (data[i] == data [j]):
                count +=1

        count_dict[data[i]] = count
        count=0

    print(count_dict)
    #belum selesai

print("\n-> soal #1 ")
alphaSum("aku")

print("\n-> soal #2 ")
alphaNext("aaa",2)

print("\n-> soal #3 ")
data = ["John", "Smith", "01-jan-1967", "M"]
generateNum(data)

print("\n-> soal #4 ")
the_data = ["halo", "hello", "halo", "fikri", "Fikri"]
the_data1= [1,1,2,3,3]
findUniq(the_data)
findUniq(the_data1)

print("\n-> soal #5 ")
the_data1= [1,0.5,0.22,3,3]
haha = sumTwoSmallest(the_data1)
print(haha)

print("\n-> soal #6 ")
the_data1= ["green","green","green", "red", "blue","blue", "blue","blue", "black", "black"]
the_data2= ["green","green", "green", "red", "black", "black"]
numOf_pair(the_data1)

