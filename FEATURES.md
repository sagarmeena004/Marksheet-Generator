# 🎓 Marksheet Generator — Features

## Project Overview

Marksheet Generator is a Python-based console application designed to generate student academic marksheets.

The application accepts student details, subject marks, and practical marks to display a structured result report.

## 1. Student Information

The program collects the following information:

- Student Name
- Enrollment Number
- Roll Number
- Semester
- Section
- Scholar Number

These details are displayed in the generated marksheet.

## 2. Subject Marks Entry

The application supports five academic subjects:

| Subject | Theory Marks | Practical Marks |
|---|---|---|
| Hindi | Supported | Not Applicable |
| English | Supported | Not Applicable |
| Physics | Supported | Supported |
| Chemistry | Supported | Supported |
| Biology | Supported | Supported |

## 3. Automatic Marks Calculation

For subjects containing practical examinations, the program calculates combined marks.

**Physics Total**

`Physics Theory + Physics Practical`

**Chemistry Total**

`Chemistry Theory + Chemistry Practical`

**Biology Total**

`Biology Theory + Biology Practical`

Hindi and English use their entered theory marks as the subject total.

## 4. Automatic PASS/FAIL Evaluation

The program evaluates subject-wise results using Python conditional statements.

| Subject | PASS Condition |
|---|---|
| Hindi | Marks > 28 |
| English | Marks > 28 |
| Physics | Total Marks > 33 |
| Chemistry | Total Marks > 33 |
| Biology | Total Marks > 33 |

## 5. Formatted Marksheet

The program displays a marksheet containing:

- University heading
- Examination information
- Student details
- Subject names
- Maximum theory marks
- Maximum practical marks
- Obtained theory marks
- Obtained practical marks
- Subject totals
- Subject-wise PASS/FAIL status

## 6. Command-Line Interface

The application runs directly in a terminal.

Users enter student information and marks through interactive prompts.

No graphical interface is required.

## 7. Python Concepts Demonstrated

- Variables
- User input
- Integer conversion
- Conditional statements
- Comparison operators
- Arithmetic operations
- Formatted console output

## 8. Current Limitations

The current version does not include:

- Overall percentage calculation
- Overall PASS/FAIL result
- PDF marksheet export
- Database storage
- Graphical user interface
- Input validation

## 9. Future Improvements

Potential future features include:

- Percentage calculation
- Overall result generation
- Grade calculation
- PDF export
- Student database integration
- Graphical interface

These features are suggestions for future development and are not implemented in the current version.

---

**Developed Using Python 🐍**