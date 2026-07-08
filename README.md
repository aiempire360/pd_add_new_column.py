# 📊 Adding a New Column and Exporting Data with Pandas

This project demonstrates how to create a new column in a Pandas DataFrame by performing a simple calculation and then save the updated data to a new CSV file.

In this example, a **Tax** column is added by calculating **20% of the Revenue** for each record.

---

## 📌 What You'll Learn

- Read a CSV file using Pandas
- Load a specific number of rows
- Create a new column using existing data
- Perform calculations on DataFrame columns
- Export the updated DataFrame to a new CSV file

---

## 📂 Project Structure

```
Project/
│── ecommerce_sales_data.csv
│── data_with_tax1.csv
│── Pandas.py
│── README.md
```

---

## 🐍 Python Code

```python
import pandas as pd

# Read the first 10 rows from the CSV file
df = pd.read_csv('ecommerce_sales_data.csv', nrows=10)

# Create a new Tax column (20% of Revenue)
df["Tax"] = df["Revenue"] * 0.20

# Save the updated DataFrame to a new CSV file
df.to_csv('data_with_tax1.csv', index=False)

# Display the DataFrame
print(df)
```

---

## 📖 Code Explanation

- **`pd.read_csv()`** reads the CSV file into a DataFrame.
- **`nrows=10`** loads only the first 10 records.
- **`df["Tax"]`** creates a new column named **Tax**.
- **`df["Revenue"] * 0.20`** calculates 20% tax for every row.
- **`to_csv()`** exports the updated DataFrame to a new CSV file.
- **`index=False`** prevents the row index from being saved in the output file.

---

## 📄 Output

The script creates a new CSV file named:

```
data_with_tax1.csv
```

Example:

| Category | Revenue | Tax |
|----------|---------:|----:|
| Electronics | 5000 | 1000 |
| Fashion | 3200 | 640 |
| Home Decor | 4500 | 900 |

---

## 💻 Requirements

- Python 3.x
- Pandas

Install Pandas:

```bash
pip install pandas
```

---

## ▶️ Run the Project

```bash
python Pandas.py
```

---

## 🎯 Learning Outcome

After completing this project, you'll be able to:

- Read data from a CSV file
- Create new columns using existing data
- Perform arithmetic operations on DataFrame columns
- Save modified data to a new CSV file
- Work with DataFrames efficiently using Pandas

---

### ⭐ If you found this project helpful, consider giving it a star on GitHub!
