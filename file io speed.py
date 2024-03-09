import os
import time
import numpy as np

def file_io_operations(writeRepetitions, totalIterations, stringLength):
    filename = "fileio.txt"
    if not os.path.exists(filename):
        open(filename, 'a').close()

    # Create a string of '1's of the specified length
    theString = "1" * stringLength

    write_times = []
    read_times = []

    for iteration in range(1, totalIterations + 1):
        start_write = time.perf_counter()
        with open(filename, 'w') as file:
            for _ in range(writeRepetitions):
                file.write(theString)
        end_write = time.perf_counter()
        write_time = end_write - start_write
        write_times.append(write_time)

        start_read = time.perf_counter()
        with open(filename, 'r') as file:
            content = file.read()
        end_read = time.perf_counter()
        read_time = end_read - start_read
        read_times.append(read_time)

        print(f"Iteration {iteration}: Write Time = {write_time} s, Read Time = {read_time} s")

    print("Write time information: Average = {:.5f} s, Median = {:.5f} s, Min = {:.5f} s, Max = {:.5f} s".format(
        np.mean(write_times), np.median(write_times), np.min(write_times), np.max(write_times)))
    print("Read time information: Average = {:.5f} s, Median = {:.5f} s, Min = {:.5f} s, Max = {:.5f} s".format(
        np.mean(read_times), np.median(read_times), np.min(read_times), np.max(read_times)))

# Example usage: writeRepetitions=10, totalIterations=5, stringLength=10240
file_io_operations(writeRepetitions=10, totalIterations=5, stringLength=10240)
