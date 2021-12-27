import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import csv
from random import randrange
import time



# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

# req = requests.get(url)
# # print(req.text)

# with open("index.html", "w", encoding="UTF8") as file:
# 	file.write(req.text)

# src = req.text

# soup = BeautifulSoup(src, "lxml")

# all_products = soup.find_all(class_="mzr-tc-group-item-href")

# all_categories_dict = {}

# for elem in all_products:
# 	item_name = elem.text
# 	item_href = "https://health-diet.ru" + elem.get("href")

# 	all_categories_dict[item_name] = item_href

# with open("all_products.json", "w", encoding="utf-8") as file:
# 	json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_products.json", encoding="utf-8") as file:
	all_catigories = json.load(file)

count = 0
for category_name, category_href in all_catigories.items():

	
	req = requests.get(category_href)
	src = req.text

	with open(f"data/{count}_{category_name}.html", "w", encoding="utf-8") as file:
		file.write(src)

	soup = BeautifulSoup(src, "lxml")

	#check if its product sheet
	try:
		alert_block = soup.find(class_="uk-alert-danger")
	except 	AttributeError:
		print("page not found")
		continue

	try:
		table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
	except AttributeError:
		print("end")	
		break

	product = table_head[0].text
	calories = table_head[1].text			
	proteins = table_head[2].text			
	fats = table_head[3].text			
	carbohydrates = table_head[4].text

	with open(f"data/{count}_{category_name}.csv" , "w") as file:
		writer = csv.writer(file)
		writer.writerow(
			(
				product,
				calories,
				proteins,
				fats,
				carbohydrates
			)
		)

	product_info = []
	
	#got all product paametrs	
	product_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

	for item in product_data:
		product_data_td = item.find_all("td")
	
		title = product_data_td[0].find("a").text
		calories = product_data_td[1].text			
		proteins = product_data_td[2].text			
		fats = product_data_td[3].text			
		carbohydrates = product_data_td[4].text

		product_info.append(
			{
				"Title" : title,
				"Calories" : calories,
				"Proteins" : proteins,
				"Fats" : fats,
				"Carbohydrates" : carbohydrates
			}
		)

		with open(f"data/{count}_{category_name}.csv" , "a") as file:
			writer = csv.writer(file)
			writer.writerow(
				(
					title,
					calories,
					proteins,
					fats,
					carbohydrates
				)
			)

	with open(f"data/{count}_{category_name}.json", "w", encoding="utf-8") as file:
		json.dump(product_info, file, indent=4, ensure_ascii=False)


			


	count+=1