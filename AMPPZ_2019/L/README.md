# **Zadanie L**: Obwarzanek

## *Limit czasowy: 30s, limit pamięciowy: 8 MB*

___

## **Treść**

Z pewnością widzieliście – a może nawet i próbowaliście – słynnych krakowskich obwarzanków.
Ale czy aby na pewno były to właściwe obwarzanki? W tym zadaniu nauczycie się je dokładnie
rozpoznawać.

*Obwarzankiem*, dla pewnego środka (𝑎, 𝑏) (gdzie 𝑎, 𝑏 są całkowite) oraz promieni 𝐿
i 𝑅 (również całkowitych, a przy tym nieujemnych) nazwiemy zbiór punktów kratowych
(całkowitych) płaszczyzny, których odległość od (𝑎, 𝑏) zawiera się w przedziale (𝐿, 𝑅]. Innymi
słowy, jest to zbiór {(𝑥, 𝑦) ∈ Z × Z : 𝐿 < 𝑑𝑖𝑠𝑡((𝑥, 𝑦),(𝑎, 𝑏)) <= 𝑅}, gdzie 𝑑𝑖𝑠𝑡 oznacza zwykłą,
euklidesową odległość.

Zaczynamy od pustego zbioru i dodajemy do niego po jednym punkcie kratowym.
Rozstrzygnij, po każdym dodanym punkcie, czy aktualny zbiór jest obwarzankiem.

*Zwróć uwagę, że to zadanie ma niski limit pamięci – 8MB.*


## **Wejście**

Pierwsza linia wejścia zawiera liczbę punktów 𝑛 (2 · 107 <= 𝑛 <= 2.5 · 107
). Kolejnych 𝑛 linii
zawiera po jednym dodawanym punkcie, podanym jako współrzędne oddzielone pojedynczym
odstępem. Współrzędne są liczbami całkowitymi, których wartość bezwzględna nie przekracza
5000. Wszystkie podane punkty są różne

## **Wyjście**

Dla każdego dodawanego punktu wypisz w osobnej linii **TAK**, jeśli po jego dodaniu aktualny
zbiór jest obwarzankiem, a **NIE**, jeśli nie jest.

### **Przykład:**

#### **Wejście**:

    12
    4 1
    3 2
    3 0
    2 3
    1 0
    0 1
    1 2
    2 -1
    2 2
    3 1
    2 0
    1 1


#### **Wyjście**:

    NIE
    NIE
    NIE
    NIE
    NIE
    NIE
    NIE
    TAK
    NIE
    NIE
    NIE
    TAK
