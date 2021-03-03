import pandas as pd 

class Prerpocessing:
    def __init__(self, events):

        self.events = events.copy()

    def user_to_dict(self):

        uniq_id = list(set(self.events.user_id.to_list()))
        dict_id = {uniq_id[i]: i for i in range(len(uniq_id))}

        return dict_id

    def encode_users(self):

        dict_id = self.user_to_dict()

        for idx in range(len(self.events.user_id)):
            idx_ = self.events.user_id.iloc[idx]
            self.events.loc[idx, "user_id"] = dict_id[idx_]

    def preprocess_date(self):

        self.events["visit_date"] = pd.to_datetime(
            self.events["visit_date"], format="%d.%m.%Y"
        )

        self.events["user_reg_date"] = pd.to_datetime(
            self.events["user_reg_date"], format="%d.%m.%Y"
        )

        self.events["week_number"] = self.events["visit_date"].dt.isocalendar().week

        self.events["registered_after"] = (
            self.events["visit_date"]
            .sub(self.events["user_reg_date"])
            .dt.days.astype(int)
        )

    def preproce_it(self):

        self.encode_users()
        self.preprocess_date()

        self.agg_features = (
            self.events.groupby("user_id")["week_number"]
            .agg(["mean", "std", "min", "max"])
            .reset_index()
        )
        self.events = pd.merge(self.events, 
                               self.agg_features, 
                               on="user_id")