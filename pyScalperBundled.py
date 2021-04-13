#using selenium, chrome 89, chromedriver 89, pyinstaller
#chromedriver.exe is placed in the source folder
#pyinstaller --add-data "chromedriver.exe;chromedriver" pyScalperBundled.py

import time, os, sys
from selenium import webdriver


if getattr(sys, 'frozen', False):
	#executed as a bundled exe, driver is in the extracted folder
	chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver/chromedriver.exe")
	browser = webdriver.Chrome(chromedriver_path)
else:
	#Using Chrome
	browser = webdriver.Chrome('chromedriver')
	#Bestbuy RTX 3070 page, replace with your desired video card page
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442&irclickid=3m51et3B8xyLRIQ0RHQK3XRkUkEScRQQiyHoTw0&irgwc=1&ref=198&loc=Troposphere%20LLC&acampID=0&mpid=62662")

#test an in stock
#browser.get("https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599")

buyButton = False

while not buyButton:

	try:
		#If this works then button is not pytopen might have to update every so often
		addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

		# Button not activated, let em know
		print("Item Sold out... refreshing in 10")

		#Refresh after a delay
		time.sleep(10)
		browser.refresh()

	except:

		addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

		#click that button
		print("Added to cart! Olawdy")
		addToCartBtn.click()
		buyButton = True

