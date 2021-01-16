import requests

class KeyBoardListener:
    def __init__(self):
        self.pin = ""
        self.url = 'https://www.gamerotasystem.com/input'
        self.run()

    def run(self):
        while True:
            self.pin = input("Pin : ")
            self.sendPin()

    def sendPin(self):
        inOut = None
        if self.pin[-1:] == "*":
            inOut = True
        elif self.pin[-1:] == "/":
            inOut = False

        if inOut != None:
            self.pin = self.pin[:-1]
            myobj = {'id': self.pin, "storeId" : 1234, "clockIn": inOut}

            s = requests.Session()
            headers = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
            x = s.post(self.url, data=myobj, headers=headers)
            if x.text == "1":
                print("Success = Green Light\n")
            else:
                print(x.text)
                print("Failed = Red Light\n")
        else:
            print("Failed = Red Light\n")
        self.pin = ""

keybord = KeyBoardListener()