#!/usr/bin/env python
# coding: utf-8

# (oppgaver-b)=
# # Oppgavesett B
# Disse oppgavene bruker teorikapitler 5-6.

# ---
# ```{admonition} A.X: Tall i liste
# :class: tip
# Opprett en liste med dine favorittall. Programmet ditt skal så:  
# * Skrive ut det dobbelte av hvert tall til skjerm.
# * Regne ut summen av alle tallene
# ```

# ```{admonition} Hint!
# :class: dropdown
# Her passer det med en `for`-løkke.
# ```

# ---
# ```{admonition} A.X: Passord
# :class: tip
# Lag et program som ber brukeren om å skrive inn et passord. Programmet skal spørre om igjen helt til passordet er riktig. Slik kan det se ut i konsollen når du kjører det ferdige programmet:  
# **Skriv inn passord: 12345  
# Feil passord!  
# Skriv inn passord: rosebud  
# Feil passord!  
# Skriv inn passord: hunter2  
# Riktig passord.**
# ```

# ```{admonition} Hint!
# :class: dropdown
# Her er det nyttig å bruke en `while`-løkke sammen med `input()`.
# ```

# ---
# ```{admonition} A.X: Donald Trump
# :class: tip
# Programkoden under leser inn alle ordene Donald Trump har brukt i sine taler i lista `ord`. Kopier koden inn i Spyder og fortsett på programmet. Ikke bry deg om at du ikke forstår alt som foregår øverst.
# 
# * Hvor stort er ordforrådet til Donald Trump?
# * Skriv ut ord nummer 100 til 110.  
# * Lag et program som ber brukeren om et ord. Programmet skal så fortelle brukeren om ordet inngår i Trumps ordforråd. Programmet skal spørre om igjen helt til brukeren skriver ordet **quit**.
# ```

# In[ ]:





# In[1]:


import urllib3
import re

http = urllib3.PoolManager()
response = http.request('GET', "https://raw.githubusercontent.com/ryanmcdermott/trump-speeches/master/speeches.txt")
data = response.data.decode('utf-8')

ord = re.split(' |,|\n|\r|\.|\?|"', data)
ord = list(filter(None, ord))
ord = [i.lower() for i in ord]
ord = list(dict.fromkeys(ord))
ord = sorted(ord)
ord = ord[324:]

###### Fortsett nedenfor #########


# ```{admonition} Hint!
# :class: dropdown
# Hint for siste punkt:  
# * Her passer det å bruke en `while`-løkke
# * Du kan sjekke om noe finnes in en liste ved å bruke ordet `in`:  
# **liste = [10, 12, 14, 16, 18]  
# if 14 in liste:  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Ja!")**
# ```

# In[ ]:




