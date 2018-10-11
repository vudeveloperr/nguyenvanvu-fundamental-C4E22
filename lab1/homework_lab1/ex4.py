from matplotlib import pyplot

# 1 . prepare data

machine_counts = [30, 13, 7 ]

# 2. prepare labels
machine_names = ["events", "advertisements", "word of mouth"]

# 3.Draw pie

pyplot.pie( machine_counts, labels = machine_names, autopct="%.1f%%",shadow= True,explode= [0,0.1,0])
pyplot.title("the number of customers group by references")
pyplot.axis("equal")
# 4. show
pyplot.show()