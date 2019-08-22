def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def check_ans(masukan, lower, upper):
    check = True
    while (check):
        while (is_int(masukan)== False):
            masukan = input('## ans (angka): ')

        while (is_float(masukan)== False):
            masukan = input('## ans (angka): ')

        masukan = int(masukan)

        if(masukan>=lower and masukan<=upper):
            check =False    
            return masukan
        else:
            masukan = input("ans ({lower} - {upper}): ".format(lower=lower, upper=upper))
        
def showDict():
    out =  '\n'
    out += '           **Dictionary**            \n'
    out += '-------------------------------------\n'
    out += 'no \tkey\t\tvalue\n'
    out += '-------------------------------------\n'
    for i in range(len(kamus)):
        no = str(i+1)
        out+= no + '\t'+(str([*kamus][i]))+'\t\t'+str([*kamus.values()][i]) + '\n'
    out += '-------------------------------------\n'
    print(out)

def addDict():
    banyak = input("# mau nginput berapa data? (angka): *")
    banyak = check_ans(banyak,0,10)
    jenis = input("# mau jenis \n[1] String\n[2] Integer\n*ans (angka): *")
    jenis = check_ans(jenis,1,2)    
    for i in range(banyak):
        if(jenis==1):
            # append data
            print("== data input ke "+str(i+1)+" ==")
            kunci = input('# keys  = ')
            nilai = input('# value = ')
            kamus[kunci] = nilai
        elif(jenis==2):
            print("== data input ke "+str(i+1)+" ==")
            kunci = input('# keys  = ')
            nilai = input('# value = ')
            nilai = check_ans(nilai,-999999999,999999999)
            kamus[kunci] = nilai
    print("\n*** DONE ADD ***")
    showDict()
def searchDict():
    nom = 0
    search = input("# mau Nyari apa? *")
    out = ''
    out += '    list key '+ search+'           \n'
    out += '-------------------------------------\n'
    out += 'no \tkey\t\tvalue\n'
    out += '-------------------------------------\n'
    for keys in [*kamus]:
        if(search.lower() in keys.lower()):
            nom += 1
            out+= str(nom) + '\t'+(str([*kamus][i]))+'\t\t'+str([*kamus.values()][i]) + '\n'
            out += '-------------------------------------\n'
    print(out)        
    print("search")
def delDict(number):
    print("del")


kamus = { "nama": "agus", "umur": 29, "gender" : "laki-laki"}
# untuk akses daftar list
# print([*kamus][1])
# print([*kamus.values()][0])
# print(list(kamus.keys()))


cek = True
listMenu = [showDict, addDict, searchDict, delDict]
while(cek==True):
    # main program
    nanya = input("# Mau Ngapain?\n[1] Show Dictionary\n[2] Add Dictionary\n[3] Search Dictionary\n[4] Delete Dictionary\n* ans (angka): *")
    nanya = check_ans(nanya,1,4)
    listMenu[nanya-1]()
    ulang = input("* Mau Keluar (y/n)? *")
    if(ulang.upper()=='Y'):
        cek=False