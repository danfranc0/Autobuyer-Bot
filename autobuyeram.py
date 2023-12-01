from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import infoam

# make sure this path is correct
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# AMAZON

# edit this link and MSRP to fit your target product
URL = "https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=sr_1_13?dchild=1&keywords=3060+ti&qid=1607791119&s=electronics&sr=1-13"
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
