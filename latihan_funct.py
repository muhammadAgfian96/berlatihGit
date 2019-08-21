#list dalam list

produk = [
    ['jeruk', 2000],
    ['apel', 2300],
    ['banana', 21200],
    ['pisan', 3000],
    ['hohoh', 4000]
]
print(produk[1][1])

cart = [
    [0, 3],
    [1, 4],
    [2,6]
]
x=1
h = cart[0][0]
nama = produk[h][0]
harga = produk[x][1] * cart[x][1]
quanty = cart[x][1]
# print(nama)
# print(harga)
def nama(indexnya):
    return produk[cart[indexnya][0]][0]

def harga(indexnya):
    return produk[indexnya][1] * cart[indexnya][1]

for i in range(0,len(cart)):
    print(nama(i)+ " sebanyak "+ str(cart[i][1])+ " sehingga total = "+ str(harga(i)))

haha = (
    [1, " haha"],
    "asd"
)
l = [1,1,1,1,1,1,1,1,1,1,123,3,23,2,32,32,32,3]
s = {1,1,23,12,1,"Z",12,"B","A",7,8,"A"}
print(s)

newList = [ 'andi', 'budi', 'group']
new_a = ['1', '2']

list2 = [item+ a +' purwadhika' for item in newList for a in new_a]

print(list2)

umur1 = [19, 51, 23, 52]
tahun_lahir = [2019 - item for item in umur1]
print(tahun_lahir)

x = lambda  a,b: 'hallo '+b+' '+ a
print(x("asd","huhu"))

list_lagi = [1,3,4,1]
def kali(x):
    return 2*x

#list isinya bisa function, ketika dipanggil harus pake ()
list2 =  list(map(kali,list_lagi))
print(list2)

tahun = [1990, 1991, 1996,1234]

def umur(tahunLahir):
    return 2019-tahunLahir

def dupMap(func,listAja):
    newList = []
    for item in listAja:
        newList.append(func(item))
    return newList

age = list(map(lambda tahunLahir: 2019 - tahunLahir, tahun))
baruuu = list(filter(lambda tahun: tahun%2 == 0, tahun))
print(baruuu)
print(age)
print(dupMap(umur,tahun))

