import requests
import json

class posterapi():

    def __init__(self, endpoint: str, token: str):
        if endpoint.endswith("/"):
            endpoint = endpoint[0:-1]
        self.endpoint = endpoint
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
        if not link.startswith('http'):
            link = self.endpoint + link
        self.link = link
        return link

    def save(self, filename='tmp.jpg'):
        response = requests.request("GET", self.link)
        with open(filename, mode='wb') as f:
            f.write(response.content)

def win(params):
    api = posterapi('http://brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
    '''
    params = {}
    params["times"]="0"
    params["profits"]="0$"
    params["brickDays"]="0"
    params["howManyPixiu"]="0"
    params["piXiuName"]="Null"
    params["maifeiMax"]="0$"
    params["maifeiWho"]="Null"
    params["maifeiPeak"]="0$"
    '''
    url = api.getUrl('9', params)
    print(url)
    return url
    #api.save()
def lose(params):
    api = posterapi('http://brickcn.xyz:5000/', 'ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv')
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