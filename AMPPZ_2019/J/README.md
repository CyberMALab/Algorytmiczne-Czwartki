# **Zadanie J**: Anteny

## *Limit czasowy: 8s, limit pami臋ciowy: 512 MB*

___

## **Tre艣膰**

W tajnej bazie wojskowej testowana jest nowa technologia komunikacji radiowej. Na potrzeby
eksperymentu w obr臋bie bazy postawiono 饾憵 anten nadawczo-odbiorczych. Teren bazy jest
ca艂kowicie p艂aski i ma z lotu ptaka kszta艂t wielok膮ta wypuk艂ego. Wzd艂u偶 brzegu tego wielok膮ta
przebiega specjalny mur, kt贸ry mi臋dzy innymi zabezpiecza fale radiowe przed pods艂uchem.
Z powodu przebudowy architektury bazy konieczne b臋dzie wyburzenie fragment贸w muru
odpowiadaj膮cym pewnym dwu bokom wielok膮ta. To niestety wystawi testowan膮 technologi臋 na
ryzyko pods艂uchu: je偶eli mo偶na rozmie艣ci膰 na zewn膮trz bazy dw贸ch szpieg贸w w taki spos贸b,
by w linii prostej pomi臋dzy nimi znalaz艂y si臋 dwie anteny i by linii tej nie przedzieli艂 偶aden
fragment muru, to komunikacj臋 mi臋dzy tymi dwiema antenami mo偶na przechwyci膰. Rozwa偶asz
r贸偶ne scenariusze usuni臋cia dwu fragment贸w muru. Twoim zadaniem jest wyznaczy膰 dla ka偶dego
z tych scenariuszy, ile par anten b臋dzie zagro偶onych pods艂uchem w tym scenariuszu.

___

___

Powy偶szy rysunek przedstawia przyk艂adow膮 baz臋, kt贸rej teren jest pi臋ciok膮tem, i w obr臋bie
kt贸rej znajduj膮 si臋 cztery anteny oznaczone krzy偶ykami. Liniami przerywanymi zaznaczono
wszystkie proste przechodz膮ce przez pary r贸偶nych anten. Rysunek odpowiada pierwszemu
zestawowi danych z przyk艂adowego wej艣cia przedstawionego w dalszej cz臋艣ci tre艣ci.


## **Wej艣cie**

Pierwsza linia wej艣cia zawiera liczb臋 zestaw贸w danych 饾懅 (1 <= 饾懅 <= 200 000). Potem kolejno
podawane s膮 zestawy w nast臋puj膮cej postaci:

Pierwsza linia zestawu zawiera liczb臋 ca艂kowit膮 饾憶 (3 <= 饾憶 <= 10) 鈥? liczb臋 wierzcho艂k贸w
wielok膮ta okre艣laj膮cego teren bazy. Nast臋pne 饾憶 linii zawiera 饾憶 par liczb ca艂kowitych 鈥? wsp贸艂rz臋dne kolejnych wierzcho艂k贸w wielok膮ta zgodnie z ruchem wskaz贸wek zegara. Wierzcho艂ki numerujemy
od 0 zgodnie z ich kolejno艣ci膮 pojawiania si臋 na wej艣ciu. Kolejna linia zestawu zawiera
liczb臋 ca艂kowit膮 饾憵 (2 <= 饾憵 <= 50 000) 鈥? liczb臋 anten. Dalsza cz臋艣膰 zestawu sk艂ada si臋 z 饾憵 linii,
ka偶da zawieraj膮ca par臋 liczb ca艂kowitych 鈥? s膮 to wsp贸艂rz臋dne anten. W nast臋pnej linii znajduje
si臋 liczba ca艂kowita 饾憺 (1 <= 饾憺 <= 10) 鈥? liczba zapyta艅. Ostatnie 饾憺 linii zestawu zawiera 饾憺 par
liczb ca艂kowitych (饾憥1, 饾憦1), . . . ,(饾憥饾憺, 饾憦饾憺) (0 <= 饾憥饾憱 < 饾憦饾憱 <= 饾憶 鈭? 1), opisuj膮cych 饾憺 zapyta艅. Para (饾憥饾憱
, 饾憦饾憱)
oznacza zapytanie o liczb臋 nieuporz膮dkowanych par r贸偶nych anten, takich 偶e przechodz膮ca przez
nie prosta przecina bok mi臋dzy wierzcho艂kami o numerach 饾憥饾憱 oraz 饾憥饾憱 + 1, a tak偶e bok mi臋dzy
wierzcho艂kami o numerach 饾憦饾憱 oraz (饾憦饾憱 + 1) mod 饾憶.

Wszystkie wsp贸艂rz臋dne s膮 liczbami ca艂kowitymi nieprzekraczaj膮cymi na modu艂 10^9.
W obr臋bie zestawu danych, wszystkie pojawiaj膮ce si臋 punkty s膮 r贸偶ne i nie ma trzech
wsp贸艂liniowych. Mi臋dzy ka偶dymi dwoma zestawami danych oraz przed pierwszym zestawem
znajduje si臋 pusta linia.

Suma warto艣ci 饾憵 we wszystkich zestawach danych nie przekracza 300 000.



## **Wyj艣cie**

Dla ka偶dego zestawu danych wypisz w osobnej linii odpowiedzi na kolejne zapytania,
oddzielaj膮c je spacjami.

### **Przyk艂ad:**

#### **Wej艣cie**:

    2
    5
    0 0
    0 5
    3 7
    6 5
    6 0
    4
    1 2
    1 3
    5 2
    5 3
    3
    0 3
    1 4
    1 2
    4
    -1 -1
    -1 1
    2 1
    2 -1
    2
    0 0
    1 0
    6
    0 1
    0 2
    0 3
    1 2
    1 3
    2 3

#### **Wyj艣cie**:

    4 1 0
    0 1 0 0 0 0