(oppgaver-a)=
# Oppgavesett A
Disse oppgavene bruker teorikapitler 1-4.

---
```{admonition} A.1: Tallregning
:class: tip
Lag en variabel med verdien 7. Gjør følgende endringer på variabelen:
* 3 ganger så stor
* Legg til 8
* Opphøy den i andre

Skriv så ut variabelen med `print()`
```

---
```{admonition} A.2: Klokka
:class: tip
Det var midnatt for 2387199 timer siden. Hvor mye er klokka nå?
```

```{admonition} Hint!
:class: dropdown
Her er modulo-operatoren (`%`) nyttig.
```

---
```{admonition} A.3: Vinkelregning
:class: tip
Lag et program som spør brukeren om en vinkel i grader. Det skal så gjøre vinkelen om til radianer.
```

---
```{admonition} A.4: Alder
:class: tip
Lag et program som leser inn alderen til brukeren som et tall. Programmet skal så fortelle brukeren om han er et barn, en tenåring eller voksen.
```

```{admonition} Hint!
:class: dropdown
Her må du bruke blant annet:
* `int(input())`
* `if`, `elif` og `else`
* noen av operatorene `>`, `<`, `>=`, `>=`
```

---
```{admonition} A.5: Kalkulator
:class: tip
Programmet under skal lese inn to tall og en regneoperator fra brukeren. Det skal så skrive ut svaret på regnestykket.

**Men!** Det fungerer ikke fordi det er fullt av feil. Kopier koden og gjør endringer slik at det fungerer.
```



print(Velkommen til min kalkulator!)
tall_1 = input("Første tall: ")
tall_2 = input("Andre tall: ")
operator = input("+ - / eller * ")

svar = 0
if operator == "+"
    svar = tall_1 + tall_2
elif operator == "-":
    svar = tall1 - tall2
elif operator = "/":
    svar = tall_1 / tall_2
elif operator == "*":
    svar = tall_1 * tall_2
else:
print(Ugyldig operator)

print(f"{tall_1} {operator} {tall2} = {svar}")

---
```{admonition} A.6: Fortegn
:class: tip
Be brukeren om to tall. Programmet skal så avgjøre om de to tallene har likt eller ulikt fortegn. Skriv resultatet til skjerm.
```

```{admonition} Hint!
:class: dropdown
Neida, denne må du klare selv!
```