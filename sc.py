bb = float(input("Masukkan berat badan : "))
tb = float(input("Masukkan tinggi badan : "))

def ibm(bb, tb):
    bmi=bb/(tb*tb)
    if (bmi < 18):
        print("Anda kurus")
    elif (bmi < 25):
        print("Tubuh anda ideal")
    elif (bmi < 27):
        print("Tubuh anda kegemukan")
    else:
        print("TUbuh anda obsitas")
    return bmi


print(ibm(bb, tb))