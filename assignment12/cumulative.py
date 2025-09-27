import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.data as pldata


# Task 2: A Line Plot with Pandas
with sqlite3.connect("../db/lesson.db") as conn:
    
    sql_statment = """
        SELECT o.order_id, SUM(price * quantity) 
        AS total_price FROM orders o 
        JOIN line_items l 
        ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY o.order_id;
        """
    
    order_cost = pd.read_sql_query(sql_statment, conn)
    print(order_cost)

    # Adds "cumulative" column to df
    def cumulative(row):
        totals_above = order_cost['total_price'][0:row.name+1]
        return totals_above.sum()
    
    order_cost['cumulative'] = order_cost.apply(cumulative, axis=1)

    # Use Pandas plotting to create a line plot of cumulative revenue vs. order_id
    order_cost.plot(x="order_id", y="cumulative", kind="line", color="purple", title="Cumulative Order Revenue")
    plt.show()
