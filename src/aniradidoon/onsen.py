import requests
import json

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

if __name__ == '__main__':
    data = OnsenAPIData()
    if data.result:
        print("データの取得に成功しています。↓")
        print(json.dumps(data.rawData))
    else:
        print("データの取得に失敗しています。")
