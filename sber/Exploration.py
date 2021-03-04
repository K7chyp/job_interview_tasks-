import matplotlib.pyplot as plt


class Exploration:
    def __init__(self, events):
        self.events = events.copy()

    def plot_something(self, 
                       title_, 
                       xlabel_, 
                       ylabel_, 
                       series, 
                       color="#607c8e"):
        """
        Common funcion for plot histogramm
        """

        series.plot.hist(grid=True, 
                         bins=20,
                         rwidth=0.9, 
                         color=color)
        plt.title(title_)
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)

        return plt.grid(axis="y", alpha=0.75)

    def plot_registered_after(self):

        return self.plot_something(
            title_="Histogramm registred after",
            xlabel_="Time spent",
            ylabel_="Value counts",
            series=self.events.registered_after,
        )

    def plot_week_number(self):

        return self.plot_something(
            title_="Histogramm week number",
            xlabel_="Number week",
            ylabel_="User count",
            series=self.events.week_number,
        )

    def plot_visits_number(self):

        return self.plot_something(
            title_="Histogramm visits number",
            xlabel_="Number visits",
            ylabel_="User count",
            series=self.events.visits_number,
        )
