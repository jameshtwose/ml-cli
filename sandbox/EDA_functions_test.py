# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_validate, RepeatedStratifiedKFold
from sklearn.metrics import make_scorer, f1_score, accuracy_score, balanced_accuracy_score, recall_score, precision_score
from sklearn.metrics import confusion_matrix
from jmspack.ml_utils import optimize_model
# %%
df = (pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
      .dropna())
outcome="sex"
features_list = df.select_dtypes("number").columns.tolist()
X = df[features_list]
y = df[outcome]
# %%
(optimized_estimator,
     feature_ranking,
     feature_selected,
     feature_importance,
     optimized_params_df,
     ) = optimize_model(X=X, y=y, estimator=RandomForestClassifier(),
                        grid_params_dict={
         "max_depth": [1, 2, 3, 4, 5, 10],
         "n_estimators": [10, 20, 30, 40, 50],
         "max_features": ["log2", "sqrt"],
         "criterion": ["gini", "entropy"],
     },
        gridsearch_kwargs={"scoring": "accuracy", "cv": 3, "n_jobs": -2},
        rfe_kwargs={"n_features_to_select": 2, "verbose": 1})
# %%
optimized_params_df
# %%
optimized_params_df.assign(**{"selected_features": str(feature_selected)}).T
# %%
