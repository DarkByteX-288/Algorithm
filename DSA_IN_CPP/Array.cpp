// using array to insert delete search and disply an element 
#include <iostream>
using namespace std;

class Array {
private:
    int arr[100];  // static array with max size 100
    int size;      // current number of elements

public:
    // Constructor
    Array() {
        size = 0;
    }

    // Function to insert element
    void insert(int element) {
        if (size < 100) {
            arr[size] = element;
            size++;
            cout << "Inserted " << element << " successfully.\n";
        } else {
            cout << "Array is full!\n";
        }
    }

    // Function to delete element
    void remove(int element) {
        int index = -1;
        for (int i = 0; i < size; i++) {
            if (arr[i] == element) {
                index = i;
                break;
            }
        }
        if (index != -1) {
            for (int i = index; i < size - 1; i++) {
                arr[i] = arr[i + 1];
            }
            size--;
            cout << "Deleted " << element << " successfully.\n";
        } else {
            cout << "Element not found!\n";
        }
    }

    // Function to search element
    int search(int element) {
        for (int i = 0; i < size; i++) {
            if (arr[i] == element)
                return i;
        }
        return -1;
    }

    // Function to display all elements
    void display() {
        if (size == 0) {
            cout << "Array is empty.\n";
            return;
        }
        cout << "Array elements: ";
        for (int i = 0; i < size; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

// Main Function
int main() {
    Array a;
    int choice, element;

    while (true) {
        cout << "\n------ Array Operations ------\n";
        cout << "1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter element to insert: ";
                cin >> element;
                a.insert(element);
                break;
            case 2:
                cout << "Enter element to delete: ";
                cin >> element;
                a.remove(element);
                break;
            case 3:
                cout << "Enter element to search: ";
                cin >> element;
                int index;
                index = a.search(element);
                if (index != -1)
                    cout << "Element found at index " << index << endl;
                else
                    cout << "Element not found.\n";
                break;
            case 4:
                a.display();
                break;
            case 5:
                cout << "Exiting program...\n";
                return 0;
            default:
                cout << "Invalid choice! Try again.\n";
        }
    }
}
