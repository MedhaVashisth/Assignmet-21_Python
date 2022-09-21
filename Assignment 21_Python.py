#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[3]:


from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today', 'wt') as output:
    print(now_str, file=output)


# In[4]:


with open('today', 'rt') as input:
    today_string = input.read()
    today_string


# In[5]:


fmt = '%Y-%m-%d\n'
datetime.strptime(today_string, fmt)
datetime.datetime(2014, 2, 4, 0, 0)


# In[6]:


import os
os.listdir('.')
['bears', 'lions', 'tigers']


# In[7]:


import os 
os.listdir('..')
['ohmy', 'paws', 'whiskers']


# In[12]:


def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())
if __name__ == '__main__':
    import random 
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()

 python multi_times.py


# In[13]:


my_day = date(1982, 8, 14)
my_day


# In[14]:


my_day.weekday()


# In[15]:


my_day.isoweekday()


# In[16]:


from datetime import timedelta
party_day = my_day + timedelta(days=10000)
party_day


# In[ ]:




