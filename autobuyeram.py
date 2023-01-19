from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import infoam

# make sure this path is correct
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# AMAZON

RTX3070LINK1 = "https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=sr_1_13?dchild=1&keywords=3060+ti&qid=1607791119&s=electronics&sr=1-13"
RTX3070LINK2 ="https://www.amazon.com/MSI-RTX-3060-Ti-Architecture/dp/B08P2D3JSG/ref=sr_1_1?dchild=1&keywords=3060+ti&qid=1607796489&s=electronics&sr=1-1"
RTX3070LINK3 = "https://www.amazon.com/EVGA-08G-P5-3755-KR-GeForce-Cooling-Backplate/dp/B08L8L71SM/ref=sr_1_6?dchild=1&keywords=3060+ti&qid=1607796489&s=electronics&sr=1-6"
R5600XLINK = "https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=as_li_ss_tl?_encoding=UTF8&psc=1&refRID=46SVCMBX83Z462G6B1R7&ascsub&linkCode=sl1&tag=fixitservices-20&linkId=4a7a15114b861372c3e24f9bb3547fd7&language=en_US"
R5800XLINK = "https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK/ref=as_li_ss_tl?_encoding=UTF8&pd_rd_i=B0815XFSGK&pd_rd_r=3088b22b-0dbb-4619-afd4-de063674e0cf&pd_rd_w=UfUsG&pd_rd_wg=NUvoL&pf_rd_p=7b36d496-f366-4631-94d3-61b87b52511b&pf_rd_r=ABTR9BBYDMMKRQ9G5K9C&psc=1&refRID=ABTR9BBYDMMKRQ9G5K9C&linkCode=sl1&tag=fixitservices-20&linkId=d6db18b428db28299671f47d2bb09c9b&language=en_US"
TEST = "https://www.amazon.com/GAMEMAX-Supply-Modular-Certified-Addressable/dp/B088QYVBBH/ref=sr_1_6?dchild=1&keywords=3060+ti&qid=1607787461&sr=8-6"

URL = RTX3070LINK2
MSRP = 650

driver.get(URL)

isComplete = False

while not isComplete:
    # find buy now button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#buy-now-button"))
        )
    except:
        print("refreshing page")
        driver.refresh()
        continue

    print("Buy now button found")

    priceEl = driver.find_element_by_id("price_inside_buybox")
    price = priceEl.text[1:7]
    print(price)

    if int(float(price)) < MSRP:
        print(int(float(price)))

        try:
            # buy now
            atcBtn.click()
            print("Worked! buying now")

            # fill in email
            emailField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ap_email"))
            )
            emailField.send_keys(infoam.email)

            # click continue button
            continueBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))
            )
            continueBtn.click()
            print("Entered email")

            # fill in password
            pwField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ap_password"))
            )
            pwField.send_keys(infoam.password)

            # sign in
            signInBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#signInSubmit"))
            )
            signInBtn.click()

            # complete checkout
            placeOrderBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "bottomSubmitOrderButtonId"))
            )
            placeOrderBtn.click()

            isComplete = True
        except:
            # try again w/same link
            driver.get(URL)
            print("Error - restarting bot")
            continue
    else:
        print("over MSRP, restarting")
        driver.refresh()
        continue

print("Order successfully placed")
