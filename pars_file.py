import requests
import time
import undetected_chromedriver
from bs4 import BeautifulSoup


try:
    driver = undetected_chromedriver.Chrome()
    driver.get("")
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



# url = ""
#
# headers ={
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text


# with open("index.html", 'w') as file:
#     file.write(src)
