# **Zadanie D**: Żaby

## *Limit czasowy: 3s, limit pamięciowy: 512 MB*

___

## **Treść**

Myślisz pewnie, że żaby są znane ze skakania oraz rechotania, a okazuje się, że są też całkiem
dobrymi programistami. Twoim zadaniem będzie wybranie trzech żab, które będą w stanie
stworzyć jak najlepszą drużynę na zawody ŻAMPPZ.
W rzędzie jest 𝑁 kamieni ustawionych co 1 metr, a na każdym kamieniu siedzi jedna żaba.
Kamienie (oraz żaby) są ponumerowane 1 do 𝑁 od lewej do prawej. Żaba numer 𝑖 siedzi na 𝑖-
tym kamieniu, a do tego jest opisana liczbami 𝑟𝑖 oraz 𝑠𝑖
, oznaczającymi odpowiednio zasięg oraz
zdolności programistyczne tej żaby. Jest ona w stanie doskoczyć na dowolny kamień w odległości
co najwyżej 𝑟𝑖
, czyli dowolny kamień, którego indeks jest w przedziale [𝑖 − 𝑟𝑖
, 𝑖 + 𝑟𝑖
]. Żadna żaba
nie ma zamiaru skoczyć więcej niż raz.
Drużyna na zawody ŻAMPPZ musi składać się z trzech żab, które są w stanie wybrać dogodne
miejsce na treningi. Oznacza to, że musi istnieć kamień, na który każda z wybranych żab jest w
stanie doskoczyć jednym skokiem (być może skokiem o zerowej długości). Jaka jest największa
możliwa suma zdolności programistycznych takich trzech żab?
Przyjmując podane poniżej limity, można udowodnić, że zawsze istnieje co najmniej jedna
trójka żab spełniająca warunki zadania.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 ¬ 𝑧 ¬ 30). Potem kolejno
podawane są zestawy w następującej postaci:
Pierwsza linia zestawu zawiera liczbę całkowitą 𝑛 (3 ¬ 𝑛 ¬ 200 000) – liczbę kamieni (i
jednocześnie żab). Każda z kolejnych 𝑛 linii zawiera dwie liczby całkowite 𝑟𝑖
, 𝑠𝑖 (1 ¬ 𝑟𝑖
, 𝑠𝑖 ¬
200 000) – odpowiednio zasięg oraz zdolności programistyczne 𝑖-tej żaby.
Suma wartości 𝑛 we wszystkich zestawach danych nie przekroczy 500 000


## **Wyjście**

Dla każdego zestawu danych wypisz w osobnej linii jedną liczbę całkowitą: największą możliwą
sumę zdolności programistycznych trzech wybranych żab.

### **Przykład:**

#### **Wejście**:

    3
    4
    1 39
    2 17
    4 5
    1 40
    3
    1 10
    1 20
    1 30
    7
    5 4
    4 3
    3 2
    2 1
    3 2
    4 3
    5 4


#### **Wyjście**:

    62
    60
    11

___

## **Wyjaśnienie**

W pierwszym zestawie żaby o numerach 2, 3 i 4 mogą wszystkie doskoczyć na kamień 3
(ale też wszystkie mogą doskoczyć na kamień 4). Ich suma zdolności programistycznych wynosi
17 + 5 + 40 = 62 i jest to największa możliwa suma.
W drugim zestawie wszystkie trzy żaby są w stanie doskoczyć na kamień 2, a wynik to
10 + 20 + 30 = 60.