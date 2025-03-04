# visualize the data
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from pip._vendor.rich import align

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
graph("Sphorts Watch Data")
show = plt.show()

# histograms
dataset.hist()
plt.title("Sports Watch Data")
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.bar_label()
plt.show()