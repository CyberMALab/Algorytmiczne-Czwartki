# **Zadanie B**: Robaczek

## *Limit czasowy: 5s, limit pamięciowy: 512 MB*

___

## **Treść**

Na krakowskich Plantach jest wielkie drzewo, na którym mieszka Robaczek. Upraszczając,
możemy powiedzieć, że drzewo 1
(jak zwykle drzewa) ma 𝑛 wierzchołków, a Robaczek jest tak
długi, że zajmuje całą ścieżkę prostą 2 pomiędzy wierzchołkami 𝑎 i 𝑏.

Robaczek chce przenieść się na inną ścieżkę – pomiędzy wierzchołkami 𝑐 i 𝑑 – ponieważ tam
jest więcej słońca. Wiadomo, że ścieżka początkowa (𝑎 ↔ 𝑏) i docelowa (𝑐 ↔ 𝑑) nie mają żadnego
wspólnego wierzchołka.

Żeby zmieniać swoje miejsce na drzewie, Robaczek może wykonywać pewne ruchy:
przechodzić którymkolwiek swoim końcem do wolnego wierzchołka. Formalnie: jeśli Robaczek
aktualnie zajmuje ścieżkę pomiędzy wierzchołkami 𝑥 i 𝑦, to może w jednym kroku wybrać
wierzchołek 𝑧, który jest sąsiadem 𝑥, i który nie jest na ścieżce 𝑥 ↔ 𝑦. Następnie zwalnia
(przestaje zajmować) 𝑦, a zamiast niego zajmuje 𝑧. Analogicznie, może też wybrać wierzchołek
𝑧
′ będący sąsiadem 𝑦, zwolnić 𝑥 i zająć 𝑧
′
. Po całej operacji Robaczek dalej zajmuje pewną
ścieżkę, a jego długość nie zmieniła się.

Robaczek bardzo chce dostać się do ścieżki pomiędzy 𝑐 i 𝑑, ale jako że jest dosyć wyluzowany
i bardzo leniwy, nie planuje na to popołudnie więcej niż 10 · 𝑛 ruchów. Czy pomożesz mu w tym
zadaniu?


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 7000). Potem kolejno
podawane są zestawy w następującej postaci:
Pierwsza linia zestawu zawiera liczbę całkowitą 𝑛 (4 <= 𝑛 <= 100 000) – liczbę wierzchołków
drzewa. Każda z kolejnych 𝑛 − 1 linii zawiera dwie liczby całkowite 𝑢, 𝑣 (1 <= 𝑢 ̸= 𝑣 <= 𝑛),
oznaczające numery wierzchołków drzewa połączonych krawędzią.
Kolejna linia zestawu zawiera dwie liczby całkowite 𝑎 i 𝑏 (1 <= 𝑎 ̸= 𝑏 <= 𝑛) – końce ścieżki, na
której aktualnie leży Robaczek.
Kolejna linia zestawu zawiera dwie liczby całkowite 𝑐 i 𝑑 (1 <= 𝑐 ̸= 𝑑 <= 𝑛) – końce ścieżki, na
którą Robaczek chce się przenieść.
Liczba wierzchołków na ścieżce pomiędzy 𝑎 i 𝑏 jest dokładnie taka sama, jak liczba
wierzchołków na ścieżce pomiędzy 𝑐 i 𝑑. Możesz również założyć, że ścieżka pomiędzy 𝑎 i 𝑏
nie ma żadnego wspólnego wierzchołka ze ścieżką pomiędzy 𝑐 i 𝑑.
Suma wartości 𝑛 we wszystkich zestawach danych nie przekroczy 1 000 000.


## **Wyjście**

Dla każdego zestawu danych, jeśli robaczek nie może dostać się do swojej mety w 10·𝑛 ruchach,
wypisz −1. W przeciwnym razie wypisz możliwą trasę Robaczka. Opis takiej trasy powinien
składać się z dwu linii, pierwszej zawierającej liczbę 𝑞 (1 <= 𝑞 <= 10 ·𝑛) ruchów, i drugiej, w której
będzie 𝑞 liczb całkowitych 𝑣1, 𝑣2, . . . , 𝑣𝑞 – opisy ruchów Robaczka. Każdy opis ruchu to jedna
liczba – numer wierzchołka, do którego przechodzi Robaczek w danym ruchu. Możesz wypisać
dowolny z poprawnych ciągów ruchów – zwróć uwagę, że nie musisz minimalizować liczby ruchów, a tylko zmieścić się w limicie 10 · 𝑛. Załóż również, że Robaczek jest symetryczny i kolejność jego
końców nie ma znaczenia – może w każdym momencie pójść w obie strony, a na pola docelowe
wejść dowolnym końcem.


### **Przykład:**

#### **Wejście**:

    3
    6
    1 2
    1 3
    1 4
    4 5
    4 6
    2 3
    5 6
    15
    1 2
    1 6
    2 3
    2 4
    2 5
    6 7
    6 8
    5 9
    6 10
    9 11
    9 12
    9 13
    12 14
    14 15
    14 13
    3 6
    6
    1 2
    1 3
    2 4
    4 5
    5 6
    4 6
    3 2


#### **Wyjście**:

    -1
    7
    15 5 2 1 6 7 3
    3
    2 1 3