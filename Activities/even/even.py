def even_number(number):
    try:
        if number % 2 == 0:
            print("This entered number is even")
    except:
        print("The number entered by you is not even")


num = input("Enter the number")
even_number(num)
