def main():
    #Prompt for input
    #Catch people that are improperly trying to break the code
    # by inputting hello as a parameter instead of "hello"
    try:
        count = input("Number to iterate to? (i.e. 100) \n")
    except NameError:
        print("If you're trying to break the code, use quotation marks")
        return False

    #Check if input is number
    if not is_number(count):
        print("Invalid Input")
        return

    #Iterate through numbers
    for i in range (1,count+1):
        #Fizzbuzz instance
        if i%5==0 and i%3==0:
            print("Fizzbuzz")
        #Fizz instance
        elif i%3==0:
            print("Fizz")
        #Buzz instance
        elif i%5==0:
            print("Buzz")
        #Neither, just print the number
        else:
            print(i)

#Check if the given prompt is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()
