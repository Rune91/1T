(oppgaver-a)=
# Oppgavesett A
Disse oppgavene bruker teorikapitler 1-4.

---
```{admonition} A.X: Alder
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
```{admonition} A.X: Kalkulator
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