import requests
import json

# Variable
baseURI = "https://www.onsen.ag/"
header = {"content-type": "application/json"}
maximumTryCount = 3


class OnsenAPIData:
    # Get program information from onsen API
    def __init__(self):
        self.result = True
        for tryCount in range(0, maximumTryCount):
            try:
                self.rawData = requests.get(
                    baseURI + "web_api/programs", headers=header
                ).json()
                break
            except Exception as e:
                if tryCount > maximumTryCount:
                    self.result = False
                    self.error = "Could not get from onsen.ag/web_api/programs : " + e
                    self.rawData = ""
                    raise e
                else:
                    print(f"Error: Trial Count: {tryCount}")
                    print(f"{e}")
                    continue

    def summary(self):
        self.summary = []
        try:
            self.summary.append(("latest_date", "directory_name", "title", "latest_count"))
            for i in range(len(self.rawData)):
                program = self.rawData[i]
                self.summary.append((program["title"],
                                    program["updated"],
                                    program["directory_name"],
                                    "No Data" if not program["contents"] else program["contents"][0]["title"]))
            return self.summary
        except Exception as e:
            self.summary = []
            self.result = False
            self.error = "Could not generate summary : " + e

class OnsenAPIDetailData:
    # Get program information from onsen API
    def __init__(self, directory_name):
        self.result = True
        for tryCount in range(0, maximumTryCount):
            try:
                self.rawData = requests.get(
                    baseURI + "web_api/programs/" + directory_name , headers=header
                ).json()
                break
            except Exception as e:
                if tryCount > maximumTryCount:
                    self.result = False
                    self.error = f"Could not get from onsen.ag/web_api/programs/{directory_name} : " + e
                    self.rawData = ""
                    raise e
                else:
                    print(f"Error: Trial Count: {tryCount}")
                    print(f"{e}")
                    continue

    def summary(self):
        self.summary = []
        self.result = True
        self.error = ""
        try:
            self.summary.append(("Subject", "Data"))
            program = self.rawData
            strPerformers = ""
            for i in range(len(program["performers"])):
                strPerformers = strPerformers + program["performers"][i]["name"] + "; "
            self.summary.extend([("Title", program["program_info"]["title"]),
                                ("Directory Name", program["directory_name"]),
                                ("Performer", strPerformers),
                                ("Latest Update", program["current_episode"]["delivery_date"]),
                                ("Station", "インターネット・ラジオステーション〈音泉〉"),
                                ("Copyrights", program["program_info"]["copyright"]),
                                ("Premium", program["program_info"]["premium"]),
                                ("URL", program["program_info"]["directory_url"])])
            return self.summary, self.result, self.error
        except Exception as e:
            self.summary = []
            self.result = False
            self.error = "Could not generate summary : " + e
            return self.summary, self.result, self.error

    def content(self):
        self.content = []
        try:
            pass
        except Exception as e:
            self.summary = []
            self.result = False
            self.error = "Could not generate summary : " + e


if __name__ == "__main__":
    data = OnsenAPIDetailData("gurepa")
    if data.result:
        print("データの取得に成功しています。↓")
        print(data.summary()) 
    else:
        print("データの取得に失敗しています。")
