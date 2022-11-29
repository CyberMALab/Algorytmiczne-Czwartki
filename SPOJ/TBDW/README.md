# ***TBDW - Binarne Drzewa Wyszukiwawcze***

## [Link do zadania...](https://pl.spoj.com/problems/TBDW/)

### *Data dodania zadania:* **2005-06-05**

### *Zadanie dodane przez:* [**mima**](https://pl.spoj.com/users/mima)

---

## **Limity**

### *Limit czasu wykonania:* ***5s***

### *Limit długości kodu źródłowego:* ***50000B***

### *Limit pamięci:* ***1536MB***

---

## **Zadanie**

Na wejściu podana jest sekwencja instrukcji:
zapytań, modyfikacji drzew oraz przeglądania
węzłów drzewa (składnia każdego polecenia identyczna:
duża litera oznaczająca instrukcję oraz liczba),
precyzyjnie:

- **I x** : wstawienie elementu *x* do drzewa (1 <= x <= 10000),
- **D x** : usunięcie elementu *x* z drzewa ,
- **S x** : wyszukiwanie elementu *x* w drzewie,
- **X 0** : znajdowanie najmniejszego elementu w drzewie,
- **X 1** : znajdowanie największego elementu w drzewie,
- **N x** : znajdowanie następnika elementu *x*,
- **P x** : znajdowanie poprzednika elementu *x*,
- **R y** : przeglądanie wierzchołków drzewa:
  - **R 0** : metoda ***inorder***,
  - **R 1** : metoda ***preorder***,
  - **R 2** : metoda ***postorder***,

W zadaniu nie można stosować dodatkowych optymalizacji,
podczas usuwania elementu, który posiada dwóch
potomków - wstawiamy w jego miejsce jego bezpośredniego poprzednika.

---

## **Wejście**

``` text
t [liczba testów = 10]
n [liczba instrukcji do wykonania <= 10000]
instrukcje... [w jednej linii jedna instrukcja]
[kolejne testy]
```

## **Wyjście**

W pierwszej linijce odpowiedzi do danego testu powinien znaleźć się
napis: 'test nr'. Odpowiedzi podawane są w kolejnych linijkach.
W przypadku jednej z instrukcji R należy na wyjściu wydrukować
wartości kluczy w kolejnych węzłach drzewa zgodnie z porządkiem,
dla zapytań należy wydrukować wartość klucza
(dla Min, Max, Succ, Pred, Search (tak))
lub - dla Search (nie), Pred (nie) lub Succ (nie).

Zwracam uwagę, że żądanie wydrukowania następnika lub poprzednika elementu,
którego nie ma w drzewie zakończyć się powinno wydrukowaniem -.

---

## **PRZYKŁAD**

### **Wejście**

```text
4
13
I 5
I 8
I 3
I 4
I 7
R 1
I 1
R 2
S 7
S 6
N 3
D 8
R 0
10
I 4
I 2
R 0
D 2
X 1
X 0
I 1
X 0
X 0
X 1
10
I 4
P 1
I 1
R 1
I 2
I 5
R 0
D 2
I 2
P 1
11
I 3
X 0
I 2
D 3
I 1
I 5
I 4
D 4
I 4
D 4
X 1
```

---

### **Wyjście**

``` text
test 1
5 3 4 8 7
1 4 3 7 8 5
7
-
4
1 3 4 5 7
test 2
2 4
4
4
1
1
4
test 3
-
4 1
1 2 4 5
-
test 4
3
5
```
