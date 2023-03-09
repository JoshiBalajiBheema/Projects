import matplotlib.pyplot as pyplot
import sys

labels = []
sizes = []


def labels_and_sizes():
    label_limit = 1
    size_limit = 1
    label_count = int(input("Enter the number of labels you want on the PieChart : "))
    while True:
        if label_limit <= label_count:
            label_input = input("Enter Labels names: ")
            labels.append(label_input)
            label_limit += 1
            size_input = input("Enter size : ")
            sizes.append(size_input)
            size_limit += 1
        else:
            break


def maxSize():
    int_list = list(map(int, sizes))
    if sum(int_list) > 100:
        print(f"Limit Exceeded! Range should not exceed 100, Your range was {sum(int_list)}")
        sys.exit()


def PieChart():
    print("PieChart is Generating..")
    pyplot.pie(sizes, labels=labels, autopct='%1.f%%', counterclock=False, startangle=90)
    pyplot.show()


if __name__ == "__main__":
    labels_and_sizes()
    maxSize()
    PieChart()
