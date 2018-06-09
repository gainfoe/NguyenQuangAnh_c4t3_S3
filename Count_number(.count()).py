number = [1, 6, 8, 1, 2, 1, 5, 6]

while True:
    while True:
        so_nhap = input("Enter a number: ")
        try:
            so_chuyen = float(so_nhap)
            break
        except ValueError:
            print("Not a number")

    print(so_nhap, "xuat hien", number.count(so_chuyen), "lan")

    while True:
        action = input("Again / Stop: ").lower()
        if action == "again" or action == "stop":
            break
        else:
            print("Loi cu phap")
    if action == "stop":
        break

