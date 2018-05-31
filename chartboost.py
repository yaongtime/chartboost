import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_element_present(browser, wait_type, wait_keys):

    print('Wait for element by: %s' % wait_keys)
    while True:
        try:
            return WebDriverWait(browser, 60).until(EC.presence_of_element_located((wait_type, wait_keys)))

        except TimeoutException:
            print("Wait Try: %s" % wait_keys)

        except:
            print("Unexpected error")
            raise

# "campain_app.txt"
# "campaign_highest.txt"

def get_campaign_list(file_name):
    f = open(file_name, "r")
    high_name = []
    for i in f:
        high_name.append(i[0:-1])
    f.close()
    return (high_name)

def all_active_DD(browser):
    #clicl list "Type"
    wait_element_present(browser, By.CSS_SELECTOR, '#s2id_autogen29 > a > span.select2-arrow > b').click()

    # CHOOSE 'DD'
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="select2-results-30"]/li[3]').click()

    #click list 'STATE'
    wait_element_present(browser, By.CSS_SELECTOR, '#s2id_autogen27 > a > span.select2-arrow > b').click()

    # CHOOSE 'Active'
    time.sleep(2)
    browser.find_element_by_css_selector('#select2-results-28 > li:nth-child(2)').click()

    #all active DD
    all_active_DD1=browser.find_elements_by_class_name('inherit')

    return(all_active_DD1)


def change_campaign_to_high(browser):
    #choose all app in studio
    wait_element_present(browser, By.XPATH, '//*[@id="direct-publisher__basic-settings__publishing-apps__actions--select-apps"]').click()
    time.sleep(5)
    wait_element_present(browser, By.XPATH, '/html/body/div[5]/div[1]/h3[1]/div/div/div[1]').click()
    #confirm
    wait_element_present(browser, By.XPATH, '//*[@id="direct-publisher__basic-settings__publishing-apps__promote-in__actions--confirm"]').click()

    time.sleep(2)
    #move mouse
    browser.execute_script("window.scrollBy(0, 200)")
    browser.find_element_by_css_selector('#direct-publisher__advanced-settings__summary--section-toggle-button').click()
    #choose highest list(test)
    browser.find_element_by_css_selector('#direct-publisher__advanced-settings__priority__actions--15').click()
    #移动到页面最底部  
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("dibu_________________________________________________________")
    time.sleep(3)
    #cancel
    # wait_element_present(browser, By.XPATH, '//*[@id="direct-publisher__enabled-actions--cancel"]').click()
    botton=browser.find_elements_by_id('direct-publisher__enabled-actions--cancel')
    botton[-1].click()

def match_app(browser):
    for i in get_campaign_list("campain_app.txt"):
        for j in all_active_DD(browser):
            if j.text[0:(i.text.find('-'))]==i:
                j.click()
                change_campaign_to_high(browser)
                break


browser = webdriver.Chrome()

browser.get("https://dashboard.chartboost.com/login")
browser.maximize_window()

# wait for web load login page
wait_element_present(browser, By.XPATH, "/html/body/div/div/div/div[1]/form/input")

browser.find_element_by_name("email").send_keys("xxxxxxxxx")
browser.find_element_by_name("password").send_keys("xxxxxxxx")
browser.find_element_by_xpath("/html/body/div/div/div/div[1]/form/input").click()

# wait for login sucess
wait_element_present(browser, By.XPATH, '//*[@id="navbar__logo"]')

browser.get('https://dashboard.chartboost.com/all/campaigns/publishing')

match_app(browser)


# # find App Icon XPATH
# wait_element_present(browser, By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/table/thead/tr/th[1]/div')
# browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]").click()

# #clicl list "Type"
# wait_element_present(browser, By.CSS_SELECTOR, '#s2id_autogen29 > a > span.select2-arrow > b').click()

# # CHOOSE 'DD'
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="select2-results-30"]/li[3]').click()

# #click list 'STATE'
# wait_element_present(browser, By.CSS_SELECTOR, '#s2id_autogen27 > a > span.select2-arrow > b').click()

# # CHOOSE 'Active'
# time.sleep(2)
# browser.find_element_by_css_selector('#select2-results-28 > li:nth-child(2)').click()


# # # CHOOSE 'Needs Confirmation'
# # time.sleep(2)
# # browser.find_element_by_css_selector('#select2-results-28 > li:nth-child(6)').click()

# app_campaign=browser.find_elements_by_class_name('inherit')


# for i in app_campaign:
#     if i.text[0:(i.text.find('-'))] in campaign_high():
#         i.click()
#         print("click------------------------------------------")
#         # choose all app



        
#         wait_element_present(browser, By.XPATH, '//*[@id="direct-publisher__basic-settings__publishing-apps__actions--select-apps"]').click()
#         time.sleep(5)
#         wait_element_present(browser, By.XPATH, '/html/body/div[5]/div[1]/h3[1]/div/div/div[1]').click()
#         #confirm
#         wait_element_present(browser, By.XPATH, '//*[@id="direct-publisher__basic-settings__publishing-apps__promote-in__actions--confirm"]').click()

#         time.sleep(2)
#         #move mouse
#         browser.execute_script("window.scrollBy(0, 200)")
#         browser.find_element_by_css_selector('#direct-publisher__advanced-settings__summary--section-toggle-button').click()
#         #choose highest list(test)
#         browser.find_element_by_css_selector('#direct-publisher__advanced-settings__priority__actions--15').click()
#         #移动到页面最底部  
#         time.sleep(2)
#         browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#         print("dibu_________________________________________________________")
#         time.sleep(3)
#         #cancel
#         # wait_element_present(browser, By.XPATH, '//*[@id="direct-publisher__enabled-actions--cancel"]').click()
#         botton=browser.find_elements_by_id('direct-publisher__enabled-actions--cancel')
#         botton[-1].click()
        

# c = [i.text[0:(i.text.find("-"))] for i in app_campaign]


# for app in c:
#     if app in campaign_high():
#         print("high:",app)

#     elif app in campaign_highest():
#         print("highest",app)
#     else:
#         print("other:",app)



input("input anythng to exit")
browser.quit()

# <a class="inherit" href="/all/campaigns/5af1358c24941e0c06fed16f">HUGS0249-20180510-SHAKE</a>

