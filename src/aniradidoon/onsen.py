import requests
import time

# Variable
baseURI = "https://www.onsen.ag/"
header = {"content-type": "application/json"}
maximumTryCount = 3

class OnsenAPIData():
    # Get program information from onsen API

    def __init__(self):
        for tryCount in range(0, maximumTryCount):
            try:
                self.result = True
                self.rawData = requests.get(baseURI + "web_api/programs", headers=header).json()
                break
            except Exception as e:
                if tryCount > maximumTryCount:
                    self.result = False
                    self.rawData = ""
                    raise e
                else: 
                    print(f"Error: Trial Count: {tryCount}")
                    print(f"{e}")
                    continue   

    def debug(self):
        if self.result:
            print("データの取得に成功しています。↓")
            self.rawData
        else:
            print("データの取得に失敗しています。")

data = OnsenAPIData()
print(data.rawData)