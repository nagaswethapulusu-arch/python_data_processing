# Python Data Processing

A beginner-friendly Python project that processes a collection of **structured employee records** and generates a **summary of useful statistics**. It combines lists, dictionaries, loops, conditions, and functions.

## Objective

Combine Python concepts to perform basic data processing.

## Tools Used

- Python 3
- Jupyter Notebook
- Streamlit (for the live demo)

## Dataset

Manually created records of 10 employees. Each record is a dictionary with `id`, `name`, `department`, `salary` (in rupees), and `experience` (in years).

| ID | Name | Department | Salary | Experience |
|----|------|------------|--------|------------|
| 1 | Asha | Engineering | 65,000 | 4 |
| 2 | Ravi | Marketing | 48,000 | 2 |
| 3 | Meena | HR | 42,000 | 3 |
| 4 | Kiran | Engineering | 95,000 | 9 |
| 5 | Swetha | Finance | 70,000 | 6 |
| 6 | Harsh | Engineering | 58,000 | 1 |
| 7 | Rupesh | Marketing | 55,000 | 5 |
| 8 | Akhil | Finance | 88,000 | 8 |
| 9 | Divya | HR | 46,000 | 2 |
| 10 | Teja | Marketing | 62,000 | 7 |

## Functions

| Function | What it does |
|----------|--------------|
| `get_level(years)` | Returns Junior (under 3 years), Mid (3 to 6 years), or Senior (over 6 years) |
| `process_record(employee)` | Copies one record and adds a `level` and a `bonus` (10% of salary) |
| `process_all(records)` | Applies `process_record` to every record |
| `summary_statistics(records)` | Calculates count, total, average, highest, and lowest salary and who earns them |
| `group_by_department(records)` | Calculates the number of employees and the average salary for each department |

## Approach

1. **Store the records** as a list of dictionaries.
2. **Process each record** by adding new fields (`level` and `bonus`). A copy is made so the original data is not changed.
3. **Calculate summary statistics** with `sum()`, `len()`, `max()`, and `min()`.
4. **Group by department** using a dictionary where the key is the department and the value is the list of salaries.
5. **Count the levels** (Junior, Mid, Senior) with a dictionary.
6. **Reuse functions** so each operation is written once and tested separately.

## What is Data Processing?

Data processing means turning raw data into useful information: cleaning it, adding calculated fields, grouping it, and summarizing it with statistics.

## How to Run

1. Install Python and Jupyter Notebook:
   ```
   pip install notebook
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `python_data_processing.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
--- Processed records (first 5) ---
Name    Dept         Salary  Exp  Level   Bonus
Asha    Engineering  65000   4    Mid     6,500
Ravi    Marketing    48000   2    Junior  4,800
Meena   HR           42000   3    Mid     4,200
Kiran   Engineering  95000   9    Senior  9,500
Swetha  Finance      70000   6    Mid     7,000

--- Summary statistics ---
Total records: 10
Total salary: Rs.629,000
Average salary: Rs.62,900.00
Highest salary: Rs.95,000 (Kiran)
Lowest salary: Rs.42,000 (Meena)

--- Department summary ---
Engineering  3 employees, average Rs.72,666.67
Marketing    3 employees, average Rs.55,000.00
HR           2 employees, average Rs.44,000.00
Finance      2 employees, average Rs.79,000.00

--- Level count ---
Mid: 4
Junior: 3
Senior: 3
```

## Limitations

- Records are typed in manually and stored only in memory.
- If two employees share the highest or lowest salary, only the first one is reported.
- An empty list of records would cause an error in `summary_statistics`.

## Possible Improvements

- Read the records from a CSV file.
- Use Pandas with `groupby()` for the department summary.
- Add median and standard deviation.

## Author

SwethaPulusu
