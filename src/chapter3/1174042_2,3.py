def npm(x):
    a = 0
    k = int(x[4])
    p = int(x[5])
    i = int(x[6])
    b = x[4:7]
    c = k+p+i

    while a < c:
        a += 1
        print("Hello, " + b + " Apa Kabar?")
    return x

x = input("Masukkan NPM: ")
c = npm(x)