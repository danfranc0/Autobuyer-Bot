# Python Autobuyer Bot
* autobuyeram.py and infoam.py for Amazon
* autobuyerbb.py and infobb.py for BestBuy

## About
Autobuyer was developed as a personal project in quarantine in 2020 during the GPU shortage. Initially developed to buy out of stock Nvidia graphics cards, Autobuyer will take in a link to an out of stock product listed on Amazon or BestBuy and purchase that product when it goes in stock. Use files with the “am” suffix for Amazon links and files with the “bb” suffix for BestBuy links. Happy buying!

## Disclaimer
* BestBuy bot requires that you provide the cvv of the credit card linked to your BestBuy account
* Amazon bot requires that you set the MSRP variable to the current retail price of product to prevent the bot from buying overpriced items

## Prerequisites
* Download and setup [ChromeDriver](https://chromedriver.chromium.org/downloads) to automate the browser
* Download and setup [Selenium WebDriver for Python](https://www.selenium.dev/downloads/) for device input
* Ensure PATH variable on line 9 is the correct location of chromedriver.exe in your device
  
## How to Use
1. Input your account information into infoam.py or infobb.py
2. Set up link variable with url to the product and set URL variable equal to that link variable
3. Run script :)
