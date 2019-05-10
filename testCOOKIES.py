from selenium import webdriver

def check_cookies():
    driver = webdriver.Edge(executable_path='C:\\Users\\narya\\Documents\\MicrosoftWebDriver.exe')
    driver.get('https://bbs.saraba1st.com/2b/thread-1814684-1-1.html')
    driver.implicitly_wait(3)
    print(driver.get_cookies())
    saved_cookies = driver.get_cookies()
    return saved_cookies

check_cookies()