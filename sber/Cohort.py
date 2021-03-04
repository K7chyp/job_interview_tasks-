class Cohort:
    """
    As it was in task, we should create division on cohort groups
    """

    def __init__(self, events=events):
        self.events = events.copy()
        self.events.set_index('user_id', inplace=True)

    def add_cohort_groups(self):
        """
        add different columns for cohort divison
        """
        self.events["CohortGroup"] = (
            self.events.groupby(level=0)["visit_date"].min().dt.isocalendar().week
        )
        self.events["first_visit_week"] = (
            self.events.groupby(level=0)["visit_date"].min().dt.isocalendar().week
        )
        self.events["last_visit_week"] = (
            self.events.groupby(level=0)["visit_date"].max().dt.isocalendar().week
        )
        self.events["visits_number"] = self.events.groupby(level=0)[
            "visit_date"
        ].count()