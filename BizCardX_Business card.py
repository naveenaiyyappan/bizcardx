#!/usr/bin/env python
# coding: utf-8

# In[1]:


# libraries 
import pandas as pd
import matplotlib.pyplot as plt 
import re


# In[2]:


# install opencv
get_ipython().system('pip install opencv-python')


# In[6]:


# Install EasyOCR 
get_ipython().system('pip install git+https://github.com/JaidedAI/EasyOCR.git')


# In[2]:


import cv2
import easyocr


# In[3]:


import os
from PIL import Image
import numpy as np


# In[4]:


img_1= Image.open("C:/Users/Ivin/Downloads/1.png")         #image1
img_1.show()


# In[5]:


print(img_1)


# In[6]:


img_1


# In[7]:


plt.imshow(img_1)


# In[8]:


img_2 = Image.open("C:/Users/Ivin/Downloads/2.png")           #image2
img_2.show()


# In[9]:


print(img_2)


# In[10]:


img_2


# In[11]:


plt.imshow(img_2)


# In[12]:


img_3 = Image.open("C:/Users/Ivin/Downloads/3.png")           #image3
img_3.show()


# In[13]:


print(img_3)


# In[14]:


img_3


# In[15]:


plt.imshow(img_3)
plt.show()


# In[16]:


img_4 = Image.open("C:/Users/Ivin/Downloads/4.png")     # image4
img_4.show()


# In[17]:


print(img_4)


# In[18]:


img_4


# In[19]:


plt.imshow(img_4)
plt.show()


# In[20]:


img_5 = Image.open("C:/Users/Ivin/Downloads/5.png")        #image5
img_5.show()


# In[21]:


print(img_5)


# In[22]:


img_5


# In[23]:


plt.imshow(img_5)
plt.show()


# In[24]:


reader = easyocr.Reader(["en"])


# In[25]:


output_1 = reader.readtext("C:/Users/Ivin/Downloads/1.png")       # immage output 1 bytes


# In[26]:


print(output_1)


# In[27]:


output_1


# In[28]:


output_2 = reader.readtext("C:/Users/Ivin/Downloads/2.png")         #image2 text bytes


# In[29]:


print(output_2)


# In[30]:


output_2


# In[31]:


output_3 = reader.readtext("C:/Users/Ivin/Downloads/3.png")         # image 3 text bytes


# In[32]:


print(output_3)


# In[33]:


output_3


# In[34]:


output_4 = reader.readtext("C:/Users/Ivin/Downloads/4.png")        #image 4  text bytes


# In[35]:


print(output_4)


# In[36]:


output_4


# In[37]:


output_5 = reader.readtext("C:/Users/Ivin/Downloads/5.png")    #image 5  text bytes


# In[38]:


print(output_5)


# In[39]:


output_5


# In[40]:


# this both the install helps to get the text from an image 


# In[45]:


get_ipython().system('pip install pillow')


# In[46]:


get_ipython().system('pip install pytesseract')


# In[51]:


get_ipython().system('pip install tesseract')


# In[40]:


# text extract from the image
text = ""
for result in output_1:
    text += result[1] + ','
    
print(text)                            # image 1 text


# In[41]:


text = ""
for result in output_2:
    text += result[1] + ','

print(text)                            # image 2 text


# In[42]:


text = ""
for result in output_3:
    text += result[1] + ","
    
print(text)                           # image 3  text


# In[43]:


text = ""
for result in output_4:
    text += result[1] + ","

print(text)                          # image 4 text


# In[57]:


text = ""
for result in output_5:
    text += result[1] + ","
    
print(text)                           # image 5 text


# In[45]:


#sql
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine


# In[46]:


connection = sqlite3.connect("BusinessCard.db")


# In[48]:


#engine = create_engine("sqlite:///Business_card.db",echo = True)


# In[47]:


cursor = connection.cursor()


# In[48]:


cursor.execute('''CREATE TABLE IF NOT EXISTS card_data
                   (id INTEGER PRIMARY KEY,
                    company_name TEXT,
                    card_holder TEXT,
                    designation TEXT,
                    mobile_number TEXT,
                    email TEXT,
                    website TEXT,
                    area TEXT,
                    city TEXT,
                    state TEXT,
                    pin_code TEXT,
                    image BLOB
                    )''')


# In[49]:


data = {
    "company_name":[],
    "card_holder":[],
    "designation":[],
    "mobile_number":[],
    "email":[],
    "website":[],
    "area":[],
    "city":[],
    "state":[],
    "pincode":[]
}


# In[51]:


def get_data(text):
    for ind, i in enumerate(text):
        if "www " in i.lower() or "www." in i.lower():  # Website with 'www'
            data["website"].append(i)
        elif "WWW" in i:  
            website = text[ind + 1] + "." + text[ind + 2]
            data["website"].append(website)
        elif "@" in i:
            data["email"].append(i)
        #to get mobile number
        elif "-" in i:
            data["mobile_number"].append(i)
            if len(data["mobile_number"]) == 2:
                data["mobile_number"] = " & ".join(data["mobile_number"])
        #to get a company details
        elif ind == len(text)-1:
            data["company_name"].append(i)
        #to get a card holder name
        elif ind == 0:
            data["card_holder"].append(i)
        #to get a desination 
        elif ind == 1:
            data ["designation"].append(i)
        #to get a area 
        if re.findall('^[0-9].+, [a-zA-Z]',i):
            data["area"].append(i.split(',')[0])
        elif re.findall('[0-9] [a-zA-z]+',i):
            data["area"].append(i)
        #to get a city name
        match1 = re.findall('.+St , ([a-zA-Z]+).+',i)
        match2 = re.findall('.+St,,([a-zA-Z]+).+',i)
        match3 = re.findall('^[E].*',i)
        if match1:
            data["city"].append(match1[0])
        elif match2:
            data["city"].append(match2[0])
        elif match3:
            data["city"].append(match3[0])
        #to get a state name
        state_match = re.findall('[a-zA-Z]{9} +[0-9]', i)
        if state_match:
            data ["state"].append(i[:9])
        elif re.findall('^[0-9].+, ([a-zA-Z]+);', i):
            data["state"].append(i.split()[-1])
        if len(data["state"]) == 2:
            data ["state"].pop(0)
        #to get a pincode
        if len(i) >= 6 and i.isdigit():
            data["pin_code"].append(i)
        elif re.findall('[a-zA-Z]{9} +[0-9]', i):
            data["pin_code"].append(i[10:])
get_data(text)


# In[53]:


print(get_data)


# In[54]:


get_data


# In[55]:


def create_df(data):
    df = pd.DataFrame(data)
    return df


# In[ ]:




