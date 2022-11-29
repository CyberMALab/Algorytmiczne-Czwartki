# **Zadanie K**: Kot i Roomba 

## *Limit czasowy: 12s, limit pamięciowy: 1024 MB*

___

## **Treść**

Kot Bitusia, Kapitan, najbardziej na świecie lubi spać. Niestety, jakość jego snu znacząco
spadła od kiedy Bituś zdecydował się na kupno Roomby – robota do odkurzania pokojów. Jak
się bowiem okazało, Kapitan Kot boi się Roomby jak... no, po prostu bardzo się boi.

Dom Bitusia zawiera 𝑛 pokojów połączonych 𝑛 − 1 dwukierunkowymi korytarzami w taki
sposób, że z każdego pokoju da się dojść do każdego innego. Bituś zauważył, że jeśli Roomba
wjeżdża do pokoju z Kapitanem, to kot budzi się i ucieka do jednego z sąsiednich pokojów, gdzie
natychmiast ponownie zasypia. Spłoszony Kapitan ucieka całkowicie na oślep, jeśli więc z pokoju
wychodzi więcej niż jeden korytarz, to wybór każdej z opcji jest tak samo prawdopodobny (w
szczególności, może on uciec do tego pokoju, z którego właśnie przyjechała Roomba).

Podczas kolejnej długiej nocy w pracy, Bituś otworzył aplikację do obsługi Roomby i zobaczył,
że w trakcie sprzątania zwiedziła ona kolejno pokoje 𝑎1, . . . , 𝑎𝑚. Pokoje w tym ciągu mogą
się powtarzać, a każde dwa sąsiednie są połączone korytarzem. Bituś pamięta też, że przed
włączeniem Roomby kot spał w pokoju 𝑐. Co więcej, zachodzi 𝑎1 ̸= 𝑐, gdyż przezorny Kapitan
nigdy nie sypia w jednym pokoju z Roombą!

Teraz Bituś zastanawia się, jaka jest wartość oczekiwana liczby razy, gdy Roomba zbudziła
Kapitana podczas sprzątania. Pomóż odpowiedzieć na dręczące go pytanie, aby mógł znów skupić
się na pracy.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 6 000). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera dwie liczby całkowite 𝑛, 𝑐 (2 <= 𝑛 <= 1 000 000, 1 <= 𝑐 <= 𝑛),
oznaczające liczbę pokojów w domu Bitusia oraz pokój, w którym początkowo śpi Kapitan Kot.

Kolejne 𝑛 − 1 linii opisuje korytarze. Każda z nich zawiera dwie liczby całkowite 𝑢𝑖
, 𝑣𝑖
(1 <= 𝑢𝑖
, 𝑣𝑖 <= 𝑛, 𝑢𝑖 ̸= 𝑣𝑖) oznaczające, że pokoje 𝑢𝑖 oraz 𝑣𝑖 są połączone korytarzem.
Możesz założyć, że z każdego pokoju da się dojść do każdego innego.

Kolejna linia zestawu zawiera liczbę pokojów 𝑚 (1 <= 𝑚 <= 5 000 000) odwiedzonych przez
Roombę.
W ostatniej linii zestawu znajduje się ciąg 𝑚 liczb całkowitych 𝑎𝑖 (1 <= 𝑎𝑖 <= 𝑛) – ciąg pokojów
odwiedzonych przez Roombę. Każde dwa kolejne pokoje są połączone korytarzem, zachodzi też
𝑎1 ̸= 𝑐.

Suma wartości 𝑛 + 𝑚 we wszystkich zestawach nie przekroczy 12 000 000.


## **Wyjście**

Dla każdego zestawu danych wypisz jedną liczbę rzeczywistą – wartość oczekiwaną liczby
obudzeń Kapitana Kota przez Roombę. Aby odpowiedź została uznana za poprawną wystarczy,
by błąd względny lub bezwzględny nie przekraczał 10^−5
. Innymi słowy, jeśli Twój algorytm
odpowie 𝑎, zaś poprawna odpowiedź to 𝑏, to wystarczy, by zachodziło |𝑎−𝑏|
max(1,𝑏) <= 10^−5


### **Przykład:**

#### **Wejście**:

    1
    4 2
    1 2
    2 3
    4 2
    4
    1 2 3 2

#### **Wyjście**:

    1.666666666666667
