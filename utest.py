import HtmlTestRunner
import unittest
import requests
from datetime import datetime

f = open('test.log', 'w+')

def saveResult(name, url, result):
    f.write('Test name:' + str(name) + '\n')
    f.write('Test URL:' + str(url) + '\n')
    f.write('Test result:' + str(result) + '\n')
    f.write('Test result: ' + str(datetime.now()) + '\n')
    f.write('---------------------------------------------\n ')

def checkServiceForWord(url, keyword):
    try:
        x = requests.get(url)
        print(x.text)
        serverStatus=1
        if keyword in x.text:
            print("found keyword")
            return True
    except:
        print("error")
        return False
    

# def test_twoValuesAreEqual(self):
#     value1=True
#     value2=checkServiceForWord('http://localhost:5000/', 'getProducts')
#     self.assertEqual(value1, value2)


# class TestGetProducts(unittest.TestCase):
#     def test_twoValuesAreEqual(self):
#         value1=True
#         value2=checkServiceForWord('http://localhost:5000/getProducts', 'Jam')
#         self.assertEqual(value1, value2)


# class TestGetTitles(unittest.TestCase):
#     def test_twoValuesAreEqual(self):
#         value1=True
#         value2=checkServiceForWord('http://localhost:5000/getTitles', 'Jam')
#         self.assertEqual(value1, value2)


# class TestInsertProducts(unittest.TestCase):
#     def test_twoValuesAreEqual(self):
#         value1=True

#         value2=checkServiceForWord('http://localhost:5000/insertProduct?title=Tea&price=4.50&id=5', 'inserted')
#         self.assertEqual(value1, value2)




name = 'TestRoot'
url = 'http://localhost:5000/'
result = checkServiceForWord(url, 'getProducts')
saveResult(name, url, result)

name = 'TestInsertProducts'
url = 'http://localhost:5000/insertProduct?title=Tea&price=4.50&id=5'
result = checkServiceForWord(url, 'inserted')
saveResult(name, url, result)


name = 'TestInsertProducts'
url = 'http://localhost:5000/insertProduct?title=Jam&price=4.50&id=5'
result = checkServiceForWord(url, 'inserted')

name = 'TestGetProducts'
url = 'http://localhost:5000/getProducts'
result = checkServiceForWord(url, 'Jam')
saveResult(name, url, result)



name = 'TestGetTitles'
url = 'http://localhost:5000/getTitles'
result = checkServiceForWord(url, 'Jam')
saveResult(name, url, result)




f.close()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_results'))
