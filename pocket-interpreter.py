# pocket interpreter

def poweroff():
    alert = input("Are you sure you want to shutdown?")
    if alert == "s" or alert == "S" or alert == "yes" or alert == "YES" or alert == "Yes":
        print("The interpreter is shutting down....")
        return
    elif alert == "n" or alert == "N" or alert == "no" or alert == "NO" or alert == "No":
        interpreter()
    else:
        print("Type yes/no")
        poweroff()

def interpreter():
    print(">>>", end=" ")
    expression = input()
    if expression == "poweroff" or expression == "shutdown":
        poweroff()
    elif expression.isalpha():
        print(expression)
        interpreter()
    else:
        print(eval(expression))
        interpreter()

interpreter()
