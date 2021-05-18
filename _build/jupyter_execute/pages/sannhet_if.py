#!/usr/bin/env python
# coding: utf-8

# # 4. Sannhetsverdier og if-setninger

# ## 4.1 Sant og usant

# Vi lager utsagn som Python evaluerer til enten `True` eller `False`. Til det bruker vi disse operatorene:

# Operator | Betydning
# :---: | :---:
# `==` | Lik
# `!=` | Ulik
# `<` | Mindre enn
# `>` | Større enn
# `<=` | Mindre eller lik
# `>=` | Større eller lik

# In[1]:


print(4==4)


# In[2]:


print(4!=4)


# In[3]:


uttrykk = 6>1
print(uttrykk)


# In[4]:


uttrykk = 3>=3
print(uttrykk)


# ```{admonition} Prøv selv
# :class: tip
# Bruk tallene 7 og 8 til å lage to uttrykk: et som blir `True` og et som blir `False`.
# ```

# ---
# I tillegg til operatorene over bruker vi kodeordene `and`, `or` og `not` til å styre evaluering av uttrykk.
# * `and` gir sant dersom begge utsagnene er sanne
# * `or` gir sant derson ett (eller begge) av de to uttrykkene er sanne
# * `not` gir det motsatte av utsagnet. Gjør `True` om til `False` og motsatt

# In[5]:


uttrykk = 3>2 and 10>8
print(uttrykk)


# In[6]:


uttrykk = 3>2 and 10>20
print(uttrykk)
print(not uttrykk)


# In[7]:


uttrykk_1 = False
uttrykk_2 = 5!=9
print(uttrykk_1 and uttrykk_2)
print(uttrykk_1 or uttrykk_2)


# ```{admonition} Prøv selv
# :class: tip
# Lag et uttrykk som bruker både `and` og `not` som evalueres til `True`.
# ```

# ## 4.2 If-setninger

# If-setninger (også kalt *kontrollstruktur*) er et viktig verktøy for å styre et program. Kodeordene `if` og `else` bruker slik:

# In[8]:


tall_1 = 10
tall_2 = 12
if tall_1 > tall_2:
    print("Det første tallet er størst")
else:
    print("Det andre tallet er størst")


# Legg merke til at linjene direkte etter `if` og `else` er rykket inn. Python bruker enten TAB eller 4 mellomrom.
# 
# `elif` kan også brukes dersom du vil ha flere muligheter:

# In[9]:


by = "Madrid"
if by == "Dortmund":
    print("Willkommen in Dortmund!")
elif by == "New York":
    print("Welcome to New York!")
elif by == "Madrid":
    print("Bienvenida a Madrid!")
else:
    print("Velkommen til ...?")


# ```{admonition} Prøv selv
# :class: tip
# Bruk samme struktur som programmet over, men nå skal det handle om frukt. La programmet skrive ut fargen på frukta.
# ```

# Du er nå klar til å gjøre [oppgavesett A](oppgaver-a).
