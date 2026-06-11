# import random, time, and sys
import random 
import time 
import sys

# increases recursion limit
sys.setrecursionlimit(10000)

# quick sort algorithm
def quick_sort(numbers):
    # check the length of list, if equal to 1 or 0 return 
    if len(numbers) <= 1:
        return numbers
    else:
        # create a list for left, right and middle and define pivot as middle of list
        pivot = numbers[len(numbers) // 2]
        left = [] 
        right = [] 
        middle = []
        # loop through numbers in the list
        for num in numbers:
            # if that number is greater than the pivot, add it to the right list
            if num > pivot:
                right.append(num)
            # if that number is less than the pivot, add it to the left list
            elif num < pivot:
                left.append(num)
            # if that number is equal to the pivot, add it to the middle list
            else:
                middle.append(num)
        # call quick_sort on the left and right lists
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        # combine all the list once sorted and return
        number_list = sorted_left + middle + sorted_right
        # return the sorted list
        return number_list

# insertion algorithm
def insertion_sort(numbers):
    # check the length of list, if equal to 1 or 0 return 
    if len(numbers) <= 1:
        return numbers 
    
    else:
        # recursive call on the list minus last element
        sorted_list = insertion_sort(numbers[:-1])
        last = numbers[-1]
        i = 0 
        while i < len(sorted_list) and sorted_list[i] < last:
            i += 1
        # insert last into position in list and return the list
        sorted_list.insert(i, last)
        # return the sorted list
        return sorted_list

# bubble algorithm   
def bubble_sort(numbers):
    # check the length of list, if equal to 1 or 0 return 
    if len(numbers) <= 1:
        return numbers
    
    else:
        # compare values next to each other, swap if not in order
        for i in range(len(numbers) -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        # recursivly sort the list but the last element, then add largest number to the end
        sorted_list = bubble_sort(numbers[:-1]) + [numbers[-1]]
        # return the sorted list
        return sorted_list


def main():
    # list with sizes needed and create the results display
    sizes = [10, 50, 100, 500, 1000, 5000]
    results = {
        'Size': [],
        'Quick': [],
        'Insertion':[],
        'Bubble': []}
    
    # loop through sizes
    for n in sizes:
        # create a random list for each sizes and copy it for each algorithm 
        test_list = [random.randint(1, n) for _ in range(n)]
        quick_list = test_list.copy()
        bubble_list = test_list.copy()
        insertion_list = test_list.copy()

        # get the current time, call quick_sort function, get the time again, find the duration
        start_time_q = time.perf_counter()
        _ = quick_sort(quick_list)
        end_time_q = time.perf_counter()
        quick_duration = end_time_q - start_time_q

        # get the current time, call insertion_sort function, get the time again, find the duration
        start_time_i = time.perf_counter()
        _ = insertion_sort(insertion_list)
        end_time_i = time.perf_counter()
        insertion_duration = end_time_i - start_time_i

        # get the current time, call bubble_sort function, get the time again, find the duration
        start_time_b = time.perf_counter()
        _ = bubble_sort(bubble_list)
        end_time_b = time.perf_counter()
        bubble_duration = end_time_b - start_time_b

        # append the duration and size to each section
        results['Size'].append(n)
        results['Quick'].append(quick_duration)
        results['Insertion'].append(insertion_duration)
        results['Bubble'].append(bubble_duration)

    print(f"{'Size':<10}{'Quick':<25}{'Insertion':<25}{'Bubble':<25}")
    print('------------------------------------------------------------------------')
    for i in range(len(sizes)):
        print(f"{results['Size'][i]:<10}{results['Quick'][i]:<25.6e}{results['Insertion'][i]:<25.6e}{results['Bubble'][i]:<25.6e}")
            

if __name__ == '__main__':
    main()
