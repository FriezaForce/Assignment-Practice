import datetime
def showMessage(msg):
    print(msg)
showMessage("Hello!")
def showMessage(msg):
    now=datetime.datetime.now()
    print(msg)
    print(str(now))
showMessage("Current Date and Time is :")