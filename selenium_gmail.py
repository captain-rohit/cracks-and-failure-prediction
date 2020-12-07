import undetected_chromedriver
undetected_chromedriver.install()
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from fake_useragent import UserAgent

chrome_path  = '/home/rohit/Downloads/chromedriver_linux64/chromedriver'
#this would be the path to the chromedriver exe on your system

# chrome_options = Options()
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# chrome_options.accept_untrusted_certs = True
# chrome_options.assume_untrusted_cert_issuer = True
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--allow-http-screen-capture")
# chrome_options.add_argument("--disable-impl-side-painting")
# chrome_options.add_argument("--disable-setuid-sandbox")
# chrome_options.add_argument("--disable-seccomp-filter-sandbox")
# chrome_options.add_argument("--enable-automation")
# chrome_options.add_argument('--user-agent="https://mail.google.com/" useragent="Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"')
# driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

# browser = webdriver.Firefox()
driver = Chrome()
driver.get("https://www.youtube.com/")
time.sleep(6)
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button").click()
element = driver.find_element_by_name("identifier")
print(element.is_displayed())
time.sleep(3)
element.send_keys("rohitrajak1907@gmail.com")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()

print(driver.title)