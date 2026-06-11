# Sorting Algorithms Performance Analysis

## Overview
This project compares the performance of three sorting algorithms: Quick Sort, Insertion Sort, and Bubble Sort. The goal is to analyze how execution time changes as input size increases and to compare algorithm efficiency using empirical runtime measurements.

---

## Algorithms

### Quick Sort
A divide-and-conquer algorithm with average time complexity of O(n log n).

### Insertion Sort
A simple comparison-based sorting algorithm with time complexity of O(n^2).

### Bubble Sort
A basic sorting algorithm with time complexity of O(n^2).

---

## Methodology
- Random datasets were generated in Python.
- Each algorithm was tested on identical input sizes.
- Execution time was measured using Python’s `time.perf_counter()`.
- Results were recorded and passed to R for visualization.

---


## Visualization
Results were visualized in R using:
- Standard scale comparison plot
- Zoomed-in comparison plot
- Log-scale plot to better show growth differences

---

## Tools Used
- Python (algorithm implementation)
- R (data visualization)
- VS Code

---

## Results
Quick Sort performed the fastest across all input sizes. Insertion Sort showed moderate performance for small datasets but degraded as size increased. Bubble Sort performed the slowest and scaled poorly with larger inputs.
