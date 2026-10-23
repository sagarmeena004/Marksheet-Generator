# 📖 Marksheet Generator — Usage Guide

## 1. Introduction

Marksheet Generator is a Python-based command-line application that generates a formatted student marksheet.

This guide explains how to install, run, and use the application.

## 2. Prerequisites

Before running the project, ensure you have:

- Python 3 installed
- A terminal or command prompt
- A code editor (optional)

The project does not require external Python libraries.

## 3. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/sagarmeena004/Marksheet-Generator.git
```

Navigate to the project directory:

```bash
cd Marksheet-Generator
```

## 4. Run the Application

Execute:

```bash
python Marksheet_genreter.py
```

On some systems, you may need to use `python3` instead of `python`.

## 5. Enter Student Information

The application asks for:

1. Student Name
2. Enrollment Number
3. Roll Number
4. Semester
5. Section
6. Scholar Number

Example:

```text
Enter the name : Rahul Sharma
Enter the enrol : ENR2026001
Enter the roll No : 101
Enter the Semester : 1
Enter the section : A
Enter the scollor no : 2026001
```

## 6. Enter Subject Marks

The application collects theory marks for:

- Hindi
- English
- Physics
- Chemistry
- Biology

Example:

```text
Enter the Number Hindi : 75
Enter the Number English : 80
Enter the Number Physics: 55
Enter the Number Chemistry : 60
Enter the Number  Biology: 58
```

## 7. Enter Practical Marks

The application also collects practical marks for:

- Physics
- Chemistry
- Biology

Example:

```text
Enter the Number phy_p: 25
Enter the Number che_p: 26
Enter the Number Bio_p: 27
```

## 8. Marksheet Generation

After entering the required information, the application automatically displays a formatted marksheet.

The output includes:

- Student details
- Subject names
- Theory marks
- Practical marks
- Combined subject marks
- Subject-wise PASS/FAIL status

## 9. Passing Conditions

The current implementation uses the following conditions:

| Subject | PASS Condition |
|---|---|
| Hindi | Marks > 28 |
| English | Marks > 28 |
| Physics | Theory + Practical > 33 |
| Chemistry | Theory + Practical > 33 |
| Biology | Theory + Practical > 33 |

## 10. Important Notes

- Enter whole numbers for subject marks.
- Enter valid numeric values to avoid conversion errors.
- The current program does not validate maximum marks.
- The application does not save marksheets to files.
- Results are displayed directly in the terminal.

## 11. Troubleshooting

### Python is not recognized

Verify your Python installation:

```bash
python --version
```

### File not found

Ensure you are inside the correct project directory.

### Invalid input error

Enter integer values when the application requests marks.

## 12. Conclusion

This guide provides the steps required to run and use the Python Marksheet Generator.

The project is suitable for beginners learning Python input handling, conditional logic, and console formatting.

---

**Happy Coding! 🐍**