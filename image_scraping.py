# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:50:36 2020

@author: INTEL
"""

from selenium import webdriver
import os
import urllib
import time

path = r'C:\Program Files (x86)\chromedriver.exe'

#https://www.google.com/search?sxsrf=ALeKk01fh3Hh_9uWtOxljuBRbwU-0QnMng:1597473898017&source=univ&tbm=isch&q=google+images%2B+toddler+images&sa=X&ved=2ahUKEwjyuOqBzpzrAhV3zTgGHapNANwQsAR6BAgKEAE&biw=1366&bih=657
url_prefix = "https://www.google.com.sg/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591"

save_folder = 'Valid Images'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    download_images()
    
def download_images():
    topic = input("What do you want to search for? ")
    n_images = int(input('How many images do you want? '))
    
    search_url = url_prefix+topic+url_postfix
    #print(search_url)
    
    path = r'C:\Program Files (x86)\chromedriver.exe'
    
    driver = webdriver.Chrome(path)
    driver.get(search_url)
    
    value = 0
    for i in range(3):
        driver.execute_script("scrollBy("+ str(value) +",+1000);")
        value += 1000
        time.sleep(1)
    
    elem1 = driver.find_element_by_id('islmp')
    sub = elem1.find_elements_by_tag_name('img')
    
    
    for j,i in enumerate(sub):
        if j < n_images:
            src = i.get_attribute('src')                         
            try:
                if src != None:
                    src  = str(src)
                    print(src)
                    save_folder = "Valid Images\\"+topic
                    if not os.path.exists(save_folder):
                        os.mkdir(save_folder)
                    urllib.request.urlretrieve(src, os.path.join(save_folder, topic+str(j)+'.jpg'))
                else:
                    raise TypeError
            except Exception as e:              #catches type error along with other errors
                print('fail')
    
    driver.close()
    
if __name__ == "__main__":
    main()
    