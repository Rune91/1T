#!/usr/bin/env python
# coding: utf-8

# # 3. Input

# Programmer er mest nyttige dersom brukeren av programmet kan gi *input* til det. (Hvor gøy hadde det egentlig vært å spille Fifa dersom du ikke kunne styre spillerne eller bla i menyene?)
# 
# Nå skal vi lære å gi input i form av tekst og tall.

# ## 3.1 Hente inn tekst

# Vi ber brukeren skrive inn en tekst i konsollvinduet ved å bruke `input()` sammen med en relevant tekst. Svaret blir lagret i en variabel.

# In[1]:


tekst = input("Skriv inn en tekst: ")
print(f"Du skrev inn dette: {tekst}!")


# ```{admonition} Prøv selv
# :class: tip
# Kopier og kjør programmet over. Når det kjører, vil det stoppe og vente på at du skriver et svar og trykker `Enter` i konsollvinduet.
# ```

# ```{admonition} Prøv selv
# :class: tip
# Lag et program som bruker to `input()`-kommandoer til å be brukeren om både fornavn og etternavn. Skriv så ut en hilsen med fullt navn.
# ```

# ## 3.2 Hente inn tall

# Ofte vil vil hente inn tall fra brukeren. `input()` leser inn svaret som en tekststreng selv om det bare inneholder tall. For å kunne gjøre regneoperasjoner må vi først gjøre det om til et heltall (`int`) eller et desimaltall (`float`).
# 
# For å konvertere til heltall bruker vi kommandoen `int()`.
# 
# Programmet under leser inn to vinkler i en trekant som heltall og regner så ut den tredje vinkelen.

# In[2]:


vinkel_1 = int( input("Vinkel: ") )
vinkel_2 = int( input("Vinkel: ") )
vinkel_3 = 180 - vinkel_1 - vinkel_2
print(f"Den tredje vinkelen er {vinkel_3} grader")


# ```{admonition} Prøv selv
# :class: tip
# Lag et program som ber brukeren om et tall. Det skal så regne ut halvparten av tallet.
# ```

# In[ ]:




