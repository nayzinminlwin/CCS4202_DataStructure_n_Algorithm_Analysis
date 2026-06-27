import time
import Sorting_Seeder
import MergeSort
import QuickSort

def analyze_sorting_algorithms(n):
    # Example arrays for testing
    quick_best_case = Sorting_Seeder.generate_quicksort_best_case(n)
    quick_worst_case = Sorting_Seeder.generate_quicksort_worst_case(n)
    quick_average_case = Sorting_Seeder.generate_quicksort_average_case(n)
    
    merge_best_case = Sorting_Seeder.generate_merge_best_case(n)
    merge_worst_case = Sorting_Seeder.generate_merge_worst_case(n)
    merge_average_case = Sorting_Seeder.generate_merge_average_case(n)

    # Analyze QuickSort
    start_time = time.time()
    QuickSort.quick_sort(quick_best_case)
    end_time = time.time()
    print(f"QuickSort Best Case: {((end_time - start_time) / 1e-9) :.2f} nano-seconds")

    start_time = time.time()
    QuickSort.quick_sort(quick_worst_case)
    end_time = time.time()
    print(f"QuickSort Worst Case: {((end_time - start_time) / 1e-9) :.2f} nano-seconds")

    start_time = time.time()
    QuickSort.quick_sort(quick_average_case)
    end_time = time.time()
    print(f"QuickSort Average Case: {((end_time - start_time) / 1e-9) :.2f} nano-seconds")

    # Analyze MergeSort
    start_time = time.time()
    MergeSort.merge_sort(merge_best_case)
    end_time = time.time()
    print(f"MergeSort Best Case: {((end_time - start_time) / 1e-9) :.2f} nano-seconds")

    start_time = time.time()
    MergeSort.merge_sort(merge_worst_case)
    end_time = time.time()
    print(f"MergeSort Worst Case: {((end_time - start_time) / 1e-9) :.2f} nano-seconds")

    start_time = time.time()
    MergeSort.merge_sort(merge_average_case)
    end_time = time.time()
    print(f"MergeSort Average Case: {((end_time - start_time) / 1e-9) :.2f} nano-seconds")


if __name__ == "__main__":
    input_sizes = [100, 200, 500, 800]  # You can change these values to test with different sizes
    number_of_trials = 5  # Number of trials to average the results
    
    for n in input_sizes:
        print(f"\nAnalyzing sorting algorithms for array size: {n}")
        for _ in range(number_of_trials):
            analyze_sorting_algorithms(n)