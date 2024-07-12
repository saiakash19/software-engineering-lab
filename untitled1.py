# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jJ4_RZa8f8Lupbj3T37_oipLFkG2uNzS
"""

import matplotlib.pyplot as plt
import numpy as np

def quadratic_models(time,a,b,c):
    temp = a* (time ** 2) + b * time + c
    return temp

def main() :

    time_values = np.linspace(0,10,50)

    with open('/content/sel.txt', 'r') as file:
            lines = file.readlines()
    # Skip the first line if it's a header
    if lines[0].strip().startswith('VALUES'):
        lines = lines[1:]
    for i, line in enumerate(lines):
        try: # Handle potential errors during conversion
            a, b, c = map(float, line.split())
            temperature_file_multiple = quadratic_models(time_values, a, b, c)
            plt.plot(time_values, temperature_file_multiple, label=f'File Input Set {i+1} Coefficients')
        except ValueError as e:
            print(f"Skipping line {i+1} due to error: {e}") # Inform the user about skipped lines
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multi Set from File')
    plt.show()

main()