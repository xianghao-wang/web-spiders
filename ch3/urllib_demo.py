from urllib import request, parse

url = "http://httpbin.org/post"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'HOST': 'httpbin.org'
}
data = bytes(parse.urlencode({
    'name': 'Xianghao' 
}), encoding='utf8')

req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)

print(response.read().decode('utf-8'))