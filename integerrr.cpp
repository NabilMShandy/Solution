// Diberikan sebuah bilangan bulat positif . Tugas Anda adalah:

// Cetak setiap digit dari bilangan  dari belakang secara terpisah, dipisahkan oleh spasi.
// Hitung hasil perkalian dari semua digit bilangan .
// Input Format

// Baris pertama berisi sebuah bilangan bulat positif .

// Constraints
// 0 <= n <= 2x10^9

// Output Format

// Baris pertama berisi setiap digit dari bilangan  secara terpisah, dipisahkan oleh spasi.

// Baris kedua berisi hasil perkalian dari semua digit bilangan .

// Sample input 0
// 921

// Sample output 0
// 1 2 9
// 18 = 1 * 2 * 9

// Solution
#include <iostream>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int angka;
    cin >> angka;
    string myangka = to_string(angka);
    int pengali = 1;

    // Reverse
    for(int i = myangka.length()-1; i >= 0; i--){
        cout << myangka[i] << " ";
    }
    cout << endl;
    // Multiply
    int arr[myangka.length()];
    for(int j = 0; j < myangka.length(); j++){
        arr[j] = myangka[j] - '0';
        pengali *= arr[j];
    }
    cout << pengali << endl;
    return 0;
}
