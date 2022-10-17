
def main():

    import random
    import string

    print("welcome to python password generator:)")

    length = int(input("how long do you want your password to be? "))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    mix = lower + upper + num + symbols

    temp = random.sample(mix, length)

    password = "".join(temp)

    print(password)

    restart = input("would you like to generate another password? ")
    if restart == "yes":
        main()

    else:
        print("bye!")
        exit

main()


