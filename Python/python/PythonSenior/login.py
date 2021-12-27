import getpass

try:
    pass_word = getpass.getpass()
except Exception as E:
    print("There is an Error : ", E)
else:
    print("Password fetched from command prompt :", pass_word)
    print(getpass.getuser())
