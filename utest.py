import HtmlTestRunner
import unittest
import requests
from datetime import datetime
import os

os.makedirs('test_results', exist_ok=True)
f = open('test_results/test.log', 'w+')

def saveResult(name, url, result):
    f.write('Test name:' + str(name) + '\n')
    f.write('Test URL:' + str(url) + '\n')
    f.write('Test result:' + str(result) + '\n')
    f.write('Test result: ' + str(datetime.now()) + '\n')
    f.write('---------------------------------------------\n ')

def checkServiceForWord(url, keyword):
    try:
        x = requests.get(url, headers={"api-key":"92hosID3jX"})
        print(x.text)
        serverStatus=1
        if keyword in x.text:
            print("found keyword")
            return True
    except:
        print("error")
        return False
    

def checkServiceForWordpost(url, keyword):
    try:
        x = requests.post(url, headers={"api-key":"92hosID3jX"})
        # print(x.text)
        serverStatus=1
        if keyword in x.text:
            print("found keyword")
            return True
    except:
        print("error")
        return False


name = 'TestRoot'
url = 'http://localhost:5000/'
result = checkServiceForWord(url, 'getProducts')
saveResult(name, url, result)

name = 'TestInsertProducts'
url = 'http://localhost:5000/insertProduct?title=Tea&price=4.50&id=5'
result = checkServiceForWordpost(url, 'inserted')
saveResult(name, url, result)


name = 'TestInsertProducts'
url = 'http://localhost:5000/insertProduct?title=Jam&price=4.50&id=5'
result = checkServiceForWordpost(url, 'inserted')

name = 'TestGetProducts'
url = 'http://localhost:5000/getProducts'
result = checkServiceForWord(url, 'Jam')
saveResult(name, url, result)



name = 'TestGetTitles'
url = 'http://localhost:5000/getTitles'
result = checkServiceForWord(url, 'Jam')
saveResult(name, url, result)




f.close()

