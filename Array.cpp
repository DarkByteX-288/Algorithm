#include <iostream>
using namespace std;

class Array {
    int *A;
    int size;
    int length;
public:
    Array(int sz) {
        size = sz;
        length = 0;
        A = new int[size];
    }
    ~Array() {
        delete[] A;
    }

    void insert(int index, int value) {
        if(index >= 0 && index <= length && length < size) {
            for(int i = length; i > index; i--)
                A[i] = A[i-1];
            A[index] = value;
            length++;
        }
    }

    void append(int value) {
        if(length < size) {
            A[length++] = value;
        }
    }

    void display() {
        for(int i = 0; i < length; i++)
            cout << A[i] << " ";
        cout << endl;
    }

    int sum() {
        return sumRec(0);
    }

    int sumRec(int idx) {
        if(idx == length) return 0;
        return A[idx] + sumRec(idx + 1);
    }

    int search(int key) {
        return searchRec(0, key);
    }

    int searchRec(int idx, int key) {
        if(idx == length) return -1;
        if(A[idx] == key) return idx;
        return searchRec(idx + 1, key);
    }

    int get(int index) {
        if(index >= 0 && index < length)
            return A[index];
        return -1;
    }

    void set(int index, int value) {
        if(index >= 0 && index < length)
            A[index] = value;
    }

    int max() {
        if(length == 0) {
            cout << "Array is empty." << endl;
            return -1; // or throw an exception if preferred
        }
        return maxRec(0, A[0]);
    }

    int maxRec(int idx, int currentMax) {
        if(idx == length) return currentMax;
        if(A[idx] > currentMax) currentMax = A[idx];
        return maxRec(idx + 1, currentMax);
    }
};

int main() {
    Array arr(10);
    arr.append(10);
    arr.append(20);
    arr.append(30);
    arr.append(40);
    arr.append(50);

    cout << "Array: ";
    arr.display();

    cout << "Sum (recursive): " << arr.sum() << endl;
    cout << "Search 30 (recursive): " << arr.search(30) << endl;
    cout << "Max (recursive): " << arr.max() << endl;

    arr.insert(2, 25);
    cout << "After insert at index 2: ";
    arr.display();

    arr.set(0, 5);
    cout << "After set index 0 to 5: ";
    arr.display();

    return 0;
}