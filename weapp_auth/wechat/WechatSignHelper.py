import collections
import hashlib
import copy

class WeChatSignHelper:
    def __init__(self,dataDict,apiKey):
        self.data = copy.deepcopy(dataDict) #type: dict
        self.apiKey = apiKey
        self.keyValueString = ""
        self.clean_up()
        self.dataToKeyValueString()


    def clean_up(self):
        if "sign" in self.data:
            del self.data["sign"]

    def dataToKeyValueString(self):
        od = collections.OrderedDict(sorted(self.data.items()))
        for key,value in od.items():
            self.keyValueString+=f"{key}={value}&"
        self.keyValueString += f"key={self.apiKey}"

    def getSign(self):
        md5Obj = hashlib.md5()
        md5Obj.update(self.keyValueString.encode("utf-8"))
        return md5Obj.hexdigest().upper()






