# 🧐 File Integrity Checker

 A Python tool to **verify the integrity of files** using cryptographic hashing.
 The program computes the hash of two files & checks whether they have been modified.

## 🚀 Features

 - Compute cryptographic hash of any file.
 - Support different algorithms (default: SHA-256)
 - Verify if two files are identical or modified.
 - Handles large files efficiently by reading in chunks (64 KB)
 - Gracefull exception handling for missing files or errors.

## 📂 Project Structure

 ```perl
 📁 Checking-File-Integrity
 ├── main.py
 └── README.md
 ```

## 📦 Requirements

 - Python 3.8+
 - Uses Python built-in libraries:
    [`hashlib`]
    [`pathlib`]

## 1️⃣ Clone the Repository

 ```bash
 git clone 
 ```

## 2️⃣ Navigate to the Project Directory

 ```bash
 cd File-Integrity_Checker
 ```

## ▶️ Usage

 **01.** Run the program:

 ```bash
 python main.py
 ```

 **02.** Enter the paths of the two files you want to compare:

 ```css
 Enter the File Path 1: file1.txt
 Enter the File Path 2: file2.txt
 ```

 **03.** The program will output whether the files are identical or have been modified.

 ```css
 No Modifications Have been Made.
 ```

 **or**

 ```css
 File Has been Modified.
 ```

## ⚙️ Supported Algorithms

 - SHA-256 (default)
 - SHA-1
 - MD5
 - Any other algorithm supported by Python's [`hashlib.new()`]


## ⚠️ Security Notes

 - SHA-256 is recommended for cryptographic integrity checks.
 - This tool is usedul for **detecting modifications, corruption, or tampering** of files.

## ⭐ Contributing

 Contributions are welcome! please fork the repository & create a pull request for any improvements or bug fixes.

## 📜 License

 This project is open-source under the **MIT License.**