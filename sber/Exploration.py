import matplotlib.pyplot as plt


class Exploration:
    """
    Class used for the first exploration in dataframe,
    get some information and visualise it
    """

    def __init__(self, events):
        self.events = events.copy()

    def plot_registered_after(self):
        """
        It should plot graph  of registred after column
        """

        self.events.registered_after.plot.hist(
            grid=True, bins=20, rwidth=0.9, color="#607c8e"
        )
        plt.title("Histogramm registred after")
        plt.xlabel("Time spent")
        plt.ylabel("Value counts")

        return plt.grid(axis="y", alpha=0.75)

    def plot_week_number(self):
        """
        It should plot graph  of week number column
        """

        self.events.week_number.plot.hist(
            grid=True, bins=20, rwidth=0.9, color="#607c8e"
        )
        plt.title("Histogramm week number")
        plt.xlabel("Number week")
        plt.ylabel("User count")

        return plt.grid(axis="y", alpha=0.75)

    def get_count_uniq_users(self, dict_) -> str:

        """
        dict of uniq users -> stats
        get some relationship between lenght of uniq users
        and all users
        """

        len_ = len(dict_)
        relationship = round((len_ / len(self.events)) * 100)

        print(
            f"Count of uniq users = {len_}",
            f"it's {relationship}% of dataset",
            sep="\n",
        )
