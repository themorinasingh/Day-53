import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DataEntryBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.url = "https://forms.gle/fmZJiPFuAkBQBeBt8"
        pass

    def chrome_opener(self):
        self.driver.get(self.url)


    def enter_data(self,dict):
        time.sleep(10)
        try:
            items = self.driver.find_elements(By.CLASS_NAME, value='whsOnd')

            address_bar = items[0]
            address_bar.send_keys(dict['address'])
            ########################################################################################################
            rent_bar = items[1]
            rent_bar.send_keys(dict['rent'])
            ########################################################################################################
            link_bar = items[2]
            link_bar.send_keys(dict['href'])
            ########################################################################################################
            time.sleep(2)
            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            submit_button.click()

        except Exception as e:
            print(f"An error occurred during data entry: {e}")

    def close_chrome(self):
        self.driver.quit()

# botty = DataEntryBot()
# botty.chrome_opener()
# botty.enter_data({'address': '747 Geary St, Oakland, CA 94609', 'rent': '$2,895', 'href': 'https://www.zillow.com/b/747-geary-street-oakland-ca-CYzGVt/'})
# time.sleep(10)
# botty.close_chrome()