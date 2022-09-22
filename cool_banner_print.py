from termcolor import colored
import pyfiglet
def cool_banner_print(text="banner"):
    text = str(text)
    cbprint = pyfiglet.figlet_format(text)
    print(colored(cbprint, "blue", attrs=["blink"]))
cool_banner_print("kali linux")
