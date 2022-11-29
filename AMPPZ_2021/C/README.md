# **Zadanie C**: Ciasto

## *Limit czasowy: 15s, limit pamięciowy: 1024 MB*

___

## **Treść**

Babcia Bajtmiła (znana już z zadania B, w którym wsławiła się znakomitymi pierogami)
tym razem upiekła sernik. Pokroiła go na 2𝑛 prostokątnych kawałków (w dwóch rzędach po 𝑛
kawałków) i na każdy z nich nałożyła lukier w jednym z wybranych przez siebie kolorów. Z dumą
spojrzała na swoje dzieło i zaniemówiła: powstała mozaika kolorów wyglądała paskudnie.

Bajtmiła zdecydowała, że musi zmienić układ kolorów na ładniejszy. Zamienianie kawałków
ciasta po jednym nie wchodzi jednak w grę: próba wyjęcia pojedynczego kawałka z sernika
niewątpliwie spowodowałaby ukruszenie się jego brzegów. Kto jak kto, ale babcia Bajtmiła nigdy
nie podałaby gościom ciasta, które sprawia wrażenie nierówno pokrojonego!

Na szczęście, Bajtmiła dysponuje prostokątną łopatką do ciast, na której mieszczą się
dokładnie cztery kawałki (w dwóch rzędach po dwa kawałki). Za jej pomocą jest w stanie ostrożnie
wyciągnąć takie cztery kawałki z ciasta, po czym – obróciwszy łopatkę – włożyć je od przeciwnej
strony z powrotem w to samo miejsce. Operacja taka może być opisana jako wybranie pewnego
kwadratu o wymiarach 2 na 2 i obrócenie go o 180 stopni.

Nauczona doświadczeniem, babcia od razu zwróciła się o pomoc do Ciebie i poprosiła o
wyznaczenie najmniejszej możliwej liczby ruchów, która zamieni układ kolorów na ładniejszy.
Oczywiście zrobiłaś to, co każdy zrobiłby na Twoim miejscu: odpowiedziałaś, że nie podejmiesz
się tego zadania, ponieważ specyfikacja wymagań jest nieprecyzyjna. Bajtmiła nie zraziła się
jednak: narysowała na tablicy pewną konkretną ładnie wyglądającą mozaikę kolorów (również o
wymiarach 2 na 𝑛) i poprosiła Cię o wyznaczenie minimalnej liczby ruchów, doprowadzającej
sernik do dokładnie tej postaci.

Oczywiście, mogło się również zdarzyć, że babcia (zmęczona przenoszeniem pierogów w
zadaniu B) pomyliła się i układu kolorów narysowanego na tablicy w ogóle nie da się w opisany
sposób uzyskać. W takim przypadku również jak najszybciej musisz jej o tym powiedzieć.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 10 000). Potem kolejno
podawane są zestawy w następującej postaci:

W pierwszej linii zestawu znajduje się liczba całkowita 𝑛 (2 <= 𝑛 <= 500 000). Następne
dwie linie wejścia opisują początkowe kolory dwóch rzędów sernika. Każda z tych linii zawiera
𝑛 liczb całkowitych z przedziału [1, 10^9
] oddzielonych pojedynczymi spacjami — identyfikatory
kolorów na kolejnych kawałkach sernika. Zauważ, że kolory mogą być użyte wielokrotnie, zatem
identyfikatory mogą się powtarzać.

Kolejne dwie linie opisują, w takim samym formacie, docelowy układ kolorów.
Suma wszystkich wartości 𝑛 we wszystkich zestawach danych nie przekracza 2 000 000.

## **Wyjście**

Dla każdego zestawu danych wypisz jedną liczbę — minimalną liczbę operacji niezbędnych do
uzyskania pożądanego układu kolorów. Jeśli wymaganej konfiguracji nie da się osiągnąć, zamiast
tego wypisz liczbę −1.

### **Przykład:**

#### **Wejście**:

    2
    4
    1 2 3 2
    4 3 1 3
    3 2 1 1
    2 3 4 3
    2
    1 2
    3 4
    3 4
    1 2

#### **Wyjście**:

    3
    -1

___

## **Wyjaśnienie**

W pierwszym teście sernik o początkowej konfiguracji
    
    1 2 3 2
    4 3 1 3

możemy przeprowadzić w żądaną konfigurację za pomocą następujących trzech kroków:

>**Odwrócenie skrajnie lewego kwadratu**

    3 4 3 2
    2 1 1 3

>**Odwrócenie skrajnie prawego kwadratu**

    3 4 3 1
    2 1 2 3

>**Odwrócenie środkowego kwadratu**

    3 2 1 1
    2 3 4 3

W drugim teście pierwszej konfiguracji nie da się w żaden sposób przeprowadzić na drugą.
