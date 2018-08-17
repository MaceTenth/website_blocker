
# coding: utf-8

# In[2]:


import time
from datetime import datetime as dt


# In[7]:

# In[3]:


hosts_path = 'hosts'
redirect = '127.0.0.1'


# In[4]:


website_list = ['www.walla.co.il','walla.com','walla.co.il','www.walla.com']


# In[18]:


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("working Hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
    time.sleep(1)

    
    

