import HtmlTestRunner
import unittest
import requests

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
    


class TestStringMethods(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        value2=checkServiceForWord('http://localhost:5000/getProducts', 'Jam')
        self.assertEqual(value1, value2)



class TestGetTitles(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        value2=checkServiceForWord('http://localhost:5000/getTitles', 'Jam')
        self.assertEqual(value1, value2)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))