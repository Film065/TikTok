#coding: utf-8

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama

def clear():
    
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    

def logo():
    try:
        text = """                                   
 _____  _   _ _____   ______ ____
|  __ \| \ | |  __ \ / ____/_ /_ |
| |__) |  \| | |__) | (___  | || |
|  ___/| . ` |  ___/ \___ \ | || |
| |    | |\  | |     ____) || || |
|_|    |_| \_|_|    |_____/ |_||_|                   
        """
        bad_colors = ['LIGHTGREEN_EX', 'GREEN']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "Discord : https://discord.gg/yPBddhu\n")

    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

maxi = 0
start = '/@'
end = '/video/'
hearts = ' '

boosted_link = input('{}\n> {}Video Link: {}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
print('  ')
username = boosted_link[boosted_link.find(start)+len(start):boosted_link.rfind(end)]
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,900')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
browser.minimize_window()
wait = WebDriverWait(browser, 3)

from selenium import webdriver

init()
os.system('title ' + ' TikTok Heart Bot By PNPS11 @{}'.format(username))

def countdown():
	while True:
		time.sleep(5)
		try:
			browser.find_element_by_xpath('//*[@id="show_theart"]/div/div/div/form/div/div/button').click()
			wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button')))
			break
		except:
			continue
			pass
def run():
	global hearts
	global username
	try:
		browser.find_element_by_xpath('//*[@id="show_theart"]/div/div/div/form/div/div/button').click()
		try:
			hearts = browser.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/div').text 
			time.sleep(1)
		except:
			pass
		time.sleep(5)
		while True:
			try:
				wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button')))
				break
			except:
				continue
				pass
		browser.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click() 
		print('  ')
		print('{}> {} Hearts Sent Success{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
		os.system('title ' + ' TikTok TikTok Heart Bot By PNPS11 @{} Hearts Sent: {}'.format(username, hearts))
		time.sleep(5)
		countdown()
		run()
	except:
		print('  ')
		run()

def paste_link():
	global boosted_link
	try:
		browser.find_element_by_xpath('//*[@id="show_theart"]/div/div/div/form/div/input').send_keys(boosted_link) #Link where is paste
		time.sleep(1)
		wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="show_theart"]/div/div/div/form/div/div/button'))) #Search link
		print('  ')
		print("{}> {}Pasted link{}".format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
		run()
	except:
		print("{}> {}Error{}".format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
		input()

def maximize():
	global maxi
	maxi += 1
	if maxi == 1:
		print('  ')
		print('{}> {}Pls do the Captcha{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
		browser.maximize_window()
	elif maxi >= 1:
		pass
	else:
		pass

def start():
	try:
		browser.get("https://vipto.de/")
		time.sleep(2)
		while True:
			try:
				wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/h2/span')))
				print('  ')
				print('{}\n {}{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
				continue
			except:
				pass
				break
		while True:
			try:
				maximize()
				wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/form/div/input[1]')))
				continue
			except:
				pass
				browser.minimize_window()
				break
	except:
		try:
			wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/ul/li/a')))
			print('  ')
			print("{}> {}Can't load page{}".format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
			input()
		except:
			pass
	print('  ')
	print('{}> {}Captcha OK{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
	time.sleep(1)
	try:
		browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/button').click()
		time.sleep(1)
	except:
		print('  ')
		print("{}> {}Error, Cannot find Element{}".format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
		pass
	clear()
	logo()
	print('{}> {}Starting{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
	paste_link()

start()