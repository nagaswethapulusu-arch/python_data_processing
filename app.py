import pandas as pd
import streamlit as st

st.title("Python Data Processing")

employees = [
    {"id": 1, "name": "Asha", "department": "Engineering", "salary": 65000, "experience": 4},
    {"id": 2, "name": "Ravi", "department": "Marketing", "salary": 48000, "experience": 2},
    {"id": 3, "name": "Meena", "department": "HR", "salary": 42000, "experience": 3},
    {"id": 4, "name": "Kiran", "department": "Engineering", "salary": 95000, "experience": 9},
    {"id": 5, "name": "Swetha", "department": "Finance", "salary": 70000, "experience": 6},
    {"id": 6, "name": "Harsh", "department": "Engineering", "salary": 58000, "experience": 1},
    {"id": 7, "name": "Rupesh", "department": "Marketing", "salary": 55000, "experience": 5},
    {"id": 8, "name": "Akhil", "department": "Finance", "salary": 88000, "experience": 8},
    {"id": 9, "name": "Divya", "department": "HR", "salary": 46000, "experience": 2},
    {"id": 10, "name": "Teja", "department": "Marketing", "salary": 62000, "experience": 7},
]


def get_level(years):
    if years < 3:
        return "Junior"
    elif years <= 6:
        return "Mid"
    else:
        return "Senior"


def process_record(employee):
    processed = employee.copy()
    processed["level"] = get_level(employee["experience"])
    processed["bonus"] = employee["salary"] * 0.10
    return processed


def summary_statistics(records):
    salaries = [r["salary"] for r in records]
    highest = max(salaries)
    lowest = min(salaries)
    return {
        "count": len(records),
        "total": sum(salaries),
        "average": sum(salaries) / len(salaries),
        "highest": highest,
        "lowest": lowest,
        "top_earner": records[salaries.index(highest)]["name"],
        "lowest_earner": records[salaries.index(lowest)]["name"],
    }


def group_by_department(records):
    groups = {}
    for r in records:
        groups.setdefault(r["department"], []).append(r["salary"])
    return {
        department: {"count": len(salaries), "average": sum(salaries) / len(salaries)}
        for department, salaries in groups.items()
    }


processed = [process_record(e) for e in employees]

departments = sorted({r["department"] for r in processed})
selected = st.multiselect("Departments", departments, default=departments)
records = [r for r in processed if r["department"] in selected]

if len(records) == 0:
    st.warning("Select at least one department.")
else:
    stats = summary_statistics(records)

    st.header("Summary statistics")
    c1, c2 = st.columns(2)
    c1.metric("Total records", stats["count"])
    c2.metric("Total salary", f"Rs.{stats['total']:,}")
    c3, c4 = st.columns(2)
    c3.metric("Average salary", f"Rs.{stats['average']:,.2f}")
    c4.metric("Highest salary", f"Rs.{stats['highest']:,}", stats["top_earner"])
    st.metric("Lowest salary", f"Rs.{stats['lowest']:,}", stats["lowest_earner"])

    st.header("Processed records")
    st.table(pd.DataFrame(records))

    st.header("Department summary")
    dept_summary = group_by_department(records)
    dept_df = pd.DataFrame(
        [{"Department": d, "Employees": v["count"], "Average salary": round(v["average"], 2)}
         for d, v in dept_summary.items()]
    )
    st.table(dept_df)
    st.bar_chart(dept_df.set_index("Department")["Average salary"])
