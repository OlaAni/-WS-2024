import HtmlTestRunner
import unittest
import requests

# class TestStringMethods(unittest.TestCase):
#     def test_twoValuesAreEqual(self):
#         value1=True
#         value2=True
#         self.assertEqual(value1, value2)
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))

def saveResult(name, url, result):
    f = open('test.log', 'w+')
    f.write('Test name:' + str(name) + '\n')
    f.write('Test URL:' + str(url) + '\n')
    f.write('Test result:' + str(result) + '\n')
    f.write('---------------------------------------------\n ')
    f.close()



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
url = 'https://jsonplaceholder.typicode.com/todos/1'
result = checkServiceForWord(url, 'userId')

# Test 1
name = 'Test 1'
url = 'https://jsonplaceholder.typicode.com/todos/1'
result = checkServiceForWord(url, 'userId')
saveResult(name, url, result)

# # Test 2
# url = 'https://jsonplaceholder.typicode.com/todos/1'
# result = checkServiceForWord(url, '1')
# print(result)

