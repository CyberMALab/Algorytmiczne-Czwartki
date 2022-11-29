# **Zadanie F**: Fantastyczna kompresja

## *Limit czasowy: 3s, limit pamięciowy: 512 MB*

___

## **Treść**

Franek miał jedno zadanie: zapamiętać permutację 𝑃, składającą się z 𝑛 liczb całkowitych
od 1 do 𝑛. To jednak przerosło Franka, bo liczb do zapamiętania było za dużo. Wymyślił
zatem fantastyczną metodę kompresowania permutacji: wybrał pewną małą liczbę 𝑘, a następnie,
zamiast permutacji, zapamiętał sumy wszystkich jej spójnych podciągów o długości 𝑘. Innymi
słowy, Franek zapamiętał ciąg 𝑆 = (𝑆1, 𝑆2, . . . , 𝑆𝑛−𝑘+1), gdzie:

 - 𝑆1 = 𝑃1 + 𝑃2 + . . . + 𝑃𝑘,
  
 - 𝑆2 = 𝑃2 + 𝑃3 + . . . + 𝑃𝑘+1,
  
 - . . .
  
 - 𝑆𝑛−𝑘+1 = 𝑃𝑛−𝑘+1 + 𝑃𝑛−𝑘+2 + . . . + 𝑃𝑛.

Dość szybko się jednak okazało, że taka kompresja wcale nie jest fantastyczna, i to co najmniej
z kilku powodów. Przede wszystkim, Franek ze zgrozą odkrył, że wiele permutacji może się
skompresować do tego samego ciągu. Co więcej, nie jest nawet pewien, czy dobrze udało mu się
wyliczyć i zapamiętać sumy. Możliwe, że permutacja w ogóle została utracona.

Mając dany ciąg 𝑆, pomóż Frankowi znaleźć wszystkie możliwe permutacje 𝑃, które
kompresują się do tego ciągu.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 1000). Potem kolejno
podawane są zestawy w następującej postaci:
W pierwszej linii zestawu podana jest długość permutacji 𝑛 oraz wybrana przez Franka liczba
całkowita 𝑘 (2 <= 𝑛 <= 25 000; 2 <= 𝑘 <= min(𝑛, 6)). W drugiej linii podane jest 𝑛 − 𝑘 + 1 liczb
całkowitych: kolejne wyrazy ciągu 𝑆 (1 <= 𝑆𝑖 <= 1 000 000).
Łączna długość wszystkich permutacji nie przekracza 250 000.


## **Wyjście**

Dla każdego zestawu danych wypisz najpierw liczbę 𝑐 permutacji, które odpowiadają
skompresowanej postaci, a następnie, w kolejnych 𝑐 liniach, te permutacje posortowane
leksykograficznie. Każdą permutację wypisz w postaci 𝑛 liczb całkowitych, z zakresu od 1 do
𝑛, rozdzielonych pojedynczymi odstępami.
Możesz założyć, że 𝑐 nie przekroczy 1 000.



### **Przykład:**

#### **Wejście**:

    2
    5 3
    8 10 12
    5 3
    10 10 10


#### **Wyjście**:

    2
    1 2 5 3 4
    2 1 5 4 3
    0