# **Zadanie G**: Glątwa Gebajta 

## *Limit czasowy: 12s, limit pamięciowy: 1024 MB*

___

## **Treść**

Jak co wiosnę, Wiedźmak Gebajt na szlak swój wyrusza, coby użyć nieco wiedźmińskiego
fachu, a i groszem kmiotów prostych sakiewkę wypchać. Szlak wiedźmaka od zachodu na wschód
się ciągnie, długi na 𝑛 stajań, co stajanie inny obiekt czeka na niego, o charakterze trojakim:

 - B 𝑏𝑖
: Leże bestyji srogiej, co na chłopkach żer bezdusznie prowadzi. Gdy wiedźmak do
potwory zawita, ta go zoczy, szponem a kłem rani niechybnie, i 𝑏𝑖 żywotności odbierze.
Jeśli żywotność wiedźmaka do zera zejdzie samego, sczeźnie on; jeśli zaś nie, brzeszczotem
swym potworzycę wnet tnie, i na miejscu ubije. Żywotność Gebajta tedy zmieni się jako
    
    >if 𝐻 <= 𝑏𝑖 then 𝑑𝑒𝑎𝑡ℎ else 𝐻 := 𝐻 − 𝑏𝑖.

 - K 𝑘𝑖
: Karczma wioskowa, gdzie Gebajt (wielce na gorzałkę łasy) wstąpić nie omieszka.
Jeśli z żywotnością mniejszą niźli 𝑘𝑖 do oberży zawita, trunkiem nad umiar upity zemrze
niechybnie. W przeciwnym zaś razie, glątwą zmożony, z żywotnością do 𝑘𝑖 pomniejszoną
przybytek o brzasku opuści. Żywotność Gebajta zmieni się jako

    >if 𝐻 < 𝑘𝑖 then 𝑑𝑒𝑎𝑡ℎ else 𝐻 := 𝑘𝑖
.

 - C 𝑐𝑖
: Czarownicy potężnej chata, w urokach a eliksirach obeznanej, co rany zdolne są
zabliźnić, glątwę zaś uleczyć. Jeśli Gebajt z żywotnością niższą jak 𝑐𝑖 do wiedźmy przybieży,
ta czaramy swemi żywotność do poziomu 𝑐𝑖 przywrócić mu zdoła. Żywotność Gebajta
zmieni się jako

    >𝐻 := 𝑚𝑎𝑥(𝐻, 𝑐𝑖).

Duma tedy wiedźmak, jaki to fragment szlaku obrać, ażeby radości wiedźmińskiej zaznać, ale
życie swe zachować. Dzień za dniem mija, a dnia 𝑖-tego jedna z dwóch rzeczy się dzieje:

 - Jeden obiekt na szlaku zmianie ulega, przykładem chatkę czarownicy miejscowy kupiec
nabywa i w karczmę zmienia, albo też nowa bestyja spod ziemi wyłazi, karczmę ogniem z
pyska pali i leże w tym miejscu zakłada;

 - Gebajt przed dom wychodzi, pod ulubionym drzewem siada i duma: gdyby od obiektu
𝑙𝑖 wędrować zaczął, i na wschód jechał, jak daleko zajechać by zdołał życia nie tracąc?
W dumaniu swym Twojej pomocy Gebajt szuka, cobyś tajemną sztuką kodów zaklinania
odpowiedź na jego pytanie znalazł.

Bacz, że wiedźmak duma jeno co począć, a nie po prawdzie na szlak rusza, tedy **zmiany na
szlaku na stałe zostają**, ale **każde wiedźmaka dumanie niezależne od inszych ostaje**,
i w każdym żywotność Gebajta spoczątku 𝐻0 jednostek wynosi.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 100 000). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera trzy liczby całkowite 𝑛, 𝑞 oraz 𝐻0 (1 <= 𝑛 <= 2 000 000,
1 <= 𝑞 <= 4 000 000, 1 <= 𝐻0 <= 1012) – długość szlaku, liczbę dni i początkową żywotność Gebajta.

Kolejne 𝑛 linii zestawu opisuje początkowy stan szlaku; 𝑖-ta zawiera literę odpowiadającą
typowi 𝑖-tego obiektu (B, K lub C), oraz liczbę (𝑏𝑖
, 𝑘𝑖
lub 𝑐𝑖
; 1 <= 𝑏𝑖
, 𝑘𝑖
, 𝑐𝑖 <= 1012) o znaczeniu
takim jak wyjaśniono powyżej.

Kolejne 𝑞 linii zestawu opisuje poszczególne dni. Linia 𝑖-ta rozpoczyna się literą Z jeśli danego
dnia następuje zmiana na szlaku, lub D jeśli następuje dumanie Gebajta.

W przypadku zmiany na szlaku, reszta linii zawiera: liczbę całkowitą 𝑥𝑖 (1 <= 𝑥𝑖 <= 𝑛),
oznaczającą obiekt ulegający zmianie, oraz literę i liczbę, w takim samym formacie jak przy opisie
stanu początkowego, oznaczające nowy obiekt. W przypadku dumania Gebajta, linia zawiera
jedną liczbę całkowitą 𝑙𝑖 (1 <= 𝑙𝑖 <= 𝑛), oznaczającą stajanie od którego zaczyna wędrować.

Łączna długość szlaków oraz łączna liczba dni nie przekroczą odpowiednio 2 000 000 i
4 000 000

## **Wyjście**

Dla każdego zestawu danych wypisz odpowiedzi na wszystkie zapytania. Dla każdego
zapytania wypisz jedną liczbę całkowitą, oznaczającą indeks najdalszego obiektu 𝑟𝑖 (𝑙𝑖 <= 𝑟𝑖 <= 𝑛)
do którego Gebajt może dojechać (i opuścić go żywym), lub −1 jeśli zginie już w starciu na
pozycji 𝑙𝑖
. Odpowiedź na zapytanie 𝑖-tego dnia powinna brać pod uwagę wszystkie zmiany z dni
wcześniejszych.

### **Przykład:**

#### **Wejście**:

    1
    4 12 10
    C 10
    B 5
    K 5
    B 6
    Z 3 K 6
    Z 1 C 11
    D 2
    D 1
    Z 3 C 1
    D 3
    Z 3 B 20
    D 3
    Z 1 C 31
    D 1
    Z 4 K 6
    D 1

#### **Wyjście**:

    2
    3
    4
    -1
    3
    4
___

## **Wyjaśnienie**

Szlak Gebajta zmienia się sześciokrotnie, w poniższy sposób:

 - [C 10, B 5, K 5, B 6] (początek)

 - [C 10, B 5, K 6, B 6] (1 dzień)

 - [C 11, B 5, K 6, B 6] (2 dzień)

 - [C 11, B 5, C 1, B 6] (5 dzień)

 - [C 11, B 5, B 20, B 6] (7 dzień)

 - [C 31, B 5, B 20, B 6] (9 dzień)

 - [C 31, B 5, B 20, K 6] (11 dzień)

Gebajt duma podczas sześciu pozostałych dni.

Trzeciego dnia Gebajt zaczyna od drugiego obiektu. Po pokonaniu bestii pozostaje mu 5
punktów żywotności, czyli o 1 za mało aby przetrwać kolejny obiekt (karczmę K 6). Najdalej jest
więc w stanie dotrzeć do drugiego obiektu.

Czwartego dnia Gebajt zaczyna od pierwszego obiektu; dzięki czarownicy ma jeden punkt
żywotności więcej, i przeżywa obiekt trzeci (karczmę), nie dając rady ostatniemu (bestii).

Szóstego dnia Gebajt zaczyna od trzeciego obiektu, który teraz jest czarownicą C 1. Z
niezmienioną liczbą punktów żywotności podąża dalej i pokonuje bestię (ostatni obiekt na szlaku).

Ósmego dnia Gebajt zaczyna od bestii B 20 której nie jest w stanie pokonać, więc odpowiedź
to -1.

Dziesiątego dnia Gebajt zaczyna od potężnej C 31, dzięki której pokonuje dwie pierwsze
bestie, nie dając jednak rady ostatniej.

Ostatniego dnia, Gebajt jest w stanie przejechać cały szlak.