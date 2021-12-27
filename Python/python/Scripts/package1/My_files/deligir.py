Max_with = 30

def main(number):
    if number > Max_with:
        count_star = '*' * Max_with
    else:
        count_star = '*' * (Max_with-round(number))
    print(f"{count_star} {round(number,2)} {count_star}")


while True:
    try:
        first = int(input("first number:"))
        second = int(input("second number:"))
    except ValueError as error:
        print(error,"/ntry again")
    else:
        main(first/second)
        break

