import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import date, datetime, timedelta
import shutil
import wget
import time
import glob

#Descarga para El Heraldo de México
def download_heraldo():
  webdriver.get("https://issuu.com/elheraldodemexico")
  webdriver2.get("https://issuu.com/elheraldodemexico")
  time.sleep(2)
  webdriver.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]').click()
  time.sleep(3)
  download_file = webdriver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/div[2]/div[4]/div/button')
  download_file.click()
  time.sleep(2)
  webdriver2.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]').click()
  time.sleep(3)
  download_file = webdriver2.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/div[2]/div[4]/div/button')
  download_file.click()

#Descarga para El Diario de México
def download_diariodemexico(path):
  webdriver.get("https://edicionimpresa.diariodemexico.com/index.php")
  time.sleep(6)
  WebDriverWait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/alink/div/div/iframe")))
  WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="toolbar_documentViewer"]/img[2]'))).click()
  time.sleep(5)
  path = path+"/view.php"
  shutil.move("view.php", path)

#Descarga para El Financiero
def download_financiero():
  webdriver.get("https://www.elfinanciero.com.mx/graficos/edicion-impresa/flip/el-financiero.html")
  time.sleep(2)
  download_file = (webdriver.find_element_by_xpath('//*[@id="df_book_full"]/div[4]/div[9]/div/a')).get_attribute("href")
  wget.download(download_file, 'Elfinanciero.pdf')

#Descarga para Publimetro
def download_Publimetro():
  webdriver.get("https://www.readmetro.com/es/mexico/publimetro/")
  time.sleep(4)
  download_file = (webdriver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[2]/div[1]/div[2]/ul/li[5]/a')).get_attribute("href")
  wget.download(download_file, 'Publimetro.pdf')

#Descarga para Excelsior
def download_Excelsior():
  webdriver.get("https://www.excelsior.com.mx/impreso")
  time.sleep(2)
  download_file = (webdriver.find_element_by_xpath('//*[@id="impreso"]/div[2]/div[1]/div/div[1]/a[1]')).get_attribute("href")
  wget.download(download_file, 'Excelsior.pdf')

#Descarga para Diputados
def download_Diputados():
  webdriver.get("http://www5.diputados.gob.mx/index.php/esl/Comunicacion/Sintesis")
  time.sleep(4)
  download_file = (webdriver.find_element_by_xpath('//*[@id="page"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/div/div[2]/div/div/div/div/div[2]/table[2]/tbody/tr[1]/td/div/a')).get_attribute("href")
  wget.download(download_file, 'Primeras_Planas.pdf')

#Descarga para La Razon
def download_la_razon():
  webdriver.get("https://www.razon.com.mx/version-impresa")
  time.sleep(4)
  webdriver.find_element_by_xpath('//*[@id="m26-25-27"]/div/ul/li[1]/article/div[2]/h3/a').click()
  time.sleep(4)
  download_file = (webdriver.find_element_by_xpath('//*[@id="m46-45-47"]/a')).get_attribute("href")
  wget.download(download_file, 'La_Razon.pdf')

#Descarga para Indigo
def download_Indigo():
  webdriver.get("https://www.reporteindigo.com/edicion-impresa/")
  time.sleep(6)
  WebDriverWait(webdriver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/main/div/div/section/div/div[2]/iframe")))
  WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="toolbar_documentViewer"]/img[2]'))).click()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    webdriver2 = webdriver.Chrome(executable_path=r"Drivers/chromedriver.exe",options=options)
    webdriver = webdriver.Chrome(executable_path=r"Drivers/chromedriver.exe",options=options)
    webdriver.set_page_load_timeout(10000)
    

    today = date.today()
    if os.path.isdir(str(today)):
        shutil.rmtree(str(today))
    os.mkdir(str(today))
    time.sleep(5)
    os.chdir(str(today))

    download_Publimetro()
    time.sleep(5)

    download_financiero()
    time.sleep(5)

    download_heraldo()
    time.sleep(5)
    
    download_Excelsior()
    time.sleep(5)

    download_Diputados()
    time.sleep(5)

    download_la_razon()
    time.sleep(5)

    download_Indigo()
    time.sleep(5)
