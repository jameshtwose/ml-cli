import typer
import pandas as pd
from EDA import create_descriptives
from classification import fit_predict_evaluate_classification
from report_templates import classification_report_template

app = typer.Typer()


@app.command()
def descriptives(filename: str):
    df = pd.read_csv(filename)
    if any([x == "Unnamed: 0" for x in df.columns.tolist()]):
        _ = df.drop(columns="Unnamed: 0", inplace=True)
    _ = create_descriptives(data=df)


@app.command()
def make_report(filename: str, export_name="report.html", outcome=None):
    df = pd.read_csv(filename)
    if any([x == "Unnamed: 0" for x in df.columns.tolist()]):
        _ = df.drop(columns="Unnamed: 0", inplace=True)
    EDA_results_dict = create_descriptives(
        data=df, cli_output=False, outcome=outcome)

    classification_results_dict = fit_predict_evaluate_classification(
        data=df.dropna(), outcome=outcome)

    _ = classification_report_template(filename=export_name,
                                       dataframe_head_insert=EDA_results_dict["head_df"].to_html(
                                       ),
                                       dataframe_descriptives_insert=EDA_results_dict["desc_df"].to_html(
                                       ),
                                       plot_descriptives_insert=EDA_results_dict["desc_plot"],
                                       plot_outcomes_insert=EDA_results_dict["outcome_count_plot"],
                                       plot_corrs_insert=EDA_results_dict["corr_plot"],
                                       dataframe_missingness_insert=EDA_results_dict["miss_df"].to_html(
                                       ),
                                       dataframe_optimized_model_insert=classification_results_dict["model_summary_df"].to_html(
                                       ),
                                       plot_cross_validation_insert=classification_results_dict[
                                           "cross_val_plot"],
                                       plot_confusion_insert=classification_results_dict["confusion_plot"],
                                       dataframe_filename=filename)


if __name__ == "__main__":
    app()
