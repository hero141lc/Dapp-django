1 取token价格
2 按天存orm
BUG
1 value只有Bnb买的
2 最亏算法

log
name = Swap
Addrs 就是持有把
to from哪个是swap
wbnb
path
status success path is Token buy?oOr is cake /wbnb is sell?

有hash 有token 有钱包 有买卖 买卖多少 用什么卖的 买卖金额 有时间

设一个字典装to from
https://api.bscscan.com/api?module=account&action=tokentx&&address=0x6A3FD03803a9f17Ae4913B83E75D1850837e50D3&page=1&offset=50&startblock=0&endblock=99999999999&sort=asc&apikey=TFD2ZDC1W77QAXP38SF9I1Z6T34GBGIGUJ


重点：多用户数据库写入冲突


李治:
交易次数的文档：https://www.covalenthq.com/docs/api/#/0/Get%20transactions%20for%20address/USD/1

李治:
持币地址的文档： https://www.covalenthq.com/docs/api/#/0/Get%20token%20holders%20as%20of%20any%20block%20height/USD/1
通过大量查询来确定赤壁地址



李治:
流通总量，池子总量，每日交易量的文档：https://www.covalenthq.com/docs/api/#/0/Get%20Pancakeswap%20v2%20pools%20by%20address/USD/1
