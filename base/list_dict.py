# -*- coding: utf-8 -*-
import sys
import os
import time
import struct
import json
from io import StringIO


def normal():
    """Demonstrate basic list operations"""
    list_t = []
    
    # Add even numbers
    for i in range(10):
        if i % 2 == 0:
            list_t.append(i)
    print("Even numbers list:", list_t)
    
    # Add odd numbers
    for i in range(10):
        if i % 2 == 1:
            list_t.append(i)
    print("Complete list:", list_t)
    
    # Sort
    list_t.sort()
    print("After sorting:", list_t)


def with_multi():
    """Demonstrate tuple list sorting"""
    list_t = []
    
    # Add even tuples
    for i in range(10):
        if i % 2 == 0:
            list_t.append((f"AA{i:02d}", i))
    print("Even tuples:", list_t)
    print('*' * 50)
    
    # Add odd tuples
    for i in range(10):
        if i % 2 == 1:
            list_t.append((f"BB{i:02d}", i))
    print("Complete tuple list:", list_t)
    print('*' * 50)
    
    # Sort by number (descending)
    list_t.sort(key=lambda x: x[1], reverse=True)
    print("Sorted by number (descending):", list_t)


def with_dict():
    """Demonstrate dictionary list sorting"""
    list_t = []
    
    # Add even dictionaries
    for i in range(10):
        if i % 2 == 0:
            dict_t = {
                "string": f"AA{i:02d}",
                "num": i
            }
            list_t.append(dict_t)
    print("Even dictionaries:", list_t)
    print('*' * 50)
    
    # Add odd dictionaries
    for i in range(10):
        if i % 2 == 1:
            dict_t = {
                "string": f"BB{i:02d}",
                "num": i
            }
            list_t.append(dict_t)
    print("Complete dictionary list:", list_t)
    
    print('Sort by string (descending)' + '*' * 50)
    list_t.sort(key=lambda x: x['string'], reverse=True)
    print(list_t)
    
    print('Sort by number (descending)' + '*' * 50)
    list_t.sort(key=lambda x: x['num'], reverse=True)
    print(list_t)
    
    print('JSON format output' + '*' * 50)
    print(json.dumps(list_t, indent=2, ensure_ascii=False))


def demo_list_comprehension():
    """Demonstrate list comprehensions"""
    print("List comprehension examples:")
    
    # Generate even numbers list
    even_numbers = [i for i in range(10) if i % 2 == 0]
    print("Even numbers list:", even_numbers)
    
    # Generate odd numbers list
    odd_numbers = [i for i in range(10) if i % 2 == 1]
    print("Odd numbers list:", odd_numbers)
    
    # Generate dictionary list
    dict_list = [{"string": f"Item{i:02d}", "num": i} for i in range(5)]
    print("Dictionary list:", dict_list)


def demo_dict_operations():
    """Demonstrate dictionary operations"""
    print("Dictionary operation examples:")
    
    # Create dictionary
    sample_dict = {"name": "John", "age": 25, "city": "New York"}
    print("Original dictionary:", sample_dict)
    
    # Add key-value pair
    sample_dict["job"] = "Engineer"
    print("After adding key-value pair:", sample_dict)
    
    # Update dictionary
    sample_dict.update({"age": 26, "hobby": "Programming"})
    print("After update:", sample_dict)
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}
    print("Squares dictionary:", squares)


def start_service():
    """Main function"""
    print("=" * 60)
    print("Python List and Dictionary Operations Demo")
    print("=" * 60)
    
    print("\n1. Basic list operations:")
    normal()
    
    print("\n2. Tuple list sorting:")
    with_multi()
    
    print("\n3. Dictionary list sorting:")
    with_dict()
    
    print("\n4. List comprehensions:")
    demo_list_comprehension()
    
    print("\n5. Dictionary operations:")
    demo_dict_operations()


if __name__ == "__main__":
    # Set console title (only effective on Windows)
    if os.name == 'nt':  # Windows system
        title = os.path.basename(sys.argv[0])
        os.system(f'title {title}')
    
    start_service()
       