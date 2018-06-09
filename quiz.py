question_pack = [
    {
        "question": "Co nhan ra giang vien ko?",
        "choices": ["A.Co", "B.Sieu co.", "C.Khong.", "D.Anh la ai."],
        "right_choice": "D"
    },
    {
        "question": "Co di muon ko?",
        "choices": ["A.Co", "B.Khong.", "C.100k", "D.20k"],
        "right_choice": "B"
    },
    {
        "question": "Tro giang co dtr ko?",
        "choices": ["A.Co", "B.Binh thuong.", "C.Khong", "D.Sieu khong"],
        "right_choice": "D"
    }
]

correct_answer_count = 0
explain = ["Vi em ko bt anh la ai.", "Vi em di som hehe.", "Vi tro giang sieu xau trai"]

for i in range(len(question_pack)):
    q = question_pack[i]
    print("Cau hoi {0}:".format(i + 1), q["question"])

    choices = q["choices"]
    for choice in choices:
        print(choice)
    print()
    user_choice = input("Your answer? ").upper()
    if user_choice == q["right_choice"]:
        print("Bingo")
        correct_answer_count += 1
    else:
        print("Nah. Dap an dung la: {0}.".format(q["right_choice"]))
        print(explain[i])
    print()

percent = correct_answer_count * 100 / len(question_pack)
percent_round = round(percent, 2)
print("Correct: {0} %".format(percent_round))
