from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time



with open('credentials.json') as file:
    credentials = json.load(file)

login = credentials['login']
password = credentials['password']
url = "https://intranet.ucll.be/Shibboleth.sso/Login?target=https%3A%2F%2Fintranet.ucll.be%2Fnl%3Fq%3Dshib_login%2Fhome"


driver = webdriver.Chrome()
driver.get(url)

# Log in
u = driver.find_element_by_name('username')
u.send_keys(login)
elt = driver.find_element_by_name('password')
elt.send_keys(password)
elt.send_keys(Keys.RETURN)

# Filter important messages
elt = driver.find_element_by_css_selector(r"a.trigger_important")
elt.click()
time.sleep(1)

# Find titles
elts = driver.find_elements_by_css_selector(r".node-title")
new_titles = [ elt.text for elt in elts ]

# Close browser
driver.close()


with open('titles.txt', encoding='utf-8') as file:
    titles = [ line.strip() for line in file.readlines() ]
    titles_set = set(titles)


for title in reversed(new_titles):
    if title not in titles_set:
        titles.insert(0, title)

with open('titles.txt', 'w', encoding='utf-8') as file:
    for title in titles:
        print(title, file=file)
