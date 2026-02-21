import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


with sqlite3.connect("./db/lesson.db") as conn:
    cursor= conn.cursor()
    query='''SELECT last_name, 
        SUM(price * quantity) AS revenue 
        FROM employees e 
        JOIN orders o ON e.employee_id = o.employee_id 
        JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id
        GROUP BY e.employee_id;
        '''
try:
    cursor.execute(query)
    results = cursor.fetchall()
    employee_results= pd.DataFrame(results, columns=['Last Name', "Revenue"])
    print(employee_results)
    employee_results.plot( x="Last Name" ,y="Revenue",kind="bar", title="Revenues based on Employee")
    plt.show()


except Exception as e:
    conn.rollback() 
    print("Error:", e)

conn.close()

