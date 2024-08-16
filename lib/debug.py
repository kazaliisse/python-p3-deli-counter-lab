#!/usr/bin/env python3
# debug.py

from lib.deli_counter import line, take_a_number, now_serving

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

    # Initialize an empty deli line
    katz_deli = []

    # Add customers to the deli line
    take_a_number(katz_deli, "Ada")     # Expected: Welcome, Ada. You are number 1 in line.
    take_a_number(katz_deli, "Grace")   # Expected: Welcome, Grace. You are number 2 in line.
    take_a_number(katz_deli, "Kent")    # Expected: Welcome, Kent. You are number 3 in line.

    # Show the current line
    line(katz_deli)                     # Expected: The line is currently: 1. Ada 2. Grace 3. Kent

    # Serve the next customer
    now_serving(katz_deli)              # Expected: Currently serving Ada.

    # Show the updated line
    line(katz_deli)                     # Expected: The line is currently: 1. Grace 2. Kent

    # Add another customer
    take_a_number(katz_deli, "Matz")    # Expected: Welcome, Matz. You are number 3 in line.

    # Show the updated line
    line(katz_deli)                     # Expected: The line is currently: 1. Grace 2. Kent 3. Matz

    # Serve the next customer
    now_serving(katz_deli)              # Expected: Currently serving Grace.

    # Show the final line
    line(katz_deli)                     # Expected: The line is currently: 1. Kent 2. Matz

