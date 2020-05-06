#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
text = handle.read()

mail=dict()

for line in handle:
    if line.startswith("From"):
        words=line.split()
        email=words[1]
        mail[email]=mail.get(email,0)+1


bigcount = None
bigemail = None
for mail,count in mail.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count
        
print(bigemail,bigcount)        


