import java.util.*;

public class SortingComparison {

    static void printArray(int arr[]) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    // Selection Sort
    static void selectionSort(int arr[]) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    // Insertion Sort
    static void insertionSort(int arr[]) {
        int n = arr.length;

        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    // Merge Sort
    static void merge(int arr[], int left, int mid, int right) {

        int n1 = mid - left + 1;
        int n2 = right - mid;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];

        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0;
        int k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    static void mergeSort(int arr[], int left, int right) {
        if (left < right) {

            int mid = (left + right) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);

            merge(arr, left, mid, right);
        }
    }

    // Quick Sort
    static int partition(int arr[], int low, int high) {

        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {

            if (arr[j] < pivot) {
                i++;

                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    static void quickSort(int arr[], int low, int high) {

        if (low < high) {

            int pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int arr[] = new int[n];

        System.out.println("Enter elements:");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int arr1[] = arr.clone();
        int arr2[] = arr.clone();
        int arr3[] = arr.clone();
        int arr4[] = arr.clone();

        System.out.println("\nOriginal Array:");
        printArray(arr);

        long start, end;

        // Selection Sort
        start = System.nanoTime();
        selectionSort(arr1);
        end = System.nanoTime();
        System.out.println("\nSelection Sort:");
        printArray(arr1);
        System.out.println("Execution Time: " + (end - start) + " nanoseconds");

        // Insertion Sort
        start = System.nanoTime();
        insertionSort(arr2);
        end = System.nanoTime();
        System.out.println("\nInsertion Sort:");
        printArray(arr2);
        System.out.println("Execution Time: " + (end - start) + " nanoseconds");

        // Merge Sort
        start = System.nanoTime();
        mergeSort(arr3, 0, n - 1);
        end = System.nanoTime();
        System.out.println("\nMerge Sort:");
        printArray(arr3);
        System.out.println("Execution Time: " + (end - start) + " nanoseconds");

        // Quick Sort
        start = System.nanoTime();
        quickSort(arr4, 0, n - 1);
        end = System.nanoTime();
        System.out.println("\nQuick Sort:");
        printArray(arr4);
        System.out.println("Execution Time: " + (end - start) + " nanoseconds");

        sc.close();
    }
}