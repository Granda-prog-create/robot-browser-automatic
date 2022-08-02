from selenium import webdriver
import pyautogui

navegador = webdriver.Chrome('C:/Users/Dell/Desktop/chromedriver.exe')

#Abrir o navegador e fazer a pesquisa no Google
navegador.get('https://www.google.com/')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Amazon')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

# Entra no site pesquisado
navegador.find_element_by_xpath('//*[@id="tads"]/div/div/div/div/div[1]/a/div[1]/span').click()


