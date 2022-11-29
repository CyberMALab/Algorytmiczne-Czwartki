# **Zadanie I**: Interesujące liczby 

## *Limit czasowy: 10s, limit pamięciowy: 1024 MB*

___

## **Treść**

Operacja ⊕ nazywana jest bitową sumą wyłączającą albo bitowym XORem. Działa ona
następująco: aby obliczyć dla dwóch liczb naturalnych wynik 𝑥 ⊕ 𝑦 zapisujemy obie w systemie
dwójkowym, po czym 𝑖-ta cyfra dwójkowa wyniku jest równa 1 wtedy i tylko wtedy, gdy dokładnie
jedna z 𝑖-tych cyfr liczb 𝑥 i 𝑦 jest równa 1. Innymi słowy, jeśli 𝑥𝑖
, 𝑦𝑖
, 𝑧𝑖 oznaczają 𝑖-tą cyfrę
odpowiednio dla 𝑥, 𝑦 i 𝑧, gdzie 𝑧 = 𝑥 ⊕ 𝑦, to 𝑧𝑖 = (𝑥𝑖 + 𝑦𝑖) mod 2. Cyfry numerujemy od
najmniej znaczących.

Dana jest liczba całkowita dodatnia 𝑘. Ciąg liczb nazwiemy interesującym, jeśli dla każdych
dwóch jego elementów ich bitowy XOR jest nie większy niż 𝑘. Mając dany ciąg liczb, wybierz z
niego jak najwięcej elementów tak, aby wybrane liczby tworzyły interesujący ciąg.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 1000). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera dwie liczby całkowite 𝑛, 𝑘 (1 <= 𝑛 <= 30 000, 1 <= 𝑘 < 2
20),
oznaczające długość ciągu i liczbę określającą maksymalny XOR dwóch elementów.

Druga linia zestawu zawiera dany ciąg 𝑛 liczb całkowitych nieujemnych, mniejszych niż 2
20
,
oddzielonych spacjami.

Suma długości ciągów we wszystkich zestawach danych nie przekracza 200 000. Suma liczb 𝑘
we wszystkich zestawach nie przekracza 3 200 000.

## **Wyjście**

Dla każdego zestawu danych wypisz jedną liczbę całkowitą – maksymalną możliwą liczbę
elementów, jakie można wybrać z wejściowego ciągu tak, aby tworzyły interesujący ciąg.

### **Przykład:**

#### **Wejście**:

    1
    7 11
    3 12 9 10 16 3 4

#### **Wyjście**:

    4

___

## **Wyjaśnienie**

Ciąg interesujący tworzą elementy 3, 9, 10 i 3, ponieważ XOR bitowy każdej pary nie
przekracza 11. Na przykład 9 ⊕ 10 = 1001_2 ⊕ 1010_2 = 11_2 = 3 <= 11. Nie da się wybrać pięciu
(ani więcej) elementów o tej własności: na przykład ciąg (3, 9, 10, 3, 4) nie nadaje się ze względu
na 4 ⊕ 9 = 100_2 ⊕ 1001_2 = 1101_2 = 13 > 11.