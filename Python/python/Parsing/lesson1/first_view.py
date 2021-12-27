from bs4 import BeautifulSoup
import re


with open("index1.html") as file:
	src = file.read()

soup = BeautifulSoup(src, "lxml")

title = soup.title
# print(title) #show teg and all his capability
# print(title.string, '\n' ,title.text) #show only text of thr teg

teg_h1 = soup.find("h1") #show teg and his capscity
# if there are more than 1 tex show only first
# print(teg_h1)

tegs_h1 = soup.find_all("h1") #show list of all tegs h1 in html
# print(tegs_h1)

user__name = soup.find("div", class_ = "user__name").find("span") #show div -> span -> name
# print(user__name.text) 

user_info = soup.find("div",class_ = "user__info").find_all("span") #sll spans from "user_info"

for info in user_info:
	print(info.string)

social__networks = soup.find("div", class_ = "social__networks").find("ul").find_all("a") #sll a from "social__networks"

print()

for networt in social__networks:
	print(networt.text, networt.get("href"))
# networt.get("href") - get atribut "href"


#find_parent and find_parent - function that produse 
# fing inpormation to top on dives


post__div = soup.find(class_="post__text").find_parent("div", class_ = "user__post__info") #show specific teg
print(post__div) #show all div user__post__info

next_elem = soup.find(class_ = "post__title").find_next()
print("\n",next_elem) #show elem after teg div "post_title"

prev_elem = soup.find(class_ = "title_text").find_previous()
print("\n",prev_elem) #show elem befor teg h3 "title_text"


next_sibling = soup.find(class_ = "post__title").find_next_sibling() #show block after post title
#supose to be post__text
print("\n\n\n", next_sibling)

prev_sibling = soup.find(class_ = "post__text").find_previous_sibling() #show block before post title
#supose to be post__title
print("\n\n\n", prev_sibling)

some_links = soup.find(class_="some_links").find_all("a")
print("\n\n\n",some_links)

for link in some_links:
	print(link.get("data-attr"))
	print(link["data-attr"]) #the same as get()

find_a_by_text = soup.find("a", text=re.compile("clothes")) #show link by a piece of text using regular expression
print("n", find_a_by_text,"\n")

find_all_by_text = soup.find_all(text = re.compile(r"[Cc]lothes"))

print(find_all_by_text)