import random
import time
import tracemalloc

# Randomized Quicksort implementation
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partition around pivot
    less = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    equal = [x for i, x in enumerate(arr) if x == pivot]
    greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Deterministic Quicksort using first element as pivot
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    pivot = arr[0]

    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# Helper to test sorting function performance and correctness
def evaluate_sort(arr, sort_fn):
    tracemalloc.start()
    start_time = time.perf_counter()

    sorted_result = sort_fn(arr)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "is_sorted": sorted_result == sorted(arr),
        "time_taken": end_time - start_time,
        "memory_used": peak
    }


# Run evaluation on all datasets for a given sorting algorithm
def run_comparison(algorithm_name, sort_function, datasets):
    print(f"\n--- {algorithm_name} ---")
    for name, data in datasets.items():
        result = evaluate_sort(data.copy(), sort_function)
        print(f"{name}")
        print(f"  Sorted Correctly : {result['is_sorted']}")
        print(f"  Time Taken       : {result['time_taken']:.6f} seconds")

# Main execution
if __name__ == "__main__":
    dataset_size = 100  # Adjust this value for larger tests
    print("Data Set Size:", dataset_size)

    datasets = {
        "sorted_dataset": list(range(dataset_size)),
        "reverse_dataset": list(range(dataset_size - 1, -1, -1)),
        "random_dataset": random.sample(range(1, dataset_size * 2), dataset_size),
        "repeated_dataset": [random.choice([1, 2, 3, 4, 5]) for _ in range(dataset_size)]
    }

    run_comparison("Deterministic Quicksort", deterministic_quicksort, datasets)
    run_comparison("Randomized Quicksort", randomized_quicksort, datasets)
