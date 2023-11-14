s = "My name is Kedar Keknis. I live in Mumbai, MH-400001."

temp = ""
prev = 0
def check(value):
    value =
    for val in value.split():
        if val.isDigit() and len(val) == 6:
            return val


print(check(s))