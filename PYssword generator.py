import random
import easygui

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
symbols = "{}[]/?!@#%^&*()_+-="

use = upper + lower
password = ""
choices = ("Yes", "No")

useNumbers = easygui.buttonbox(msg="Do you want to use numbers in your pass?", title="PYssword generator", choices=choices)
if useNumbers == "Yes":
    use += numbers

useSymbols = easygui.buttonbox(msg="Do you want to use symbols in your pass?", title="PYssword generator", choices=choices)
if useSymbols == "Yes":
    use += symbols

length = int(easygui.enterbox(msg="Length:", title="PYssword generator"))
for i in range (length):
    ran = random.randint(0, len(use))
    password += use[ran]
easygui.msgbox(msg=password, title="PYsswordgenerator")
