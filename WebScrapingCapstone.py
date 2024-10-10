from bs4 import BeautifulSoup
import requests
from formFillerBot import DataEntryBot
##########################################################################################################
URL = 'https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(URL)
content = response.text
##########################################################################################################
soup = BeautifulSoup(content, 'html.parser')
houses = soup.select(selector='.StyledCard-c11n-8-84')
house_list = []
for i in range(len(houses)):
    house_address = houses[i].select_one(selector="a").text.strip()
    house_link = houses[i].select_one(selector="a").attrs['href']
    house_rent = houses[i].select_one(selector='.PropertyCardWrapper__StyledPriceLine').text.split("+")[0]
    house_list.append({"address":house_address, 'rent': house_rent, 'href':house_link})
##########################################################################################################
my_boat = DataEntryBot()
##########################################################################################################
for item in house_list:
    my_boat.chrome_opener()
    my_boat.enter_data(item)
##########################################################################################################
my_boat.close_chrome()
##########################################################################################################


link_to_excel_sheet = "https://docs.google.com/spreadsheets/d/1TDQlJ0PQswu4-jezodbelLSHZ58Os_VfhMutB6DY1xY/edit?usp=sharing"