import matplotlib.pyplot as plt  

class Exploration:
    def __init__(self, events):
        self.events = events.copy()

    def plot_registered_after(self):

        self.events.registered_after.plot.hist(
            grid=True, bins=20, rwidth=0.9, color="#607c8e"
        )
        plt.title("Histogramm registred after")
        plt.xlabel("Time spent")
        plt.ylabel("Value counts")

        return plt.grid(axis="y", alpha=0.75)

    def plot_week_number(self):

        self.events.week_number.plot.hist(
            grid=True, bins=20, rwidth=0.9, color="#607c8e"
        )
        plt.title("Histogramm week number")
        plt.xlabel("Number week")
        plt.ylabel("User count")

        return plt.grid(axis="y", alpha=0.75)
