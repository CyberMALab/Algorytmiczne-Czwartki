# **Zadanie F**: Farba

## *Limit czasowy: 3s, limit pamięciowy: 1024 MB*

___

## **Treść**

Bajtazar powszechnie uważany jest za największego skąpca w całej gminie. Na poparcie
tej tezy można przytoczyć wiele przykładów, najmniej istotnym spośród nich jest zaś to, że
jego posesja nie posiada nawet płotu. Ostatnio jednak odnalazł on w piwnicy 𝑛 starych desek,
postanowił więc wykonać chociaż kawałek ogrodzenia.

Bajtazar położył deski na stosie tak, że kolejne z nich miały długości 𝑎1, . . . , 𝑎𝑛. Wziął
pierwszą deskę, odciął z niej fragment o długości 𝑏 i przybił jako pierwszą sztachetę, następnie
z pozostałej części odciął kolejny fragment o długości 𝑏 i przybił tuż obok. Kontynuował ten
proces, aż w rękach pozostała mu resztka deski, której długość mieściła się w przedziale [1, 𝑏].
Cóż, taka dobra deska nie może się wszak zmarnować, mimo że zdaje się być trochę przykrótka,
pomyślał Bajtazar... i również przybił ją do płotu jako kolejną sztachetę. Następnie wziął drugą
deskę ze stosu, a potem kolejną, i dla każdej z nich powtórzył opisaną procedurę.

Po ukończonej pracy, Bajtazar spojrzał na swoje dzieło i stwierdził, że przybijanie sztachet o
różnych długościach mogło jednak nie być najlepszym pomysłem. Wygląda to bardziej jak zbiór
losowych desek, niż jak przemyślana konstrukcja, pomyślał. Postanowił więc pomalować płot
białą farbą, licząc że dzięki temu będzie wyglądał on choć odrobinę bardziej profesjonalnie. Ale,
zdał sobie sprawę po chwili, jeżeli pomaluję na biało tylko co drugą sztachetę, resztę zaś pozostawię
brązową, to zużyję (około) dwukrotnie mniej farby, a ogrodzenie nadal będzie sprawiało wrażenie
spójnej i przemyślanej całości!

Jak pomyślał, tak zrobił, i pomalował w ogrodzeniu tylko co drugą sztachetę, rozpoczynając
od pierwszej 1
. Dopiero przed snem Bajtazarowi przyszła do głowy przerażająca myśl: być może
gdyby wybrał inną długość 𝑏, to zużyłby mniej farby? Cóż, teraz już niewiele da się zrobić, lecz
sama świadomość możliwego błędu nie daje Bajtazarowi spokoju. Zastanawia się więc, ile farby
musiałby zużyć, gdyby zdecydował się na zbudowanie płotu o innej spośród możliwych wysokości.

Pomóż Bajtazarowi rozwiązać ten problem i spraw, aby mógł on w końcu spokojnie (bądź
niespokojnie, zależnie od wyniku Twoich obliczeń) usnąć.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 5). Potem kolejno podawane
są zestawy w następującej postaci:

W pierwszej linii zestawu znajduje się liczba całkowita 𝑛 (1 <= 𝑛 <= 1 000 000). W drugiej
linii znajduje się 𝑛 liczb całkowitych 𝑎𝑖 (1 <= 𝑎𝑖 <= 1 000 000,
∑︀𝑛
𝑖=1 𝑎𝑖 <= 1 000 000), oznaczających
długości kolejnych desek.

## **Wyjście**

Niech 𝑀 oznacza największą spośród wszystkich wartości 𝑎𝑖 w wybranym zestawie danych.
Na wyjściu dla tego zestawu danych wypisz 𝑀 linii. W 𝑖-tej z nich powinna znajdować się jedna
liczba całkowita 𝑓𝑖
: sumaryczna długość sztachet, które Bajtazar musiałby pomalować na biało,
gdyby zdecydował się na budowanie płotu o wysokości 𝑏 = 𝑖.

### **Przykład:**

#### **Wejście**:

    1
    4
    10 7 2 8

#### **Wyjście**:

    14
    13
    15
    13
    15
    16
    21
    23
    24
    12
___

## **Wyjaśnienie**

Dla wysokości płotu 𝑏 = 4, kolejne sztachety miałyby wysokości: 4 4 2 4 3 2 4 4. Bajtazar
musiałby pomalować deski o długościach 4, 2, 3 oraz 4, więc odpowiedzią w czwartej linii jest 13.

Dla wysokości płotu 𝑏 = 5, kolejne sztachety miałyby wysokości: 5 5 5 2 2 5 3. Bajtazar
musiałby pomalować deski o długościach 5, 5, 2 oraz 3, więc odpowiedzią w piątej linii jest 15.