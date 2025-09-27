import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Task 1: Plotting with Pandas
with sqlite3.connect("../db/lesson.db") as conn:
    
    sql_statment = """
        SELECT last_name, SUM(price * quantity) 
        AS revenue FROM employees e 
        JOIN orders o 
        ON e.employee_id = o.employee_id JOIN line_items l 
        ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY e.employee_id;
        """
    
    employee_results = pd.read_sql_query(sql_statment, conn)
    print(employee_results)

    # Use the Pandas plotting functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue.
    employee_results.plot(x="last_name", y="revenue", kind="bar", color="teal", title="Employee Sales Revenue")
    plt.show()
