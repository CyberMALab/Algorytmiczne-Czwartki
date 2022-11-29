# **Zadanie C**: Koło (z) Matematyków

## *Limit czasowy: 1s, limit pamięciowy: 512 MB*

___

## **Treść**

Koło Matematyków Studentów Uniwersytetu Jagiellońskiego imienia profesora Stanisława
Zaremby jest najstarszym tego typu kołem w Polsce. Jego początki sięgają 1893 roku. Z okazji
zbliżającego się niedługo 128-lecia istnienia, członkowie Koła postanowili urządzić happening na
płycie Rynku Głównego i utworzyć żywe koło, kładąc się wzdłuż obwodu. Oczywiście nie będzie
to idealne koło, raczej wielokąt wypukły, ale przy tak dużej liczbie studentów różnica ma być
niezauważalna (a przynajmniej tak twierdzi Prezes Koła).
Pojawiła się niestety obawa, że ze względu na wzrost niektórych członków Koła, nie
wszyscy będą mogli wziąć udział w wydarzeniu. By rozwiać wątpliwości, studenci postanowili
zamodelować problem matematycznie: Dane jest 𝑛 odcinków, o długościach odpowiednio
ℓ1, ℓ2, . . . , ℓ𝑛. Wyznaczyć największy możliwy obwód wielokąta wypukłego, którego brzeg można
utworzyć z tych odcinków (ustawiając je w dowolnej kolejności i niekoniecznie wykorzystując
wszystkie). Wielokąt musi być niezdegenerowany, czyli jego pole powierzchni musi być niezerowe.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 100 000). Potem kolejno
podawane są zestawy w następującej postaci:
Pierwsza linia zestawu zawiera liczbę studentów/odcinków 𝑛 (1 <= 𝑛 <= 100 000). Druga
linia zestawu zawiera 𝑛 liczb całkowitych ℓ1, . . . , ℓ𝑛 (1 <= ℓ𝑖 <= 109
), wzrost/długości kolejnych
studentów/odcinków.
Suma wartości 𝑛 we wszystkich zestawach danych nie przekracza 1 000 000.


## **Wyjście**

Dla każdego zestawu danych wypisz w osobnej linii największy możliwy obwód wielokąta
wypukłego utworzonego z podanych odcinków. Jeśli takiego wielokąta w ogóle nie da się utworzyć,
wypisz 0.



### **Przykład:**

#### **Wejście**:

    4
    6
    1 2 3 4 5 6
    3
    9 5 14
    4
    5 15 4 6
    2
    10 11


#### **Wyjście**:

    21
    0
    15
    0