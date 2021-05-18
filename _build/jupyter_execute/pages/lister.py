#!/usr/bin/env python
# coding: utf-8

# # 5. Lister

# En liste inneholder flere tall eller flere tekststrenger.

# ## 5.1 Lage og legge til i en liste

# Vi oppretter en liste enten tom, eller med noen verdier i. Her lager vi en liste med de 7 første primtallene.

# In[1]:


primtall = [2, 3, 5, 7, 11, 13, 17]
print( primtall )


# In[2]:


favorittmat = ["lapskaus", "taco", "fårikål"]
print( favorittmat )


# ```{admonition} Prøv selv
# :class: tip
# Lag en liste med dine favorittdyr. Skriv den til skjerm.
# ```

# Vi kan også legge til elementer i en liste som allerede eksisterer ved å bruke `append()`:

# In[3]:


favorittmat = ["lapskaus", "taco", "fårikål"]
favorittmat.append("fiskekaker")
favorittmat.append("iskrem")
print( favorittmat )


# ```{admonition} Prøv selv
# :class: tip
# Bruk `append()` for å legge til to ekstra dyr i lista di.
# ```

# ## 5.2 Plukke ut fra en liste

# Lister er veldig nyttige fordi vi kan gå inn og inspisere enkelte elementer, lese av lengden, søke etter innhold og mye mer.
# 
# Vi bruker `len()` til å lese av lengden:

# In[4]:


liste = []
liste.append(1)
liste.append(4)
liste.append(9)
liste.append(16)
lengden = len(liste)
print( lengden )


# ```{admonition} Prøv selv
# :class: tip
# Bruk `len()` til å lese av lengden på lista di over favorittdyr.
# ```

# Vi inspiserer ett spesifikt element ved hjelp av `[]`-paranteser.

# In[5]:


liste = ["lapskaus", "Taco", "fårikål", "fiskekaker", "iskrem"]
print( liste[0] )
print( liste[3] )


# `liste[0]` leser av det 0-te elementet i lista. Python teller alltid fra 0, ikke fra 1. Siden det *første* (altså det 0-te) elementet er `lapskaus`, blir det skrevet til skjerm av `print()`.
# 
# Legg merke til at `liste[3]` gir `fiskekaker`, siden det er det tredje elementet når man teller fra 0. Forvirra? Så bra.

# ```{admonition} Prøv selv
# :class: tip
# Legg inn denne lista over de 25 første primtallene. Bruk `[]` til å finne ut:
# * Hva er primtall nummer 12?
# * Hva er differansen mellom primtall nummer 19 og primtall nummer 7?
# 
# `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]`
# ```
# 
# ```{admonition} Svar
# :class: dropdown
# * Primtall nummer 12 er **37**
# * Primtall 19 - primtall 7 er **48**
# 
# ```
