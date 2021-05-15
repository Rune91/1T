# 1. Output og regning

## 1.1 Skrive til skjerm (output)

Vi kan skrive tekst og verdier til konsollvinduet ved hjelp av kommandoen `print()`. Tekst må stå i anførselstegn, mens tall og variabler står uten.

print("Dette er en tekst.")
print(10)

```{admonition} Prøv selv
:class: tip
Åpne kodevinduet i Spyder. Bruk `print()` til å skrive en hyggelig hilsen. Kjør programmet med play-knappen og les hilsenen din i konsollvinduet.
```

## 1.2 Regning med Python

Vi bruker regneartene som vi er vant med fra matematikk til å regne med tall og variabler.

Operator | Betydning
:---: | :---:
+ | pluss
- | minus
* | gange
/ | dele
** | potens
// | heltallsdivisjon
% | modulo

For så styre flyten i regnestykker bruker vi paranteser akkurat som vanlig. Legg merke til at det er ikke noe problem å legge inn mellomrom i regnestykket for at det blir lettere å lese.

print(5+3)
print(3*4)
print(3**4)
print( 2*(5-1) + 7**2 - 1/(5*2) )

Heltallsdivisjon (`//`) er divisjon hvor resten blir forkastet. Modulo (`%`) finner resten i en heltallsdivisjon.

Eksempel: $\dfrac{16}{3} = 5.3333...$ Vi kjenner det også som 5 med 1 i rest.

print( 16//3 )
print( 16%3 )

```{admonition} Prøv selv
:class: tip
Regn ut disse regnestykkene med Python. Bruk `print()` til å skrive ut svaret til konsollvinduet.

$3+7*5$

$1.2*\dfrac{7}{21} + 2^8 + \dfrac{4^2-1}{2^4+1}$
```

```{admonition} Svar
:class: dropdown
$3+7*5 = 38$

$1.2*\dfrac{7}{21} + 2^8 + \dfrac{4^2-1}{2^4+1} = 257.2823429...$
```

```{admonition} Prøv selv
:class: tip
Bruk `%` til å avgjøre om tallet 1974 er delelig på 7.
```

