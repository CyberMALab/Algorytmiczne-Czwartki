# **Zadanie L**: Leniwce

## *Limit czasowy: 10s, limit pamięciowy: 1024 MB*

___

## **Treść**

Wyruszasz na wyprawę do dżungli w celu obserwacji mało dotychczas zbadanego gatunku
leniwców Choloepus manhattani. Cały obszar dżungli, na którym żyją leniwce, to jedno z
najdziwniejszych miejsc na świecie: drzewa rosną tam ustawione w idealny prostokąt 𝑛 × 𝑚.
Na Twojej mapie oznaczone są parami liczb naturalnych – drzewo (𝑖, 𝑗) rośnie na przecięciu 𝑖-
tego wiersza oraz 𝑗-tej kolumny. Wszystkie leniwce z gatunku Choloepus manhattani żyją na tym
obszarze.

Każdy leniwiec ma swoje stałe legowisko na jednym z drzew, ale czasem wyrusza z niego
na okoliczne drzewa w poszukiwaniu pożywienia. Po dżungli leniwce poruszają się wyłącznie
przeskakując z drzewa na drzewo – w jednym skoku leniwiec przenosi się na drzewo, które
sąsiaduje z poprzednim w poziomie lub w pionie. Aby nie oddalić się za bardzo od legowiska, każdy
leniwiec żeruje tylko w zasięgu 𝑘 skoków od niego. Innymi słowy, jeśli legowisko jest na drzewie
(𝑥, 𝑦), to obszarem żerowania leniwca jest zbiór drzew o współrzędnych (𝑥
′
, 𝑦′
) spełniających
|𝑥 − 𝑥
′
| + |𝑦 − 𝑦
′
| <= 𝑘 (oraz 1 <= 𝑥
′ <= 𝑛, 1 <= 𝑦
′ <= 𝑚). Stała 𝑘 jest wspólna dla wszystkich
leniwców, ustalona przez miliony lat ewolucji.

Masz pewne wątpliwości co do tych fantastycznych doniesień, ale nie będziesz w stanie
ich skonfrontować z poprzednim badaczem, bowiem ten pewnego dnia zniknął w dżungli w
niewyjaśnionych okolicznościach (co między innymi skłoniło Cię do przemyśleń, czy leniwce
na pewno są roślinożerne...). Pozostała po nim jedynie mapa o wymiarach 𝑛 × 𝑚, na której
odpowiednio oznaczone są wszystkie drzewa, na których żerują leniwce. Na mapie nie zostały
jednak zaznaczone ich legowiska.

Sprawdź, czy mapa w ogóle może być poprawna – rozstrzygnij, czy istnieje taki zbiór legowisk,
dla którego obszary żerowania leniwców będą dokładnie odpowiadały tej mapie.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 4 000). Potem kolejno
podawane są zestawy w następującej postaci:

W pierwszej linii zestawu znajdują się liczby całkowite 𝑛, 𝑚, 𝑘 (1 <= 𝑛, 𝑚, 𝑘 <= 1 000) o
znaczeniu podanym w treści zadania.

W kolejnych 𝑛 liniach znajduje się opis mapy – po 𝑛 znaków w każdej linii. Jeżeli według
mapy leniwce żerują na drzewie (𝑖, 𝑗), to w 𝑖-tej linii na 𝑗-tej pozycji znajdzie się znak x, w
przeciwnym wypadku znajdzie się tam znak . (kropka).

Suma wartości 𝑛 + 𝑚 + 𝑘 we wszystkich zestawach nie przekracza 100 000.

## **Wyjście**

Dla każdego zestawu danych wypisz pojedynczy napis TAK lub NIE oznaczający odpowiedź na
pytanie, czy pozostawiona przez poprzedniego badacza mapa może opisywać poprawne obszary
żerowania leniwców.

### **Przykład:**

#### **Wejście**:

    2
    3 3 1
    .xx
    xxx
    xx.
    3 4 1
    ..xx
    x.xx
    x..x

#### **Wyjście**:

    TAK
    NIE

___

## **Wyjaśnienie**

W pierwszym teście zaznaczony obszar jest poprawnym terenem żerowania dla trzech
leniwców, jeśli przyjmiemy, że zamieszkują pola (1, 3), (2, 2) oraz (3, 1).

W drugim teście nie istnieje zbiór pól zamieszkanych przez leniwce, który generowałby
zaznaczony obszar żerowania.
