# **Zadanie A**: AMPPZ w czasach zarazy

## *Limit czasowy: 12s, limit pamięciowy: 1024 MB*

___

## **Treść**

Organizacja Akademickich Mistrzostw Polski w Programowaniu Zespołowym w czasach
pandemii to nie lada wyzwanie. Twoim zadaniem jako Głównego Sędziego ds. Dystansu
Społecznego jest dopilnowanie, aby zachowany był odpowiedni dystans pomiędzy uczestnikami.
Zawodnicy z jednego uniwersytetu są dla siebie praktycznie jak rodzina, więc głównie martwi
Cię dystans pomiędzy studentami z różnych uniwersytetów. Intuicyjnie, chcesz aby reprezentanci
każdego uniwersytetu skupili się w zwartą grupę zachowującą odpowiedni dystans od innych grup.

Aby opisać swoją intuicję w sposób formalny, wprowadziłeś następującą zasadę. Niech
𝐴 oznacza największą odległość (euklidesową, czyli standardową odległość na płaszczyźnie)
pomiędzy dwójką studentów należących do tego samego uniwersytetu, zaś 𝐵 oznacza najmniejszą
odległość euklidesową pomiędzy dwójką studentów należących do różnych uniwersytetów. Musi
wtedy zachodzić 𝐴 < 𝐵.

Twoi goście ochoczo przyjęli zalecenia i stosowali się do nich podczas całej imprezy. Niestety,
jest pewien szkopuł: po zawodach otrzymałeś polecenie aby udowodnić, że zasada dystansu
społecznego faktycznie była respektowana. Wszyscy rozjechali się już do domów i jedyne co Ci
pozostaje, to użyć jednego ze zdjęć grupowych jako dowodu. Problem w tym, że nie wiesz którzy
zawodnicy pochodzą z których uniwersytetów. Ale skoro wiesz, że zasada dystansu społecznego
faktycznie była zachowana, może uda Ci się odtworzyć podział na uniwersytety?

Znając pozycje wszystkich studentów na zdjęciu (opisane jako punkty na płaszczyźnie 1)
oraz liczbę uniwersytetów, znajdź podział, który respektuje Twoją zasadę. 
**Każdy uniwersytet musi mieć co najmniej jednego studenta. Ponadto możesz założyć, że rozwiązanie
zawsze istnieje.**

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 100 000). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera dwie liczby całkowite 𝑛, 𝑘 (2 <= 𝑛 <= 2 000 000,
2 <= 𝑘 <= min(𝑛, 20)), oznaczające odpowiednio liczbę studentów i liczbę uniwersytetów.

Każda z kolejnych 𝑛 linii zawiera dwie liczby całkowite 𝑥𝑖
, 𝑦𝑖 (0 <= 𝑥𝑖
, 𝑦𝑖 < 109
), oznaczające
współrzędne 𝑖-tego studenta. **Żadna dwójka studentów nie stoi w tym samym punkcie.**
Sumaryczna liczba studentów we wszystkich zestawach danych nie przekroczy 10^7.

## **Wyjście**

Dla każdego zestawu danych wypisz 𝑛 liczb 𝑐1, . . . , 𝑐𝑛 (1 <= 𝑐𝑖 <= 𝑘), gdzie 𝑐𝑖 jest numerem
uniwersytetu, z którego pochodzi 𝑖-ty student. Przypisanie studentów do uniwersytetów powinno
spełniać opisaną powyżej zasadę dystansu społecznego. Jeśli istnieje wiele rozwiązań, możesz
wypisać dowolne z nich.


### **Przykład:**

#### **Wejście**:

    3
    3 2
    0 0
    0 1
    0 3
    4 4
    0 0
    0 1
    1 0
    1 1
    8 3
    3 1
    4 1
    1 6
    2 6
    6 5
    6 7
    3 2
    4 2

#### **Wyjście**:

    1 1 2
    4 1 3 2
    2 2 1 1 3 3 2 2