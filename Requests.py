import requests
from colorama import Fore, Style
try:
    source = requests.get("https://modernshadow.ir/api/players?source=bungee")

    responseid = source.status_code

    if responseid == 200:
        print("Status:" + Fore.LIGHTGREEN_EX + " 200" + Style.RESET_ALL)
    elif responseid == 404:
        print("Status:" + Fore.LIGHTYELLOW_EX + " 404" + Style.RESET_ALL)
    elif responseid == 500:
        print("Status:" + Fore.LIGHTRED_EX + " 505" + Style.RESET_ALL)

    api = source.json()

    player = api["players"]

    print("Players: " + Fore.CYAN + str(player) + Style.RESET_ALL )
except Exception as error:
    print(Fore.RED + f"Error: {error}" + Style.RESET_ALL)