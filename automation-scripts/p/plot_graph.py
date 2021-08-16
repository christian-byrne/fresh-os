

import matplotlib.pyplot as plt
import math
def womens_beauty_standards(time):
    standards = math.log(abs(time))
    return standards*-1 if time < 0 else standards


def plot_values(domain):
    xaxis = []
    yaxis = []
    for x in range(-1*domain, domain):
        if x != 0:
            xaxis.append(x)
            yaxis.append(womens_beauty_standards(x))

    return xaxis, yaxis


def decorate_graph(plt, title, x_label="x - axis", y_label="y - axis"):
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)


def main():
    xaxis, yaxis = plot_values(100)
    plt.plot(xaxis, yaxis)
    decorate_graph(
        plt,
        "Women's Beauty Standards over Time",
        x_label="Time (years)",
        y_label="Standards (relative)"
    )
    plt.show()


if __name__ == "__main__":
    main()

