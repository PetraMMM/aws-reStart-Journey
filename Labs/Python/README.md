# Python Programming Labs: From Basics to Bioinformatics

This repository contains a comprehensive series of Python scripts developed during the "Introduction to Programming" labs. The projects progress from fundamental data types to complex real-world applications, including bioinformatics analysis, cryptography, and system administration.

## Table of Contents
1. [Core Fundamentals](#-core-fundamentals)
2. [Data Collections & Composite Types](#-data-collections--composite-types)
3. [Control Flow & Logic](#-control-flow--logic)
4. [Case Study: Human Insulin Analysis](#-case-study-human-insulin-analysis)
5. [Cryptography: Caesar Cipher](#-cryptography-caesar-cipher)
6. [System Administration & Modules](#-system-administration--modules)
7. [Debugging & Optimization](#-debugging--optimization)

---

## Core Fundamentals
Exploring the building blocks of Python syntax and data handling.
* **Numeric Data Types:** Working with `int`, `float`, `complex`, and `bool`.
* **String Manipulation:** Practiced concatenation, user input retrieval, and output formatting.
* **Math Operations:** Utilizing Python's ability to process large datasets and perform arithmetic.

## Data Collections & Composite Types
Managing data efficiently using Python’s built-in collection types.
* **Collections:** Implementation of `Lists`, `Tuples`, and `Dictionaries`.
* **Categorizing Values:** Using `for` loops to iterate through and identify types within mixed-data lists.
* **Composite Data Types:** Creating nested structures (e.g., a dictionary inside a list) to manage complex data (the "Turducken" approach).

## Control Flow & Logic
Building dynamic programs that respond to data and user input.
* **Conditionals:** Using `if`, `elif`, and `else` statements for decision-making.
* **Loops:** Implementing `while` loops for conditional repetition and `for` loops for sequence iteration.

## Case Study: Human Insulin Analysis
Applying Python to scientific computing and bioinformatics.
* **Sequence Extraction:** Retrieving protein sequences from raw preproinsulin data.
* **Molecular Weight:** Calculating weights using numeric types and string manipulation.
* **Net Charge Calculation:** Using pKa values, amino acid counts, and loops to calculate the net charge of insulin from pH 0 to pH 14.

## Cryptography: Caesar Cipher
Practicing modular programming and user-defined functions.
* **Functions:** Created reusable logic for encryption and decryption.
* **Logic:** Implemented a shift-based cipher to protect messages by moving characters along the alphabet.

## System Administration & Modules
Interacting with the operating system and external files.
* **File Handling & JSON:** Using the `json` module to load and parse insulin data from external files.
* **System Commands:** Utilizing `os.system()` and `subprocess.run()` to execute Bash commands directly from Python scripts.
* **Modular Programming:** Organizing code into modules for better scalability.

## Debugging & Optimization
Ensuring code reliability and fixing logic errors.
* **Python Debugger (pdb):** Stepping through code to inspect variables and program flow.
* **Caesar Cipher Debugging:** Identifying and fixing flaws in logic within the encryption functions using the interactive debugger.

---

## How to Use
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Navigate to a lab:**
    ```bash
    cd lab-folder-name
    ```
3.  **Run the script:**
    ```bash
    python3 script_name.py
    ```

## 💻 Requirements
* Python 3.x
* Bash (for System Administration labs)
* Standard Library Modules: `os`, `subprocess`, `json`, `pdb`
