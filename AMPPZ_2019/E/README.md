# **Zadanie E**: Drony

## *Limit czasowy: 30s, limit pamięciowy: 1024 MB*

___

## **Treść**

Wielki Krakowski Pokaz Dronów zanosi się na najgłośniejsze wydarzenie technologiczne
tego roku. Już teraz wiadomo, że Pokaz będzie bardzo skomplikowany, i przy nieodpowiednim
przygotowaniu może dojść do tragedii. By upewnić się, że wszystko pójdzie zgodnie z planem,
władze miasta zatrudniły Ciebie – znanego algorytmika – do weryfikacji planu Pokazu.

Pokaz Dronów przebiega według ściśle ustalonego schematu. Na początku, w 𝑛 punktach na
ziemi znajdują się drony. Powierzchnię ziemi możemy potraktować jako płaszczyznę, i wprowadzić
trójwymiarowy układ współrzędnych w którym trzecia współrzędna oznacza wysokość nad
ziemią. Ponieważ początkowo każdy dron leży na ziemi, to startowe współrzędne 𝑖-tego drona
możemy opisać jako (𝑥𝑖
, 𝑦𝑖
, 0).

By umożliwić dronom łatwą komunikację, 𝑚 par dronów zostało połączonych przewodami.
Przewody leżą na ziemi w formie prostych odcinków łączących pary dronów. Wiadomo, że dla
dowolnych dwóch dronów istnieje sekwencja przewodów prowadząca od jednego do drugiego
(innymi słowy, powstała sieć przewodów jest spójna). Ponadto, aby kable łączące drony nie
poplątały się, **żadne dwa odcinki odpowiadające przewodom nie przecinają się poza
swoimi końcami.**

Podczas Pokazu wykonana zostanie sekwencja 𝑘 manewrów. Każdy manewr polega na zmianie
wysokości (tj. trzeciej współrzędnej) pewnego z dronów. Zmiany te następują jedna po drugiej,
i są wykonywane w sposób ciągły.

Rzecz jasna, podczas manewrów pary dronów połączone przewodami mogą oddalić się od
siebie na odległość większą niż były oddalone w początkowej konfiguracji. Na szczęście, przewody
użyte do połączenia dronów są rozciągliwe, a przynajmniej do pewnego stopnia – dla każdego z
przewodów znana jest maksymalna odległość euklidesowa, na którą mogą oddalić się drony, które
łączy dany przewód. W momencie gdy wartość ta zostanie przekroczona, przewód się zrywa.

Organizatorzy Pokazu spodziewają się, że podczas manewrów dronów część przewodów
pozrywa się. Jednakże dopóki cała konstrukcja pozostanie dostatecznie dobrze połączona,
komunikacja między dronami będzie możliwa, i Pokaz się uda.

Otrzymałeś listę 𝑞 krytycznych par dronów, o których wiadomo, że będą przesyłać informacje
między sobą podczas Pokazu. Dla każdej takiej pary, Organizatorzy chcą wiedzieć, czy
przesył informacji między dronami (bezpośredni lub pośredni) stanie się w pewnym momencie
niemożliwy, i jeśli tak, kiedy nastąpi pierwszy taki moment.

Pozostaje tylko mieć nadzieję, że Twój algorytm będzie dostatecznie szybki, i zdąży
odpowiedzieć na wszystkie pytania przed początkiem Pokazu!


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 400). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera liczbę dronów 𝑛 (2 <= 𝑛 <= 500 000). Każda z kolejnych 𝑛
linii zawiera dwie liczby całkowite 𝑥𝑖
, 𝑦𝑖 (|𝑥𝑖
|, |𝑦𝑖
| <= 108
) – pierwsze dwie współrzędne pozycji
początkowej 𝑖-tego drona. Żadne dwa drony nie mają tej samej pozycji początkowej.

Kolejna linia zestawu zawiera liczbę całkowitą 𝑚 (1 <= 𝑚 <= 3 · 𝑛) – liczbę przewodów
między dronami. Każda z kolejnych 𝑚 linii zawiera trzy liczby całkowite 𝑢, 𝑣, 𝑙 (1 <= 𝑢 ̸=
𝑣 <= 𝑛; 1 <= 𝑙 <= 10^9
), oznaczające odpowiednio numery dronów połączonych przewodem, oraz maksymalną długość, na którą można rozciągnąć dany przewód. Każda para dronów jest
połączona co najwyżej jednym przewodem, zaś jego maksymalna długość jest nie mniejsza niż
odległość euklidesowa początkowych lokalizacji tych dronów.

Kolejna linia zestawu zawiera liczbę manewrów 𝑘 (1 <= 𝑘 <= 500 000). Każda z kolejnych 𝑘
linii zawiera dwie liczby całkowite 𝑣, ℎ (1 <= 𝑣 <= 𝑛; |ℎ| <= 10^9
) – numer drona wykonującego dany
manewr i zmianę jego wysokości. Wysokość każdego drona pozostanie nieujemna przez cały czas
trwania Pokazu.

Kolejna linia zestawu zawiera liczbę całkowitą 𝑞 (1 <= 𝑞 <= 500 000) – liczbę krytycznych par
dronów. Każda z kolejnych 𝑞 linii zawiera dwie liczby całkowite 𝑢, 𝑣 (1 <= 𝑢 ̸= 𝑣 <= 𝑛) – parę
dronów, którą chcą zbadać Organizatorzy.

Suma wartości 𝑛 we wszystkich zestawach danych nie przekracza 1 000 000.

Suma wartości 𝑘 we wszystkich zestawach danych nie przekracza 1 000 000.

Suma wartości 𝑞 we wszystkich zestawach danych nie przekracza 1 000 000.



## **Wyjście**

Dla każdego zestawu danych wypisz w osobnej linii największy możliwy obwód wielokąta
wypukłego utworzonego z podanych odcinków. Jeśli takiego wielokąta w ogóle nie da się utworzyć,
wypisz 0.



### **Przykład:**

#### **Wejście**:

    1
    4
    0 0
    0 12
    0 24
    0 25
    3
    1 2 13
    2 3 13
    3 4 1
    4
    3 1
    2 6
    3 1
    2 -6
    4
    1 2
    2 3
    3 4
    1 4


#### **Wyjście**:

    2
    -1
    1
    1