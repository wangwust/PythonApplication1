from selenium import webdriver
import time

#driver = webdriver.PhantomJS("C:\Python27\phantomjs.exe")
driver = webdriver.Firefox()
def run():
    loginSuccess = login("http://www.cpkk7.com/login")
    if bool(loginSuccess) == False:
        print("登录失败")
        return

    driver.implicitly_wait(3)
    for i in range(0,10):
        result = get_openresult("http://www.cpkk7.com/lottery/K3/1407")

        if result == "":
            print("抓取失败")
        else:
            print(result)
        time.sleep(60)

def login(url): #��¼
    try:
        driver.get(url)

        username = driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[1]/input")
        username.send_keys('dw9527')

        password = driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[2]/input")
        password.send_keys('qq123456')

        button = driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[3]/a[1]")
        button.click()

        return True
    except Exception,e:
        print(e.message)
        return False

def get_openresult(url):
    try:
        driver.get(url)
        html = driver.page_source
    
        result = driver.find_element_by_class_name("ResultsList").text
        return result
    except Exception,e:
        print(e.message)
        return ""


run()
driver.quit()
