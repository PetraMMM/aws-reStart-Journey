# Python Programming Labs: From Basics to Bioinformatics

This repository contains a comprehensive series of Python scripts developed during the "Introduction to Programming" labs. The projects progress from fundamental data types to complex real-world applications, including bioinformatics analysis, cryptography, and system administration.

## Development Environment
All labs in this repository were developed and tested using **AWS Cloud9**. 
* **IDE:** Cloud-based integrated development environment (IDE) for writing, running, and debugging code.
* **Terminal:** Used the built-in browser-based shell for executing scripts and managing files.
* **Collaboration:** Utilized Cloud9's features for seamless code editing and execution within the AWS ecosystem.

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
* **System Commands:** Utilizing `os.system()` and `subprocess.run()` to execute Bash commands directly from Python scripts within the Cloud9 terminal.
* **Modular Programming:** Organizing code into modules for better scalability.

## Debugging & Optimization
Ensuring code reliability and fixing logic errors.
* **Python Debugger (pdb):** Stepping through code to inspect variables and program flow.
* **Caesar Cipher Debugging:** Identifying and fixing flaws in logic within the encryption functions using the interactive debugger.

---

## How to Use
1.  **Environment Setup:** These scripts are optimized for **AWS Cloud9**. You can run them in any Python 3 environment, but ensure you have terminal access for the System Administration labs.
2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
3.  **Run a script:**
    ```bash
    python3 script_name.py
    ```

## 💻 Requirements
* Python 3.x
* AWS Cloud9 (preferred) or any Linux-based environment
* Standard Library Modules: `os`, `subprocess`, `json`, `pdb`
