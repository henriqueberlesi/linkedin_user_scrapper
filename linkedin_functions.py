import time
import csv

def login(driver, email, password):
    driver.get("https://linkedin.com")
    driver.find_element_by_name("session_key").send_keys(email)
    driver.find_element_by_name("session_password").send_keys(password)
    driver.find_element_by_id("login-submit").click()

class Search:
    def __init__(self, user, driver):
        self.driver = driver
        self.user = user
        self.driver.get("https://www.linkedin.com/search/results/all/?keywords={username}".format(username=user))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        self._results = self.driver.find_elements_by_class_name("search-result__info")
        self.people = []
        self.get_positions()
    
    def get_positions(self):
        if len(self._results) == 0:
            return self.people.append({'query': self.user, 'name': 'sem resultados'})
        for people in self._results:
            name = people.find_element_by_class_name("actor-name").text
            link = people.find_element_by_class_name("search-result__result-link").get_attribute("href")
            position = people.find_element_by_class_name("subline-level-1").text
            region = people.find_element_by_class_name("subline-level-2").text
            profile = {
                'query': self.user,
                'name': name, 
                'region': region, 
                'position': position, 
                'url': link
                }
            self.people.append(profile)
    
    def save(self, file):
         with open(file, 'a') as file:
             w = csv.DictWriter(file, ['query', 'name', 'region','position', 'url'])
             w.writerows(self.people)
