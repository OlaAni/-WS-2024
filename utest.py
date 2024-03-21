import HtmlTestRunner
import unittest
import requests
import subprocess
import time

f = open('test.log', 'w+')

def saveResult(name, url, result):
    f.write('Test name:' + str(name) + '\n')
    f.write('Test URL:' + str(url) + '\n')
    f.write('Test result:' + str(result) + '\n')
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
    

class TestRoot(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        value2=checkServiceForWord('http://localhost:5000/', 'getProducts')
        self.assertEqual(value1, value2)


class TestGetProducts(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        value2=checkServiceForWord('http://localhost:5000/getProducts', 'Jam')
        self.assertEqual(value1, value2)


class TestGetTitles(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        value2=checkServiceForWord('http://localhost:5000/getTitles', 'Jam')
        self.assertEqual(value1, value2)


class TestInsertProducts(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True

        value2=checkServiceForWord('http://localhost:5000/insertProduct?title=Tea&price=4.50&id=5', 'inserted')
        self.assertEqual(value1, value2)




# name = 'Test 1'
# url = 'https://jsonplaceholder.typicode.com/todos/1'
# result = checkServiceForWord(url, 'userId')
# saveResult(name, url, result)

f.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_results'))
