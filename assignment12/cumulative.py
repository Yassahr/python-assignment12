import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


with sqlite3.connect("./db/lesson.db") as conn:
    cursor= conn.cursor()
    query='''SELECT o.order_id,
        SUM(l.quantity * p.price) as order_cost
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p ON p.product_id = l.product_id
        GROUP BY o.order_id
        '''
try:
    cursor.execute(query)
    results = cursor.fetchall()
    order_cost= pd.DataFrame(results, columns=['order number', "order cost"])
    order_cost['cumulative'] = order_cost['order cost'].cumsum()

    print(order_cost.head(5))

    order_cost.plot( x="order number" ,y="cumulative",kind="line", title="Cumulative based on Order Number")
    plt.show()


except Exception as e:
    conn.rollback()  
    print("Error:", e)

conn.close()