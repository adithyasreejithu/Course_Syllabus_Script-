# List of every import used 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# # Chrome preset options 
# options = webdriver.ChromeOptions()
# # options.add_argument('--headless') 
# options.add_experimental_option('detach', False)

# #directing script to D2l Login 
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
# driver.get("https://uottawa.brightspace.com/d2l/home") #the link is too the uOttawa bright space home page. 
# #this area is for testing purposes
# driver.maximize_window()

"""
#start of actual script 

# first step - getting passed login ( assumption that user is logged in )
# look to find a way to bypass the 2FA 
# this will be added later 

# Second Step - Finding the Specfic Classes

# this here is locating the grid in which the classes are stored
container = WebDriverWait(driver, 5).until(
    EC.presence_of_all_element_located(By.CLASS_NAME,"d2l-card-container")
)

classes = container.find_elemnts(By)

# this is based off the concept of this 
try: 
    # this is the explict wait - for 10 seconds and the wait is to take place until the element is located 
    # it is finding the specific section where all the articles are stored 
    bodyText = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mwsquerygc section"))
    )
    
    #this here will finding the article tags inside the specfied section 
    
    aritcles = bodyText.find_elements(By.TAG_NAME, "article")
    print("******these are the top results on the first page******** \n")

    #this section is finding every article that e
    for article in aritcles:
        header = article.find_element(By.CLASS_NAME,"h4")
        print(header.text + "\n")
        

finally: 
    print("commands have ended")

"""

###################################################################################################
                            # this is the OS portion of the code

"""CWD-1"""
#finds dir that the script is running in  
def findCWD ():
    path = os.getcwd()
    print (path)
    return path

# will create a new Dir in given path
def createDir():
    dir = "Downloads" # this is creating a folder where the downloads will be stored. 
    parentDir = findCWD()
    dirPostion = os.path.join(parentDir, dir) # creating the full path of the new directory 
    mode = 0o666 # this mode allows for the editing of the contents inside the directory 
    os.makedirs(dirPostion, mode, exist_ok= True) # creating new folder with mode and stating to now throw exeception if it does exist 

    print("Directory '% s' has been created" % dir)

    deleteDir(dirPostion)

# deletes given dir 
def deleteDir(path):
    os.rmdir(path)

#call functions for testinf 
createDir() 











"""this is where I will do the all the planning for the code and all the ideas that come to my head 
each plan should be labled"""
# (CSV) create a CSV file with the name of class (CSV-1), storage location  in CWD (CWD - 1), new location if needed (CWD-2), save files at the end? 

#(CWD-1) this using the dir that the script is operating in this where the new folder will be created

#(Dir-1) this creates new dir 
#(Dir-2) will need to 


###############################################
# what will be needed for this project 
# selenium 
# pandas 