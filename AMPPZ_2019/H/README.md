# **Zadanie H**: Oscypki

## *Limit czasowy: 2s, limit pamięciowy: 512 MB*

___

## **Treść**

Po wyjeździe na prestiżową konferencję Gry dla Dwóch Graczy oraz Algorytmy Szyfrowania,

Alicja i Bob wrócili właśnie do rodzinnego Krakowa. By odpocząć po długiej podróży, przyjaciele
planują oddać się odrobinie relaksu – który to, rzecz jasna, będzie miał formę gry dla dwojga
graczy.

Na początku gry Alicja i Bob wspólnie ułożą w rzędzie 𝑛 oscypków, ponumerowanych
kolejnymi liczbami całkowitymi od 1 do 𝑛. Wiadomym jest, że chociaż niektóre oscypki są
smaczniejsze od innych, to jednak wszystkie są smaczne – dlatego właśnie walory smakowe 𝑖-tego
oscypka określamy dodatnią liczbą całkowitą 𝑜𝑖.

Podczas gry gracze będą wykonywać ruchy naprzemiennie, przy czym pierwszy ruch wykona
Alicja. W swoim ruchu, gracz może spałaszować dowolny zbiór jeszcze nie skonsumowanych
oscypków, pod jednym warunkiem: żadne dwa oscypki o sąsiednich numerach (tj. 𝑖 oraz 𝑖+ 1 dla
pewnego 𝑖) nie mogą zostać zjedzone w jednym ruchu.

Oczywiście zarówno Alicja jak i Bob wykonują ruchy tak, by zmaksymalizować sumaryczną
smaczność zjedzonych przez siebie oscypków. Zakładając, że oboje grają optymalnie, jaka będzie
sumaryczna smaczność oscypków spożytych przez Alicję?


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 20). Potem kolejno
podawane są zestawy w następującej postaci:

Opis jednego zestawu składa się z dwóch linii. Pierwsza linia zestawu zawiera liczbę
przygotowanych przez Alicję i Boba oscypków 𝑛 (1 <= 𝑛 <= 100 000). Druga linia zestawu zawiera 𝑛 liczb całkowitych 𝑜1, 𝑜2, . . . , 𝑜𝑛 (1 <= 𝑜𝑖 <= 1 000 000) – smaczności kolejnych oscypków.


## **Wyjście**

Dla każdego zestawu danych wypisz w osobnej linii jedną liczbę całkowitą – maksymalną
sumaryczną smaczność oscypków zjedzonych przez Alicję, jeśli oboje grają optymalnie.

### **Przykład:**

#### **Wejście**:

    2
    3
    10 10 10
    4
    1 2 3 4

#### **Wyjście**:

    20
    7