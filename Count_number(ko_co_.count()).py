number = [1, 6, 8, 1, 2, 1, 5, 6]

while True:
    while True:
        so_nhap = input("Enter a number: ")
        try:
            so_chuyen = float(so_nhap)
            break
        except ValueError:
            print("Not a number")

    so_lan = 0
    for i in range(len(number)):
        if so_chuyen == number[i]:
            so_lan += 1

    print(so_nhap, "xuat hien", so_lan, "lan")

    while True:
        action = input("Again / Stop: ").lower()
        if action == "again" or action == "stop":
            break
        else:
            print("Loi cu phap")
    if action == "stop":
        break

