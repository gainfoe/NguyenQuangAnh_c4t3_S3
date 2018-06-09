str_nhap = sorted(input("Nhap tu: ").lower())
alphabet = "qwertyuiopasdfghjklzxcvbnm"
letters = {}

for letter in str_nhap:
    if letter in alphabet and letter not in letters:
        letters[letter] = []

print("So chu cai la:")
for letter in letters:
    print(letter + ":", str_nhap.count(letter))

