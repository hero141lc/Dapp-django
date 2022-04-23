import requests
import json

class posterapi():

    def __init__(self, endpoint: str, token: str):
        if endpoint.endswith("/"):
            endpoint = endpoint[0:-1]
        #self.endpoint = endpoint
        self.endpoint ='http://brickcn.xyz:5000'
        self.token = token

    def getUrl(self, posterId: str, params: dict = {}):
        params = dict(params)
        params['id'] = posterId
        #url = f"{self.endpoint}/api/link"
        #修改地址
        url = "http://brickcn.xyz:5000/api/link"
        headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }
        payload = json.dumps(params)
        response = requests.request("POST", url, headers=headers, data=payload)
        link = response.json()['data']['url']  # type:str
        link='http://brickcn.xyz:5000/'+link[link.index('v'):]
        if not link.startswith('http'):
            link = self.endpoint + link
            print('self.endpoint',self.endpoint)
        self.link = link
        print(self.link)
        return link

    def save(self, filename='tmp.jpg'):
        response = requests.request("GET", self.link)
        with open(filename, mode='wb') as f:
            f.write(response.content)

def win(paramsa):
    api = posterapi('http://brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
    paramsa = eval(paramsa['context'])
    #str(paramsa['times'])
    #params["profits"]=str(paramsa["profits"])
 
    params = {}
    params["times"]=str(paramsa["times"])
    params["profits"]=str(paramsa["profits"])+'$'
    params["brickDays"]=str(paramsa["brickDays"])
    params["howManyPixiu"]=str(paramsa["howManyPixiu"])
    params["piXiuName"]=str(paramsa["piXiuName"])
    params["maifeiMax"]=str(paramsa["maifeiMax"])+'$'
    params["maifeiWho"]=str(paramsa["maifeiWho"])
    params["maifeiPeak"]=str(paramsa["maifeiPeak"])+'$'

    url = api.getUrl('9', params)
    print(url)
    return url
    #api.save()
def lose(paramsa):
    api = posterapi('http://brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
    {'months': 12, 'times': 4073, 'profitsMax': 6709, 'profitsMin': 442, 'minName': 'EKTA', 'maxName': 'FFC', 'brickDays': 232, 'maifeiWho': 'JF', 'maifeiPeak': 131020213, 'profits': 7445, 'maifei': 132615274, 'winne': 1, 'howManyPixiu': 51, 'piXiuName': 17587089259908986131928, 'piXiuPrice': 'BSC-USD', 'maifeiMax': 34512846280213397504}
    params = {}
    params["times"]=str(paramsa["times"])
    params["profits"]=str(paramsa["profits"])+'$'
    params["brickDays"]=str(paramsa["brickDays"])
    params["profitsMin"]=str(params["profitsMin"])+'$'
    params["howManyPixiu"]=str(params["howManyPixiu"])
    params["piXiuName"]=str(params["piXiuName"])
    params["piXiuPrice"]=str(params["piXiuPrice"])+'$'
    params["maifeiWho"]=str(params["maifeiWho"])
    params["maifeiPeak"]=str(params["maifeiPeak"])+'$'
    '''
    params = {}
    params["times"]="0"
    params["profits"]="0$"
    params["brickDays"]="0"
    params["profitsMin"]="Null"
    params["howManyPixiu"]="0"
    params["piXiuName"]="Null"
    params["piXiuPrice"]="0$"
    params["maifeiWho"]="Null"
    params["maifeiPeak"]="0$"
    '''
    url = api.getUrl('8', params)
    print(url)
    return url
if __name__ == '__main__':
    win()
    lose()