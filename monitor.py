from bs4 import BeautifulSoup
from selenium import webdriver

ebook_list = []
new_ebook = input("Enter the ebook's title: ")
ebook_list.append(new_ebook)


for ebook in ebook_list:
    ebook = ebook.replace(" ", "+")
    url = f"https://www.amazon.com/s?k={ebook}&ref=nb_sb_noss_2"
    print(url)



driver = webdriver.Chrome(r'A:Python\chromedriver_win32\chromedriver.exe')
source = driver.get(url)