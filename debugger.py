import math
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(orgStr):
    newStr = ""
    for i in orgStr:
        if int(i) + 3 >= 10:
            i = str(((int(i)+3) % 10))
        else:
            i = str(int(i)+3)
        newStr = newStr + i
    return newStr
def decoder(orgStr):
    newStr = ""
    for i in orgStr:
        if int(i) - 3 < 0:
            i = str(10 + (int(i)-3))
        else:
            i = str(int(i)-3)
        newStr = newStr + i
    return newStr
if __name__ == "__main__":
    bool = True
    pswd = ""
    input2 = ""
    while bool:
        menu()
        input1 = int(input("Please enter an option: "))
        if input1 == 1:
            input2 = input("Please enter your password to encode: ")
            pswd = encoder(input2)
            print("Your password has been encoded and stored! ")
        if input1 == 2:
            print(f"The encoded password is {pswd}, and the original password is {input2} ")
        if input1 == 3:
            bool = False
