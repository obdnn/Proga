def text():
    a = open("proga.txt", "r")
    s = a.readlines()
    a.close()

    for i in range(len(s)):
        if "\n" in s[i]:
            s[i] = s[i][:-1]

    return s


def calc(text, a):
    for i1, i in enumerate(text):
        text[i1] = i.split(" ")

    for i in text:
        if int(i[1]) > a:
            print(f"час - {i[0]}  значенння параметра XXX - {i[1]}")


def tin():
    while True:
        a = input("Введіть значення параметра або введіть 'exit' для виходу \n -> ")

        if a == "exit":
            break
        elif a.isdigit():
            calc(text(), int(a))
        else:
            print("Спробуйте використовувати тільки цифри\n")


def main():
    tin()


main()
