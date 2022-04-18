# Name: Abhi Shrestha
# Classwork 12
# Date: 3/31/22
def question1():
    print("For the follwoing code:\n")
    print("num = 0\nmax = 20\nwhile num< max:\n\tprint(num)\n\tnum = num + 4\n")
    print("The code will count and print to console form 0 to 16 by 4. It should look like:\n 0\n 4\n 8\n 12\n 16")
    keepGoing()
def question2():
    try:
        # prompt user for a number
        num = input("Please input in a positive number: ")
        # lstrip to temporarily strip off any positive or negative signs, replace to for any decimal points (done only 1 incase something like IP address is inputted)
        # isdigit then checks if remaing characters are numbers or not
        while num.lstrip("+|-").replace(".","",1).isdigit() == False:
            print("Non-numerical text/Multi-decimal digits detected. Recheck your input")
            num = input("Please input in a positive number: ")
        else:
            # checking to see if negative sign is in input or not
            while "-" in num:
                print("Negative sign detected.")
                num = input("Please input in a positive number: ")
            else: 
                while "." in num.replace(".","",1):
                    print("Error. Too many decimal points detected. Try again.")
                    num = input("Please input in a positive number: ")
                else: print(f"Postive number detected. You have input: {num}")
        keepGoing()
    except:
        print("Error Detected. Please try again.")
        question2()
def main():
    print("                Welcome to Classwork 12")
    print("--------------------------------------------------------")
    choices()
def choices():
    ans = input("Which question would you like to see the asnwer to, [1] or [2]? ")
    while ans != "1" and ans != "2":
        print("Error detected. Please choose again.")
        ans = input("Which question would you like to see the asnwer to, [1] or [2]? ")
    else:
        if ans == "1": question1()
        else: question2()
def keepGoing():
    x = input("Would you like to continue [Y/N]? ")
    answers = ["y","yes","n","no"]
    while x.lower() not in answers:
        print("Please recheck you input.")
        x = input("Would you like to continue [Y/N]? ")
    else:
        if x.lower() == "y" or x.lower() == "yes": choices()
        else: goodbye() 
def goodbye():
    print("Thank you and have a great Day!")
    tyMessage = """                                                                         
███▀▀██▀▀█████                          ▀███          ▀███▀   ▀██▀                   ██ 
█▀   ██   ▀███                            ██            ███   ▄█                     ██ 
     ██     ███████▄  ▄█▀██▄ ▀████████▄   ██  ▄██▀       ███ ▄█    ▄██▀██▄▀███  ▀███ ██ 
     ██     ██    ██ ██   ██   ██    ██   ██ ▄█           ████    ██▀   ▀██ ██    ██ ██ 
     ██     ██    ██  ▄█████   ██    ██   ██▄██            ██     ██     ██ ██    ██ ▀▀ 
     ██     ██    ██ ██   ██   ██    ██   ██ ▀██▄          ██     ██▄   ▄██ ██    ██ ▄▄ 
   ▄████▄  ████  ████▄████▀██▄████  ████▄████▄ ██▄▄      ▄████▄    ▀█████▀  ▀████▀███▄█
                                                                         
    """
    print(tyMessage)
    print("      .--..--..--..--..--..--.")
    print("    .' \  (`._   (_)     _   \ ")
    print("  .'    |  '._)         (_)  |")
    print("  \ _.')\      .----..---.   /")
    print("  |(_.'  |    /    .-\-.  \  |")
    print("  \     0|    |   ( O| O) | o|")
    print("   |  _  |  .--.____.'._.-.  |")
    print("   \ (_) | o         -` .-`  |")
    print("    |    \   |`-._ _ _ _ _\ /")
    print("    \    |   |  `. |_||_|   |")
    print("    | o  |    \_      \     |     -.   .-.")
    print("    |.-.  \     `--..-'   O |     `.`-' .'")
    print("  _.'  .' |     `-.-'      /-.__   ' .-'")
    print(".' `-.` '.|='=.='=.='=.='=|._/_ `-'.'")
    print("`-._  `.  |________/\_____|    `-.'")
    print("   .'   ).| '=' '='\/ '=' |")
    print("   `._.`  '---------------'")
    print("           //___\   //___\ ")
    print("             ||       ||")
    print("             ||_.-.   ||_.-.")
    print("            (_.--__) (_.--__)")            
main()
