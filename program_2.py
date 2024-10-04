def random_num():
    return 100 + (hash(str(id(random_num))) % 900)

def ask_question():
    num1 = random_num()
    num2 = random_num()
    correct_answer = num1 + num2

    print(f"\n{num1}\n+ {num2}\n------")

    try:
        x = int(input("Enter your answer: "))

        if x == correct_answer:
            print("Congratulations! That's correct.")
        else:
            print(f"Sorry, the answer is {correct_answer}.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    ask_question()
