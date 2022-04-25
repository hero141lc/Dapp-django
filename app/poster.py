import requests
import json
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
        url = "{self.endpoint}/api/link"
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
s
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
    params["howManyPixiu"]=str(paramsa["howManyPixiu"])
    params["piXiuName"]=str(paramsa["piXiuName"])
    params["maifeiMax"]=str(paramsa["maifeiMax"])+'$'
    params["maifeiWho"]=str(paramsa["maifeiWho"])
    params["maifeiPeak"]=str(paramsa["maifeiPeak"])+'$'

    url = api.getUrl('9', params)
    print(url+'.jpg')
    return url+'.jpg'
    #api.save()
def lose(paramsa):
    api = posterapi('http://brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
    paramsa = eval(paramsa['context'])
    params = {}
    params["times"]=str(paramsa["times"])
    params["profits"]=str(paramsa["profits"])+'$'
    params["brickDays"]=str(paramsa["brickDays"])
    if "profitsMin" in params:
        params["profitsMin"]=str(params["profitsMin"])+'$'
    else:
        params["profitsMin"]="0$"
    params["howManyPixiu"]="0$"
    params["piXiuName"]="0$"
    params["piXiuPrice"]="0$"

    if "maifeiWho" in params:
        params["maifeiWho"]=str(params["maifeiWho"])
    else:
        params["maifeiWho"]=""

    if "maifeiPeak" in params:
        params["maifeiPeak"]=str(params["maifeiPeak"])+'$'
    else:
        params["maifeiPeak"]="0$"    
    
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
    print(url+'.jpg')
    return url+'.jpg'
if __name__ == '__main__':
    win()
    lose()