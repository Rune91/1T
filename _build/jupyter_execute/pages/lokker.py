#!/usr/bin/env python
# coding: utf-8

# # 6. Løkker

# Endelig er du kommet til det viktigste verktøyet i programmering: **løkker**!
# 
# Løkker lar deg skrive kode som kjøres mer enn én gang.

# ## 6.1 for-løkker

# Vi bruker for-løkker når vi vet hvor mange ganger vi skal kjøre koden. Ta en titt på dette programmet som skriver ut de 10 første tallene:

# In[1]:


for tall in range(10):
    print(tall)


# Så hva skjer?
# 
# * `range(10)` lager en følge med de 10 første tallene. Husk at vi teller fra 0!
# * Koden blir så kjørt én gang for hvert tall i følgen.
# * Variabelen `tall` vil endre seg for hver runde koden kjøres.

# ---
# ```{admonition} Prøv selv
# :class: tip
# Lag et program som skriver ut alle tallene opp til 500.
# ```

# Vi kan også bruke `range()` til å telle fra et annet tall enn null, eller å bruke en annen steglengde:

# In[2]:


for x in range(5, 13):
    print(x)


# Legg merke til at tallet **13** ikke blir med i eksempelet over.

# In[3]:


for oddetall in range(1, 21, 2):
    print(oddetall)


# I `range(1, 21, 2)`, vil det tredje *argumentet*, tallet `2`, bestemme steglengden mellom tallene. For-løkka går da direkte fra 1 til 3 og så videre.

# ---
# ```{admonition} Prøv selv
# :class: tip
# Skriv ut alle partall fra 12 til 48.
# ```

# ---
# Ved å bruke enda en variabel kan vi for eksempel summere tallene i en følge:

# In[4]:


# Dette programmet regner ut summen av alle tallene fra 1 til og med 100
totalt = 0
for tall in range(1, 101):
    totalt = totalt + tall

print(f"Summen av tallene fra 1 til og med 100 er {totalt}.")


# ---
# ```{admonition} Prøv selv
# :class: tip
# Hva er summen av alle oddetall opp til 1 million?
# ```

# ```{admonition} Svar
# :class: dropdown
# $250000000000$ altså $2.5*10^{11}$
# ```

# ## 6.2 while-løkker

# Vi bruker ofte while-løkker når vi på forhånd ikke vet hvor mange ganger koden skal kjøre. Den bruker ordet `while` sammen med et utsagn som enten blir `True` eller `False`. Koden i while-løkka kjører så lenge uttrykket er `True`.

# In[5]:


tall = 0
while tall < 10:
    print(f"Tallet er {tall}")
    tall = tall + 1


# `tall < 10` vil være `True` helt til tallet økes til 10, så da stopper løkka. 
# 
# Det går også an å bruke `while` til å lage evige løkker.
# 
# **while True:  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Hei på deg")**
# 
# Dersom du kjører dette, vil konsollvinduet henge seg opp og aldri slutte å skrive ut *Hei på deg*. Avslutt programmet ved å trykke på stoppknappen i Spyder.

# ```{admonition} Prøv selv
# :class: tip
# Lag en while-løkke som gir følgende output:  
# **1  
# 2  
# 4  
# 8  
# 16  
# 32  
# 64  
# 128**
# ```

# ## 6.3 Løkker sammen med lister

# Løkker og lister passer godt sammen. Vi kan bruke en `for`-løkke til å skrive skrive ut alle elementene i en liste hver for seg:

# In[6]:


favorittmat = ["lapskaus", "taco", "fårikål", "fiskekaker", "iskrem"]
for mat in favorittmat:
    print(f"Jeg liker {mat}")


# Dette er en litt annen måte å bruke en `for`-løkke på, som ikke bruker `range()`. Her blir hvert element i lista satt inn i `mat` etter hverandre.

# Vi kan også bruke løkker til å fylle opp en liste. `tall = []` lager en tom liste, som fylles opp i `for`-løkka:

# In[7]:


tall = []
for x in range(0, 30, 3):
    tall.append(x)
print(tall)


# In[ ]:





# Du er nå klar til å gjøre [oppgavesett B](oppgaver-b)
