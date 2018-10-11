
from matplotlib import pyplot

# 1 . prepare data

machine_counts = [15, 4, 2 ]

# 2. prepare labels
machine_names = ["PC", "LINUX", "MAC"]

# 3.Draw pie

pyplot.pie( machine_counts, labels = machine_names, autopct="%.1f%%",shadow= True,explode= [0,0.1,0])
pyplot.title("PC LINUX MAC")
pyplot.axis("equal")
# 4. show
pyplot.show()




