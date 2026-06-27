import random
import sys
import math

from time import perf_counter

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

import MergeSort
import QuickSort
import Sorting_Seeder


INPUT_SIZES = [100, 200, 500, 800, 1000]
NUMBER_OF_TRIALS = 5

sys.setrecursionlimit(10000)


def benchmark_sort(sort_function, input_generator, n, trials):
    total_elapsed = 0.0

    for _ in range(trials):
        arr = input_generator(n)
        start_time = perf_counter()
        sort_function(arr)
        total_elapsed += perf_counter() - start_time

    return (total_elapsed / trials) * 1000.0


def collect_case_data(quicksort_generator, mergesort_generator, sizes, trials):
    quicksort_times = []
    mergesort_times = []

    for n in sizes:
        quicksort_times.append(
            benchmark_sort(QuickSort.quick_sort, quicksort_generator, n, trials)
        )
        mergesort_times.append(
            benchmark_sort(MergeSort.merge_sort, mergesort_generator, n, trials)
        )

    return quicksort_times, mergesort_times


def plot_case(case_title, sizes, quicksort_times, mergesort_times, output_file):
    plt.figure(figsize=(9, 5.5))
    plt.plot(sizes, quicksort_times, marker="o", linewidth=2, label="QuickSort")
    plt.plot(sizes, mergesort_times, marker="s", linewidth=2, label="MergeSort")
    plt.title(case_title)
    plt.xlabel("Input size n")
    plt.ylabel("Time (ms)")
    plt.grid(True, linestyle="--", alpha=0.35)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()
    

def calculate_constant_trick(sizes, quick_times, merge_times, case_name, is_worst_case_quick=False):
    print(f"\n--- {case_name} ---")
    print("n\t | MergeSort c (Time / n log n) | QuickSort c")
    print("-" * 60)
    
    for i, n in enumerate(sizes):
        # Calculate n log n (using base 2)
        n_log_n = n * math.log2(n)
        
        # Calculate c for MergeSort (always O(n log n))
        c_merge = merge_times[i] / n_log_n
        
        # Calculate c for QuickSort
        if is_worst_case_quick:
            # Worst case is O(n^2), so divide by n^2
            c_quick = quick_times[i] / (n ** 2)
            quick_label = "(Time / n^2)"
        else:
            # Best/Average case is O(n log n), so divide by n log n
            c_quick = quick_times[i] / n_log_n
            quick_label = "(Time / n log n)"
            
        print(f"{n}\t | {c_merge:.6f}\t\t\t| {c_quick:.6f} {quick_label if i==0 else ''}")

# Add these lines inside your main() function, right after the plot_case() calls:

# print("\n=== PHASE 4: CONSTANT TRICK CALCULATIONS ===")
# calculate_constant_trick(INPUT_SIZES, best_quick, best_merge, "BEST CASE", is_worst_case_quick=False)
# calculate_constant_trick(INPUT_SIZES, average_quick, average_merge, "AVERAGE CASE", is_worst_case_quick=False)
# calculate_constant_trick(INPUT_SIZES, worst_quick, worst_merge, "WORST CASE", is_worst_case_quick=True)


def main():
    random.seed(42)

    best_quick, best_merge = collect_case_data(
        Sorting_Seeder.generate_quicksort_best_case,
        Sorting_Seeder.generate_merge_best_case,
        INPUT_SIZES,
        NUMBER_OF_TRIALS,
    )
    worst_quick, worst_merge = collect_case_data(
        Sorting_Seeder.generate_quicksort_worst_case,
        Sorting_Seeder.generate_merge_worst_case,
        INPUT_SIZES,
        NUMBER_OF_TRIALS,
    )
    average_quick, average_merge = collect_case_data(
        Sorting_Seeder.generate_quicksort_average_case,
        Sorting_Seeder.generate_merge_average_case,
        INPUT_SIZES,
        NUMBER_OF_TRIALS,
    )

    plot_case(
        "Best Case Running Time",
        INPUT_SIZES,
        best_quick,
        best_merge,
        "img/best_case_comparison.png",
    )
    plot_case(
        "Worst Case Running Time",
        INPUT_SIZES,
        worst_quick,
        worst_merge,
        "img/worst_case_comparison.png",
    )
    plot_case(
        "Average Case Running Time",
        INPUT_SIZES,
        average_quick,
        average_merge,
        "img/average_case_comparison.png",
    )
    print("Saved best_case_comparison.png, worst_case_comparison.png, and average_case_comparison.png")
    
    calculate_constant_trick(INPUT_SIZES, best_quick, best_merge, "BEST CASE", is_worst_case_quick=False)
    calculate_constant_trick(INPUT_SIZES, average_quick, average_merge, "AVERAGE CASE", is_worst_case_quick=False)
    calculate_constant_trick(INPUT_SIZES, worst_quick, worst_merge, "WORST CASE", is_worst_case_quick=True)


if __name__ == "__main__":
    main()