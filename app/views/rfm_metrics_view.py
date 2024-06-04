from pandas import DataFrame
import pandas as pd
from pandas import Timestamp
import datetime as dt
import mlflow
import mlflow.sklearn
from sklearn.preprocessing import OneHotEncoder


class RFMMetricView:
    def interpreting_data(self, df: DataFrame):
        today_date = dt.datetime(2009, 11, 12)
        # Let's add a new variable to the data set to see the total price for each row.
        df["total_price"] = df["quantity"] * df["price"]

        # We obtain RFM metrics by grouping "Customer IDs" with aggregation methods that I use specific to each metric.
        rfm = df.groupby("customer_id").agg(
            {
                "invoice_date": lambda InvoiceDate: (
                    today_date - pd.to_datetime(InvoiceDate.max())
                ).days,
                "invoice": lambda Invoice: Invoice.nunique(),
                "total_price": lambda TotalPrice: TotalPrice.sum(),
            }
        )

        # We name the columns according to the metrics.
        rfm.columns = ["recency", "frequency", "monetary"]
        # We create RFM scores between 1-5.
        rfm["recency_score"] = pd.cut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
        rfm["frequency_score"] = pd.cut(
            rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]
        )
        rfm["monetary_score"] = pd.cut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
        # The designation of the recency_score and frequency_score variables as the RFM_SCORE variable.
        rfm["RFM_SCORE"] = rfm["recency_score"].astype(str) + rfm[
            "frequency_score"
        ].astype(str)
        # mlflow.set_tracking_uri(uri="./mytracks")
        print("The set to tracking uri is", mlflow.get_tracking_uri())
        exp = mlflow.set_experiment(experiment_name="experment_2")
        with mlflow.start_run(experiment_id=exp.experiment_id, run_name="run_2"):
            rfm = self.creating_segment(rfm)
            # Let's group our dataframe by segment and look at the averages of the RFM scores.
            rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(
                ["mean", "count"]
            )
            print(rfm)
            ## automatic login 
            ## mlflow.autolog(log_input_examples=True)

            mlflow.log_param("recency", rfm["recency"].to_string())
            mlflow.log_param("frequency", rfm["frequency"].to_string())
            mlflow.log_param("monetary", rfm["monetary"].to_string())
            mlflow.log_metric("recency_score", 90.0)
            mlflow.log_metric("frequency_score", 77.7)
            mlflow.log_metric("RFM_SCORE", 88.8)
            mlflow.sklearn.log_model(rfm, "rfm_model")

            #log parameters
            params ={
                "alpha": "alpha",
                "l1_ratio": "l1_ratio"
            }
            #log metrics
            metrics = {
                "rmse":00.00,
                "r2":90.00,
                "mae":77.90
            }
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)

            tags = {
                "engineering": "ML platform",
                "release.candidate":"RC1",
                "release.version": "2.0"
            }
            mlflow.set_tags(tags)
            run = mlflow.active_run()
            print("Active run id", run.info.run_id)
            print("Active run name", run.info.run_name)

            run = mlflow.last_active_run()
            print("Active last run id", run.info.run_id)
            print("Active last run name", run.info.run_name)

            mlflow.log_artifacts("data/")
            artifacts_uri=mlflow.get_artifact_uri()
            print("The artifact path is",artifacts_uri )

            print("Lifecycle_stage: {}".format(exp.lifecycle_stage))
            print("Creation timestamp: {}".format(exp.creation_time))
            
            ## register the model
            mlflow.register_model(
                model_uri='runs:/{}/model'.format(run.info.run_id),
                name='elastic-api-2'
    )


        return rfm

    def creating_segment(self, rfm):
        # Creating segment map with regex
        seg_map = {
            r"[1-2][1-2]": "hibernating",
            r"[1-2][3-4]": "at_Risk",
            r"[1-2]5": "cant_loose",
            r"3[1-2]": "about_to_sleep",
            r"33": "need_attention",
            r"[3-4][4-5]": "loyal_customers",
            r"41": "promising",
            r"51": "new_customers",
            r"[4-5][2-3]": "potential_loyalists",
            r"5[4-5]": "champions",
        }

        # Let's define segments so that the generated RFM scores can be explained more clearly.
        rfm["segment"] = rfm["RFM_SCORE"].replace(seg_map, regex=True)
        return rfm
