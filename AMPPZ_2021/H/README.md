# **Zadanie H**: Hasła 

## *Limit czasowy: 5s, limit pamięciowy: 1024 MB*

___

## **Treść**

Po udanym stażu Bajtek został zatrudniony jako ekspert ds. cyberbezpieczeństwa. Aby
samemu być dobrym przykładem dla innych, zdecydował się ustawić sobie inne hasło do poczty
e-mail, zaś inne do serwisu społecznościowego Facepalm. Niestety zapamiętanie dwóch różnych
haseł okazało się trudne, a zapisanie ich wprost na kartce naruszałoby zasady bezpieczeństwa
ustalone przez niego samego. Przezorny Bajtek wybrał więc pewną sekretną liczbę 𝑑 > 0 i zapisał
na kartce oba swoje hasła zakodowane szyfrem Cezara 1
z przesunięciem 𝑑. Zadowolony z siebie
spojrzał na swoją karteczkę i zdębiał: po zakodowaniu jego hasło do Facepalm stało się hasłem
do poczty i odwrotnie! “Co ja narobiłem...” – wykrzyknął, łapiąc się za głowę.

Ty też sprawdź się w cyberbezpieczeństwie! Mając dane pierwsze z haseł Bajtka, odtwórz
drugie lub ustal, że nie da się tego w sposób jednoznaczny zrobić.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 20). Potem kolejno
podawane są zestawy w następującej postaci:

Każdy zestaw to jedno hasło składające się z małych liter alfabetu angielskiego. Hasło ma co
najmniej 1 i co najwyżej 200 000 znaków.

Suma długości wszystkich haseł nie przekracza 1 000 000.

## **Wyjście**

Dla każdego podanego hasła wypisz odpowiadające mu drugie hasło. Jeśli drugiego hasła
nie da się odtworzyć (rozwiązanie nie istnieje albo jest więcej niż jedno), wypisz zamiast tego
pojedyncze słowo NIE.

### **Przykład:**

#### **Wejście**:

    1
    cnffjbeq

#### **Wyjście**:

    password
