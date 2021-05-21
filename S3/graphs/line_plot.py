import matplotlib.pyplot as plt

def plot(plots, labels, xlabel, ylabel, title):
    for index, metric in enumerate(plots):
        plt.plot(metric, label = labels[index])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(bbox_to_anchor=(1,1))
    plt.title(title)
    plt.show()
    
