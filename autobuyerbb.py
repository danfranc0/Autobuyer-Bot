from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import infobb

# make sure this path is correct
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# BEST BUY

# change link here
URL = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-gaming-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442484.p?skuId=6442484"
driver.get(URL)

isComplete = False

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        print("refreshing page")
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        # add to cart
        atcBtn.click()

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
        )
        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")

        # fill in email and password
        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(infobb.email)

        pwField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(infobb.password)

        # click sign in button
        signInBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button"))
        )
        signInBtn.click()
        print("Signing in")

        # fill in card cvv
        cvvField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvField.send_keys(infobb.cvv)
        print("Attempting to place order")

        # place order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()
        
        isComplete = True
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(URL)
        print("Error - restarting bot")
        continue

print("Order successfully placed")
