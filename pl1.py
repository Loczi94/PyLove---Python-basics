import string

def policz_slowa(zdanie):
    count=0
    lista=zdanie.split()
    print("Liczba slow w zdaniu:")
    print(len(lista))

def policz_samogloski(zdanie):
    count=0
    samogloski=["a","e","i","o","u","y"]
    for z in zdanie:
        if z in samogloski:
            count+=1
    print("Liczba samoglosek w zdaniu:")
    print(count)

def xo_checker(xo_string):
    x=0
    o=0
    illegal=False
    for s in xo_string:
        if s=="x":
            x+=1
        elif s=="o":
            o+=1
        else:
            print("Illegal letters in text!")
            illegal=True
            break
    if not illegal:
        if x==o:
            return True
        else:
            return False

def cenzura_cyfr(password):
    cyfry=("1","2","3","4","5","6","7","8","9")
    for p in password:
        if p in cyfry:
            password=str.replace(password,p,"#")
    print(password)

def odwazniki(a,b):
    try:
        a=int(a)
        b=int(b)
        tmp_a=a
        tmp_b=b
        ab=a*b
        while (tmp_b!=0):
            t=tmp_b
            tmp_b=tmp_a%tmp_b
            tmp_a=t
        ab=ab/tmp_a
        liczba_a=ab/a
        liczba_b=ab/b
        print(str(liczba_a)+" odważnik(i)/odważników o wadze "+str(a)+" = "+str(liczba_b)+" odważnik(i)/odważników o wadze "+str(b))
    except ValueError:
        print("Niepoprawne dane wejściowe!")

def droga(t, a, vs=0):
    s=vs*t+((a*t**2)/2)
    print(s)
    return s

def cezar(napis,parametr):
    pozycja=0
    for l in napis:
        if (ord(l)>=97 and ord(l)<=122): #małe litery
            if (ord(l)+parametr<97):
                nowy_indeks=122-(97-ord(l)-parametr)+1
                nowa_l=chr(nowy_indeks)
                napis = napis[:pozycja+1] + napis[(pozycja + 1):]
                napis = napis[:pozycja] + nowa_l + napis[(pozycja + 1):]
            elif (ord(l)+parametr>122):
                nowy_indeks=97+(ord(l)+parametr-122)-1
                nowa_l = chr(nowy_indeks)
                napis = napis[:pozycja+1] + napis[(pozycja + 1):]
                napis = napis[:pozycja] + nowa_l + napis[(pozycja + 1):]
            else:
                nowa_l = chr(ord(l)+parametr)
                napis = napis[:pozycja+1] + napis[(pozycja + 1):]
                napis = napis[:pozycja] + nowa_l + napis[(pozycja + 1):]
        elif (ord(l)>=65 and ord(l)<=90): #duże litery
            if (ord(l)+parametr<65):
                nowy_indeks = 90 - (65 - ord(l) - parametr)+1
                nowa_l = chr(nowy_indeks)
                napis = napis[:pozycja+1] + napis[(pozycja + 1):]
                napis = napis[:pozycja] + nowa_l + napis[(pozycja + 1):]
            elif (ord(l)+parametr>90):
                nowy_indeks = 65 + (ord(l) + parametr - 90)-1
                nowa_l = chr(nowy_indeks)
                napis = napis[:pozycja+1] + napis[(pozycja + 1):]
                napis = napis[:pozycja] + nowa_l + napis[(pozycja + 1):]
            else:
                nowa_l = chr(ord(l)+parametr)
                napis = napis[:pozycja+1] + napis[(pozycja + 1):]
                napis = napis[:pozycja] + nowa_l + napis[(pozycja + 1):]
        pozycja+=1
    print(napis)


if __name__ == '__main__':
    print('Zadanie 1\n')
    xo_checker("xxxxxxoooooo")
    print('\nZadanie 2\n')
    cezar("1AbcDExYZz-2", -3)
    print('\nZadanie 3\n')
    droga(10, 10, vs=100);
    print('\nZadanie 4\n')
    odwazniki(6, 4);
    print('\nZadanie 5\n')
    cenzura_cyfr("123password456")
    print('\nZadanie 6\n')
    policz_samogloski("Ala ma kota")
    print('\nZadanie 7\n')
    policz_slowa("Ala ma kota")
