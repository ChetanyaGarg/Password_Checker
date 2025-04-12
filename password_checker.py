import re
import random
import string
from colorama import Fore, Style

def random_password(password,k):
    if len(password)<8:
        k = 8-len(password)-2
        
    random_digit=''.join(random.choices(string.digits,k=k))
    random_unique=random.choice("!@#$%^&*()_-+=<>.?")
    random_upper=random.choice(string.ascii_uppercase)
    return password+random_upper+random_digit+random_unique


def password_checker(password):

    if any(character.isspace() for character in password):  
        return Fore.RED + "Avoid Using Spaces" + Style.RESET_ALL
    
    if len(password) < 8:
        return Fore.RED + "Weak Password, Your Password Should Contain At Least 8 Characters" + Style.RESET_ALL

    if not any(character.isdigit() for character in password):
        return Fore.RED + "Weak Password, Try Adding At Least One Digit" + Style.RESET_ALL
    
    if not any(character.isupper() for character in password):
        return Fore.RED + "Weak Password, Try Adding At Least One Upper Case Character" + Style.RESET_ALL
    
    if not any(character.islower() for character in password):
        return Fore.RED + "Weak Password, Try Adding At Least One Lower Case Character" + Style.RESET_ALL
    
    if not re.search(r'[!@#$%^&*()_\-+=<>.{,/}\[\]?]', password):
        return Fore.YELLOW + "Medium Password, Try Adding Special Character To Make Your Password Stronger" + Style.RESET_ALL
    
    return Fore.GREEN + "Strong Password, It Is A Reliable Password" + Style.RESET_ALL

def password_input():
    print('\n')
    print(Fore.CYAN + "[+] Starting Password Strength Checker" + Style.RESET_ALL)
    print(Fore.CYAN + "[+] Just A Second..." + Style.RESET_ALL)

    while True:
        print('\n')
        
        password = input("Enter Your Password (Type 'exit' to quit): ")

        if password.lower() == 'exit':
            print('\n')
            print(Fore.CYAN + "[-] Quitting The Program" + Style.RESET_ALL)
            print(Fore.CYAN + "[-] Thanks For Using :)" + Style.RESET_ALL)
            print('\n')
            break

        rec1=random_password(password,random.randint(0, 6))
        rec2=random_password(password,random.randint(0, 6))
        rec3=random_password(password,random.randint(0, 6))

        result = password_checker(password)
        print(result)
        
        print(Fore.MAGENTA + f"Recommended Passwords: {rec1}, {rec2}, {rec3}" + Style.RESET_ALL)



if __name__ == "__main__":
    password_input()
