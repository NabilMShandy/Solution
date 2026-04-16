// Diberikan dua bilangan bulat positif  dan , tugas Anda adalah mencari Faktor Persekutuan Terbesar (FPB) dari  dan . FPB adalah bilangan bulat terbesar yang merupakan faktor dari kedua bilangan  dan .

// Input Format
// Baris pertama berisi dua bilangan bulat positif  dan  yang dipisahkan oleh spasi.

// Output Format
// Cetak FPB dari a dan b

// Sample Input 0
// 20 15

// Sample Output 0
// 5

#include <iostream>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a, b;
    cin >> a >> b;
    
    while(b!=0){
        int temp = b;
        b = a%b;
        a = temp;
}
    cout << a;
    return 0;
}