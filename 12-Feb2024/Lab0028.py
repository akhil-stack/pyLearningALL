# Match and Case
# write a program to check the entered browser

browser = str(input("Enter the browser name\t"))
match browser:
    case "Chrome":
        print("Chrome browser is executed")
    case "Firefox":
        print("Firefox browser is executed")
    case _:
        print("Not supported")
