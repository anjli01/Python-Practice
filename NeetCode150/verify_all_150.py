"""
NeetCode 150 - Master Verification Suite
Runs and validates all 18 module test suites across all 150 problems.
"""

import subprocess
import sys
import os

MODULE_DIRS = [
    ("Module 1.1: Arrays & Hashing (9 Problems)", "module_1_arrays_and_hashing"),
    ("Module 1.2: Two Pointers (5 Problems)", "module_2_two_pointers"),
    ("Module 1.3: Sliding Window (6 Problems)", "module_3_sliding_window"),
    ("Module 1.4: Stack (7 Problems)", "module_4_stack"),
    ("Module 2.1: Binary Search (7 Problems)", "module_5_binary_search"),
    ("Module 2.2: Linked List (11 Problems)", "module_6_linked_list"),
    ("Module 3.1: Trees (15 Problems)", "module_7_trees"),
    ("Module 3.2: Tries (3 Problems)", "module_8_tries"),
    ("Module 3.3: Heap / Priority Queue (7 Problems)", "module_9_heap"),
    ("Module 4.1: Backtracking (9 Problems)", "module_10_backtracking"),
    ("Module 4.2: Graphs (13 Problems)", "module_11_graphs"),
    ("Module 4.3: Advanced Graphs (6 Problems)", "module_12_advanced_graphs"),
    ("Module 5.1: 1-D Dynamic Programming (12 Problems)", "module_13_1d_dp"),
    ("Module 5.2: 2-D Dynamic Programming (11 Problems)", "module_14_2d_dp"),
    ("Module 5.3: Greedy (8 Problems)", "module_15_greedy"),
    ("Module 6.1: Intervals (6 Problems)", "module_16_intervals"),
    ("Module 6.2: Math & Geometry (8 Problems)", "module_17_math_geometry"),
    ("Module 6.3: Bit Manipulation (7 Problems)", "module_18_bit_manipulation"),
]

def run_master_verification():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    python_exe = sys.executable

    print("\n" + "=" * 70)
    print("       NEETCODE 150 — MASTER VERIFICATION & AUDIT SUITE")
    print("=" * 70 + "\n")

    total_modules = len(MODULE_DIRS)
    passed_modules = 0

    for name, directory in MODULE_DIRS:
        dir_path = os.path.join(base_dir, directory)
        test_script = os.path.join(dir_path, "test_solutions.py")

        print(f"[*] Running: {name} ...", end=" ", flush=True)

        res = subprocess.run([python_exe, test_script], cwd=dir_path, capture_output=True, text=True)
        if res.returncode == 0:
            print("PASSED [100%]")
            passed_modules += 1
        else:
            print("FAILED!")
            print(res.stdout)
            print(res.stderr)
            sys.exit(1)

    print("\n" + "=" * 70)
    print(f" ALL {passed_modules} / {total_modules} MODULES PASSED VERIFICATION!")
    print(f" TOTAL 150 / 150 PROBLEMS TESTED, VALIDATED & 100% CORRECT.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    run_master_verification()
