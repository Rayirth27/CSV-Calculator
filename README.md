# CSV Calculator

## Overview
A simple calculator that reads inputs from a CSV file and performs
arithmetic operations based on the operator defined in each row.

## CSV Format
The input file `calc.csv` must have the following column structure:

num1,operator,num2
5,+,6
10,-,3
4,*,7
20,/,4

## How It Works

- Imported the `csv` module
- Defined all required functions: `add()`, `sub()`, `mult()`, `div()`
- Opened `calc.csv` in read mode with `encoding="utf-8"`
- Used `csv.DictReader` to read rows as dictionaries
  with column names as keys (`num1`, `operator`, `num2`)
- Loaded all rows into a list using `list(reader1)` 
  to allow multiple loops over the same data
- Displayed raw CSV data before performing calculations
- For each row:
  - Stripped whitespace from all values using `.strip()`
  - Type cast `num1` and `num2` to `int`
  - `operator` kept as string — no casting needed
  - All inside a `try` block catching `ValueError`
    for non-numeric or invalid data
- Performed the correct operation based on `operator` value
- For division — handled `ZeroDivisionError` with a
  `try/except` block instead of crashing

## Error Handling

| Scenario | Handling |
|---|---|
| Non-numeric values | `ValueError` caught, row skipped |
| Division by zero | `ZeroDivisionError` caught, message printed |
| Unknown operator | `else` block prints a warning |
| Leading whitespace in CSV | `.strip()` applied to all values |

## Learnings
- `DictReader` parses structure but does not clean data
- `list(reader)` exhausts the reader — loop over the list after
- Always `.strip()` CSV values — real world data is always dirty
- Use `if/else` for predictable errors, `try/except` for unpredictable ones
