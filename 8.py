orders = [
    "1,1000, completed, 2024-07-01",
    "2,500, pending, 2024-07-02",
    "1,300, completed, 2024-07-03",
    "3,50, cancelled, 2024-07-04",
    "2,150, completed, 2024-07-05",
    "1,75, pending, 2024-07-06",
    "4,200, completed, 2024-07-07",
    "5,120, shipped, 2024-07-08",
    "7,200, cancelled, 2024-07-07",
    "8,120, cancelled, 2024-07-08"
]

print(type(orders))

# Checking if the third item of the first order is 'completed'
print((orders[0].split(',')[2].strip()) == 'completed')

# Filtering orders with 'completed' status
completed_orders = list(filter(lambda x: x.split(',')[2].strip() == 'completed', orders))
print(completed_orders)
