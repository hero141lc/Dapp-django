import requests
import json
import datetime
import time

class posterapi():

    def __init__(self, endpoint: str, token: str):
        if endpoint.endswith("/"):
            endpoint = endpoint[0:-1]
        self.endpoint = endpoint
        self.token = token

    def getUrl(self, posterId: str, params: dict = {}):
        start_time = time.time()
        params = dict(params)
        params['id'] = posterId
        url = f"{self.endpoint}/api/link"
        print("getUrl:",url)
        headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }
        payload = json.dumps(params)
        response = requests.request("POST", url, headers=headers, data=payload)
        link = response.json()['data']['url']  # type:str
        if not link.startswith('http'):
            link = self.endpoint + link
        self.link = link
        end_time = time.time()
        print("geturl const: {:.2f}s".format(end_time - start_time))
        return link

    def save(self, filename='tmp.jpg'):
        response = requests.request("GET", self.link)
        with open(filename, mode='wb') as f:
            f.write(response.content)

def win(paramsa):
    api = posterapi('http://poster.brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
    paramsa = eval(paramsa['context'])
    #str(paramsa['times'])
    #params["profits"]=str(paramsa["profits"])
    params = {}
    params["times"]=str(paramsa["times"])
    params["profits"]=str(paramsa["profits"])+'$'
    params["brickDays"]=str(paramsa["brickDays"])
    params["firstTime"]=str(paramsa["firstTime"])
    params["firstCoin"]=str(paramsa["firstCoin"])
    params["maifeiMax"]=str(paramsa["buyAmountOfMax_Maifei"])+'$'
    params["maifeiWho"]=str(paramsa["maifeiWho"])
    params["maifeiPeak"]=str(paramsa["maifeiPeak"])+'$'
    params["firstPrice"]=str(paramsa["firstPrice"])+'$'
    params['firstTime'] = str(params['firstTime']).replace('-', '年', 1)
    params['firstTime'] = params['firstTime'].replace('-', '月', 1)+'日'

    
    url = api.getUrl('11', params)
    print(url+'.jpg')
    return url+'.jpg'
    #api.save()
def lose(paramsa):
    api = posterapi('http://poster.brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
    paramsa = eval(paramsa['context'])
    params = {}
    params["times"]=str(paramsa["times"])
    params["profits"]=str(paramsa["profits"])+'$'
    params["brickDays"]=str(paramsa["brickDays"])
    params["firstTime"]=str(paramsa["firstTime"])
    params["firstCoin"]=str(paramsa["firstCoin"])
    params["maifeiMax"]=str(paramsa["buyAmountOfMax_Maifei"])+'$'
    params["maifeiWho"]=str(paramsa["maifeiWho"])
    params["maifeiPeak"]=str(paramsa["maifeiPeak"])+'$'
    params["firstPrice"]=str(paramsa["firstPrice"])+'$'

    
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
    url = api.getUrl('12', params)
    print(url+'.jpg')
    return url+'.jpg'
if __name__ == '__main__':
    win()
    lose()