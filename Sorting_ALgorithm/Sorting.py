#Sorting Algrithm 
class SortingAlgorithms:
    
    # Bubble Sort Implementation
    def bubble_sort(self, arr):
        """
        Optimized bubble sort with early termination
        """
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    # Selection Sort Implementation
    def selection_sort(self, arr):
        """
        Selection sort with minimum element selection
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    # Insertion Sort Implementation
    def insertion_sort(self, arr):
        """
        Insertion sort with shifting
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    # Merge Sort Implementation
    def merge_sort(self, arr):
        """
        Recursive merge sort implementation
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = j = k = 0
            
            # Merge the sorted halves
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            # Copy remaining elements
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr
    
    # Quick Sort Implementation
    def quick_sort(self, arr, low=0, high=None):
        """
        Quick sort with Hoare partition scheme
        """
        if high is None:
            high = len(arr) - 1
        
        if low < high:
            pi = self._partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)
        return arr
    
    def _partition(self, arr, low, high):
        """
        Partition function for quick sort
        """
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Heap Sort Implementation
    def heap_sort(self, arr):
        """
        Heap sort using max heap
        """
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._heapify(arr, i, 0)
        
        return arr
    
    def _heapify(self, arr, n, i):
        """
        Heapify a subtree rooted at index i
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)
    
    # Counting Sort Implementation
    def counting_sort(self, arr):
        """
        Counting sort for non-negative integers
        """
        if not arr:
            return arr
        
        max_val = max(arr)
        min_val = min(arr)
        
        # Count array
        count = [0] * (max_val - min_val + 1)
        
        # Count occurrences
        for num in arr:
            count[num - min_val] += 1
        
        # Cumulative count
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # Build output array
        output = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
        
        return output
    
    # Radix Sort Implementation
    def radix_sort(self, arr):
        """
        Radix sort using counting sort as subroutine
        """
        if not arr:
            return arr
        
        # Find maximum number to know number of digits
        max_num = max(arr)
        exp = 1
        
        while max_num // exp > 0:
            self._counting_sort_radix(arr, exp)
            exp *= 10
        
        return arr
    
    def _counting_sort_radix(self, arr, exp):
        """
        Counting sort for radix sort
        """
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # Count occurrences
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        # Cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        
        # Copy output to original array
        for i in range(n):
            arr[i] = output[i]
    
    # Bucket Sort Implementation
    def bucket_sort(self, arr, bucket_size=10):
        """
        Bucket sort implementation
        """
        if len(arr) == 0:
            return arr
        
        # Determine minimum and maximum values
        min_val = min(arr)
        max_val = max(arr)
        
        # Initialize buckets
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        
        # Distribute input array values into buckets
        for i in range(len(arr)):
            buckets[(arr[i] - min_val) // bucket_size].append(arr[i])
        
        # Sort buckets and place back into input array
        arr.clear()
        for i in range(bucket_count):
            self.insertion_sort(buckets[i])
            arr.extend(buckets[i])
        
        return arr

# Utility class for testing and analysis
class SortingAnalysis:
    def __init__(self):
        self.algorithms = SortingAlgorithms()
    
    def test_all_algorithms(self, test_arr):
        """
        Test all sorting algorithms on given array
        """
        original = test_arr.copy()
        results = {}
        
        # Test each algorithm
        algorithms = [
            ('Bubble Sort', self.algorithms.bubble_sort),
            ('Selection Sort', self.algorithms.selection_sort),
            ('Insertion Sort', self.algorithms.insertion_sort),
            ('Merge Sort', self.algorithms.merge_sort),
            ('Quick Sort', self.algorithms.quick_sort),
            ('Heap Sort', self.algorithms.heap_sort),
            ('Counting Sort', self.algorithms.counting_sort),
            ('Radix Sort', self.algorithms.radix_sort),
            ('Bucket Sort', self.algorithms.bucket_sort)
        ]
        
        for name, func in algorithms:
            try:
                arr_copy = original.copy()
                results[name] = func(arr_copy)
                print(f"{name}: {results[name][:10]}..." if len(results[name]) > 10 else results[name])
            except Exception as e:
                print(f"{name} failed: {e}")
        
        return results

# Example usage and testing
if __name__ == "__main__":
    # Create test arrays
    test_cases = {
        "Random": [64, 34, 25, 12, 22, 11, 90, 5],
        "Sorted": [1, 2, 3, 4, 5, 6, 7, 8],
        "Reverse": [8, 7, 6, 5, 4, 3, 2, 1],
        "Duplicates": [5, 2, 5, 1, 2, 3, 3, 1],
        "Single": [42],
        "Empty": []
    }
    
    analyzer = SortingAnalysis()
    
    for case_name, test_arr in test_cases.items():
        print(f"\n{case_name} Case: {test_arr}")
        print("=" * 50)
        analyzer.test_all_algorithms(test_arr)
