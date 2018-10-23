from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import xlwt 
import mysql.connector
import random

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path='/home/mukesh/Desktop/backup/Programminghub/whatsapp_python_scripts/chromedriver_linux64/chromedriver', chrome_options=option)

symbol=["Ambani","Adani","Bajaj","Mukesh","Goenka","135431","4525$5","%&@*&$&","Crush","---32-1-"]
date=["11/02/1992","05/02/1998","03/12/1999","26/05/1998","20/01/2000","MyNameisNone","Ihope","IsThatYou?","23/01/1999","alal"]
#date=["11/02/1992","05/02/1998","03/12/1999","26/05/1998","20/01/2000","MyNameisNone","12/01/2012","IsThatYou?","23/01/1999","12/12/2010"]
#high=["12626","66375","95230","65320","9632","8646","45231","694613","68453","12/12/2010"]
browser.get("localhost:5000")
browser.get("localhost:5000/new_user")
l=[]
net=10
for i in xrange(0,10):
	browser.get("localhost:5000/new_user")
	field = browser.find_element_by_name('inputsymbol')
	#var=''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8))
	field.send_keys(symbol[i])
	if(symbol[i].isalpha()==0):
		l.append(i)
	field = browser.find_element_by_name('inputdate')
	field.send_keys(date[i])
	field = browser.find_element_by_name('inputhigh')
	var=''.join(random.choice('0123456789') for i in range(8))
	field.send_keys(var)
	field = browser.find_element_by_name('inputlow')
	var=''.join(random.choice('0123456789') for i in range(8))
	field.send_keys(var)
	field = browser.find_element_by_name('inputvolume')
	var=''.join(random.choice('0123456789') for i in range(8))
	field.send_keys(var)
	field = browser.find_element_by_name('inputopen')
	var=''.join(random.choice('0123456789') for i in range(8))
	field.send_keys(var)
	field = browser.find_element_by_name('inputclose')
	var=''.join(random.choice('0123456789') for i in range(8))
	field.send_keys(var)
	browser.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()
#print(l)
for i in xrange(0,10):
	if(i in l):
		print "Test Case Failed as Symbol is just alphabet and this is not: "+str(symbol[i])+"a valid symbol"
	if(i in l):
		print "Test Case Failed as Date is invalid and this is not: "+str(date[i])+"a valid date"
print "These many cases Passed: "+ str(net-len(l))
print "These many cases Failed: "+str(len(l)) 





