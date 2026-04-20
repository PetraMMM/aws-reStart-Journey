# My Python Programming Journey: From Basics to Bioinformatics

This repository contains a collection of Python projects and labs I completed to build my programming foundation. I developed all of these scripts using **AWS Cloud9**, using its cloud-based IDE and integrated terminal to write, test, and debug my code.

---

## Core Fundamentals
In these initial labs, I focused on the essential building blocks of Python:
* **I worked with Numeric Data Types:** I explored `int`, `float`, `complex`, and `bool` types within the Python shell to understand how the language handles mathematical data.
* **I manipulated Strings:** I practiced concatenating strings, taking user input, and formatting output to create interactive scripts.
* **I categorized Values:** I created programs that mixed different data types in a list and used `for` loops and `print()` functions to iterate through and identify them.

## Data Collections & Composite Types
I learned how to organize data efficiently using Python's collection structures:
* **I implemented Collections:** I used `Lists`, `Tuples`, and `Dictionaries` to store and manage related data points.
* **I created Composite Data Types:** I built complex data structures, where I nested a dictionary inside a list to manage multi-layered information.

## Control Flow & Logic
I developed scripts that can make decisions and repeat tasks:
* **I used Conditionals:** I implemented `if`, `elif`, and `else` statements to create different execution paths based on specific conditions.
* **I used Loops:** I utilized both `while` loops for conditional repetition and `for` loops for iterating over data sequences.

## Case Study: Human Insulin Analysis
One of the highlights of my learning was applying Python to biological data.
* **I processed Insulin Sequences:** I retrieved the protein sequence of human insulin from preproinsulin and I used string manipulation to clean the data.
* **I calculated Molecular Weight:** I assigned variables to represent the weight of insulin and performed math operations to find the total molecular weight.
* **I calculated Net Charge:** I created a dictionary of pKa values and used a `while` loop to calculate the net charge of insulin across a pH scale of 0 to 14.

## Cryptography & System Admin
I explored how Python interacts with the system and handles security:
* **I built a Caesar Cipher:** I wrote user-defined functions to implement a Caesar cipher, allowing me to encrypt and decrypt messages by shifting alphabet positions.
* **I performed System Administration:** I used the `os` and `subprocess` modules to run Linux Bash commands directly from my Python scripts.
* **I handled JSON Files:** I used the `json` module to open and parse external data files to retrieve specific insulin information.

## Debugging & Testing
I prioritized code reliability by learning how to troubleshoot effectively:
* **I used the Python Debugger (pdb):** I used `pdb` to step through my scripts line-by-line, allowing me to inspect variables and track the flow of execution.
* **I debugged the Caesar Cipher:** I specifically used the debugger to find and fix logic flaws in my encryption program to ensure it functioned perfectly.

---

## How to Run my Projects
1.  **Clone this repo:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Navigate to a lab folder:**
    ```bash
    cd lab-directory-name
    ```
3.  **Run the script:**
    ```bash
    python3 script_name.py
    ```

## Skills & Tools
* **Languages:** Python 3, Bash
* **IDE:** AWS Cloud9
* **Libraries:** `json`, `os`, `subprocess`, `pdb`
