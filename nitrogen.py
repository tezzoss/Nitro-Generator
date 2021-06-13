import random, string, webbrowser, time, requests, colorama
from colorama import init, Fore
#
init()
num=input('How many codes?: ')

f=open("list.txt","w", encoding='utf-8')

print("")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()
print(f"{Fore.RED}Codes saved to list.txt")
print(f"{Fore.MAGENTA}Thank you for using my very basic nitro code generator.")
input()