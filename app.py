from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
import time



class WhatsappAutomate:
    def __init__(self,url,sendTo):
        self.driver = webdriver.Chrome('./chromedriver')
        self.contact=sendTo
        self.driver.get(url) 
        time.sleep(10)
        print("All systems armed")
    
    def sendMessage(self,messageList):
        selected_contact = self.driver.find_element_by_xpath("//span[@title='"+self.contact+"']")
        selected_contact.click()
        for message in messageList:
            inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
            input_box = self.driver.find_element_by_xpath(inp_xpath)
            time.sleep(2)
            input_box.send_keys(message + Keys.ENTER)
            time.sleep(2)


def main():
    whatsappAutomate=WhatsappAutomate("https://web.whatsapp.com","Contact name")
    messageList=["Test message from from python","Hello world!"]
    whatsappAutomate.sendMessage(messageList)
    

if __name__ == "__main__":
    main()