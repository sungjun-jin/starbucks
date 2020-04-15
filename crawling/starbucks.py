import requests
import csv
import time

from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.starbucks.co.kr/menu/drink_list.do'
file = open('starbucks.csv',mode='w',encoding='UTF-8',newline='')
writer = csv.writer(file)
writer.writerow(['name','en_name','size','kcal','sodium','sat_fat','sugar','protein','caffeine','allergy','image','desc_top','desc_bottom'])

def get_categories():
	
	category_list = []
	
	req = requests.get(URL)
	html = req.text
	
	soup = BeautifulSoup(html,'html.parser')
	product_soup = soup.find('div',{'class' : 'product_list'})
	category_soup = product_soup.find_all('dt')

	for category in category_soup:
	    category_list.append(category.find('a').string)

	print(category_list)    

def get_product_code():

	product_code_list = []
	driver = webdriver.Chrome('/home/sungjunjin/chromedriver')

	driver.get(URL)
	product_codes = driver.find_elements_by_class_name('goDrinkView')

	for product_code in product_codes:
		product_code_list.append(product_code.get_attribute('prod'))

	return product_code_list

def get_product_info(product_code_list):
	
	for product_code in product_code_list:
		ID = product_code	
		DRINK_URL = f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={ID}'
		driver = webdriver.Chrome('/home/sungjunjin/chromedriver')
		driver.get(DRINK_URL)

		name, en_name = driver.find_elements_by_tag_name('h4')[0].text.split('\n')
		size = driver.find_element_by_id('product_info01').text
		#amount = amount.split(' ' )
		#ml = amount[1]
		#oz = amount[2][1:]
		description_top = driver.find_element_by_class_name('t1').text
		description_bottom = driver.find_element_by_class_name('product_view_wrap2').text
		description_bottom = description_bottom.split('\n')[0]
		kcal = driver.find_element_by_class_name('kcal').text
		kcal = kcal.split('\n')[1]	
		sat_fat = driver.find_element_by_class_name('sat_FAT').text
		sat_fat = sat_fat.split('\n')[1]
		protein = driver.find_element_by_class_name('protein').text
		protein = protein.split('\n')[1]
		sodium = driver.find_element_by_class_name('sodium').text 
		sodium = sodium.split('\n')[1]	
		sugars = driver.find_element_by_class_name('sugars').text
		sugars = sugars.split('\n')[1]	
		caffeine = driver.find_element_by_class_name('caffeine').text
		caffeine = caffeine.split('\n')[1]
		allergy = driver.find_element_by_class_name('product_factor').text.split(': ')
		allergy = allergy[-1]
		image = driver.find_element_by_xpath('//*[@id="product_thum_wrap"]/ul/li/a/img').get_attribute('src')
		
		writer.writerow([name,en_name,size,kcal,sodium,sat_fat,sugars,protein,caffeine,allergy,image,description_top,description_bottom])
		driver.close()

	
get_product_info(get_product_code())


