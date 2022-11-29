# Akademickie Mistrzostwa Polski w Programowaniu Zespołowy 2019

## Opis

### [Strona UJ](https://amppz.tcs.uj.edu.pl/2019/data.html)

Katalog zawiera zadania wystawione podczas AMPPZ w roku 2019.

___

### **Język programowania:** *C, C++, Python*

___

## **Struktura katalogu**

``` text
    <zadanie>\:
    |-- <data>\:
        |
        |-- <dane_wejściowe>.in
        |-- <dane_wyjściowe>.out
    
    |-- <treść_zadania.pdf>
    |-- <treść_zadania.md>
    |-- <skrypt>
    
    <zadanie>\:
    |

    ...
```

___

## **Porady**

### **Przekierowanie wejścia**

W celu szybszego testowania danych wejściowych zalecane jest
przekierowania standardowego strumienia wejściowego na plik *.in*.

Poniżej przykłady implementacji:

### Python

``` python
import sys

stream_in = 'path/to/sample.in'

sys.stdin = open(stream_in, 'r')
```

### C++

``` cpp
#include <iostream>
#include <fstream>

using namespace std;

const char * stream_in  = "path/to/sample.in";

ifstream in(stream_in);

// -- optional performance optimizations
ios_base::sync_with_stdio(false);
cin.tie(0);

cin.rdbuf(in.rdbuf());
```
