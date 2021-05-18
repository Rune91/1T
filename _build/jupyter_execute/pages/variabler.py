#!/usr/bin/env python
# coding: utf-8

# # 2. Variabler

# ## 2.1 Kommentarer

# Det er viktig å gjøre programkode lett å lese både for deg selv og andre. Et nyttig verktøy til dette er å bruke kommentarer. En kommentar *gjør* ingenting i programmet. Alt etter `#` på en linje er en kommentar.

# In[1]:


# Dette er en kommentar
print(2+2) # Denne linjen regner ut 2+2


# ## 2.2 Å lage variabler

# Vi bruker variabler til å lagre tall, tekst eller annet i programmet vårt. Variabler må ha navn, som kan være på bare én bokstav eller et helt ord.

# In[2]:


a = 3
b = 6
c = a + b
print(c)


# In[3]:


fart = 60 # km/t
tid = 2.5 # timer
strekning = fart * tid # km


# I programmet over har variabelen strekning fått verdien 150. Programmet gir derimot ingen output siden det ikke bruker `print()`.

# ```{admonition} Prøv selv
# :class: tip
# Bruk samme struktur som eksempelet over, men nå har du kjøpt poteter på butikken! Lag en variabel for vekt og en for prisen du betalte. Regn ut kilospris og skriv svaret ut til skjerm med `print()`.
# ```

# For å lagre tekst i variabler må teksten være i anførselstegn. Variabler med tekst kalles for en *tekststreng* eller bare *streng*.

# In[4]:


navn = "Rune"
beskrivelse = " er kul"
print( navn + beskrivelse )


# Vi kan endre innholdet i en variabel like enkelt ved å gi den en ny verdi.

# In[5]:


a = 10
a = 21
a = 5
print(a)


# Vi kan også bruke variabelens gamle verdi for å oppdatere den.

# In[6]:


tall = 38
tall = tall + 1
tall = tall + 10
print(tall)


# ```{admonition} Prøv selv
# :class: tip
# Lag et program som gjør dette:
# * Oppretter en variabel x med verdi 11
# * Oppretter en ny variabel y som er det dobbelte av x
# * Øker y med 1
# * Skriver ut svaret til skjerm
# ```

# ```{admonition} Prøv selv
# :class: tip
# Hva blir output av programmet under? Når du har bestemt deg, kopier koden over i Spyder og sjekk om du hadde rett.
# ```

# In[7]:


alice = 18
bob = alice / 2
cecilie = bob + alice

cecilie = cecilie + 1

print(cecilie)


# ## 2.3 Å skrive tall og tekst sammen

# I `print()` kan vi skrive verdien av variabler sammen med en tekst. Til dette bruker vi et såkalt f-literal. Vi setter `f` foran tekst-strengen, og bruker variabelnavnet inne i `{}` i teksten.

# In[8]:


navn = "Rune"
mat = "lapskaus"
print(f"Hei, jeg heter {navn} og jeg liker {mat}.")


# ```{admonition} Prøv selv
# :class: tip
# Bruk variabler og `print()` til å skrive ut en hilsen som forteller om deg og dine hobbyer.
# ```

# Vi bruker også f-literaler til å skrive tall sammen med tekst. Når vi gjør det, har vi også muligheten til å styre antall desimaler som skrives ut. `{c:.2f}` betyr at variabelen c skrives ut med 2 desimaler.

# In[9]:


a = 22
b = 7
c = a / b
print(f"{a} delt på {b} er {c}")
print(f"{a} delt på {b} er {c:.2f}")


# Vi kan også velge å skrive ut tall på standardform. Til dette bruker vi `.2e` (eller `.3e` eller `.7e`).

# In[10]:


c = 300000000 # m/s
print(f"Lyshastigheten er {c:.2e} m/s.")


# ```{admonition} Prøv selv
# :class: tip
# Lag et program som utfører regnestykket $2^5 - 1$. Det skal så skrive ut svaret i en svarsetning slik:
# 
# **2^5-1 er lik 31**
# ```

# ```{admonition} Prøv selv
# :class: tip
# Lag et program som regner ut $\dfrac{14}{3}$ og skriver ut svaret med 3 desimaler.
# ```
