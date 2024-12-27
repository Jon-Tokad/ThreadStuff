import subprocess
import time
import matplotlib.pyplot as plt

# Path to the compiled C program
PROGRAM_PATH = "./thread_stuff"
MAX_THREADS = 16
RUNS_PER_THREAD = 10

def run_program(num_threads):
    """Run the C program with the specified number of threads and return the execution time."""
    start_time = time.time()
    try:
        subprocess.run([PROGRAM_PATH, str(num_threads)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"Error running program with {num_threads} threads.")
        return None
    end_time = time.time()
    return end_time - start_time

def benchmark_program():
    """Benchmark the program with thread counts from 1 to MAX_THREADS."""
    avg_times = []
    
    for threads in range(1, MAX_THREADS + 1):
        run_times = []
        print(f"Running with {threads} threads...")
        for _ in range(RUNS_PER_THREAD):
            exec_time = run_program(threads)
            if exec_time is not None:
                run_times.append(exec_time)
        avg_time = sum(run_times) / len(run_times) if run_times else 0
        avg_times.append(avg_time)
        print(f"Average Time for {threads} threads: {avg_time:.4f} seconds")
    
    return avg_times

def plot_results(avg_times):
    """Plot the average execution time for each thread count."""
    thread_counts = list(range(1, MAX_THREADS + 1))
    
    plt.figure(figsize=(10, 6))
    plt.plot(thread_counts, avg_times, marker='o', linestyle='-')
    plt.title('Average Execution Time vs Number of Threads')
    plt.xlabel('Number of Threads')
    plt.ylabel('Average Execution Time (seconds)')
    plt.xticks(thread_counts)
    plt.grid(True)
    plt.show()

def main():
    print("Starting benchmark...")
    avg_times = benchmark_program()
    plot_results(avg_times)
    print("Benchmark completed!")

if __name__ == "__main__":
    main()
