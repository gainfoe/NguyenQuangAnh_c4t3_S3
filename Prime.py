while True:
    while True:
        try:
            so_nhap = int(input("Enter a positive integer: "))
            break
        except ValueError:
            print("Not a positive integer")

    prime = " "
    for i in range(2, so_nhap - 1):
        if so_nhap % i == 0:
            prime = " khong "

    print("So vua nhap" + prime + "la so nguyen to")

    while True:
        action = input("Again / Stop: ").lower()
        if action == "again" or action == "stop":
            break
        else:
            print("Loi cu phap")
    if action == "stop":
        break






