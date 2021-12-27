import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import csv
from random import randrange
import time


print = pprint

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"


# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
# }

# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)



# with open("index.html", "r", encoding ="utf8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")

# all_products = soup.find_all(class_="mzr-tc-group-item-href")

# all_categories_dict = {}

# for item in all_products:
# 	item_text = item.text
# 	item_href = "https://health-diet.ru" +  item.get("href")
	
# 	all_categories_dict[item_text] = item_href


# with open("all_categories_dict.json", "w", encoding ="utf8") as file:
# 	json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json", encoding ="utf8") as file:
	all_catigories = json.load(file)


count = 0
iteration_count = int(len(all_catigories)) - 1 
print(f"all iteration count - {iteration_count}")	

for category_name, category_href in all_catigories.items():

	rep = [","," ","-","'"]
	for item in rep:
		if item in category_name:
			category_name = category_name.replace(item, "_")

	req = requests.get(category_href)
	src = req.text


	with open(f"html/{count}_{category_name}.html", "w" ,encoding="utf8") as file:
		file.write(src)		

	with open(f"html/{count}_{category_name}.html" ,encoding="utf8") as file:
		src = file.read()

	soup = BeautifulSoup(src, "lxml")	

	#check if its product sheet
	alert_block = soup.find(class_="uk-alert-danger")
	if alert_block is not None:
		continue

	#create a title of our table
	table_head = soup.find(class_ = "mzr-tc-group-table").find("tr").find_all("th")

	product = table_head[0].text
	calories = table_head[1].text
	proteins = table_head[2].text
	fats = table_head[3].text
	carbohydrates = table_head[4].text

	
	with open(f"html/{count}_{category_name}.csv", "w") as file:
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

	#got all product paametrs	
	product_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

	product_info = []

	for item in product_data:
		product_tds = item.find_all("td")

		title = product_tds[0].find("a").text
		calories = product_tds[1].text
		proteins = product_tds[2].text
		fats = product_tds[3].text
		carbohydrates = product_tds[4].text

		product_info.append(
			{
				"Title" : title,
				"Calories" : calories,
				"Proteins" : proteins,
				"Fats" : fats,
				"Carbohydrates" : carbohydrates
			}
		)

		with open(f"html/{count}_{category_name}.csv", "a") as file:
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

	with open(f"html/{count}_{category_name}.json", "a", encoding ="utf8") as file:
		json.dump( product_info,file, indent=4, ensure_ascii=False)		

	count +=1 
	print(f"{count} iteration {category_name} has been written")
	iteration_count -=1

	if iteration_count == 0:
		print("Done")
		break

	print(f"{iteration_count} iteration left")
	time.sleep(randrange(2,4))