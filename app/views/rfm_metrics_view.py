from pandas import DataFrame
import pandas as pd
import datetime as dt

class RFMMetricView:
    def interpreting_data(self, df: DataFrame):
        today_date = dt.datetime(2009, 11, 12)
        # Let's add a new variable to the data set to see the total price for each row.
        df["total_price"] = df["quantity"] * df["price"]
        
        # We obtain RFM metrics by grouping "Customer IDs" with aggregation methods that I use specific to each metric.
        rfm = df.groupby('customer_id').agg({'invoice_date': lambda InvoiceDate: (today_date - pd.to_datetime(InvoiceDate.max())).days,
                                            'invoice': lambda Invoice: Invoice.nunique(),
                                            'total_price': lambda TotalPrice: TotalPrice.sum()})
        
        # We name the columns according to the metrics.
        rfm.columns = ['recency', 'frequency', 'monetary']
        # We create RFM scores between 1-5.
        rfm["recency_score"] = pd.cut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
        rfm["frequency_score"] = pd.cut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
        rfm["monetary_score"] = pd.cut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])
        # The designation of the recency_score and frequency_score variables as the RFM_SCORE variable.
        rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))
        rfm = self.creating_segment(rfm)
        # Let's group our dataframe by segment and look at the averages of the RFM scores.
        rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])
        print(rfm)
        return rfm
    
    
    def creating_segment(self, rfm):
        # Creating segment map with regex
        seg_map = {
            r'[1-2][1-2]': 'hibernating',
            r'[1-2][3-4]': 'at_Risk',
            r'[1-2]5': 'cant_loose',
            r'3[1-2]': 'about_to_sleep',
            r'33': 'need_attention',
            r'[3-4][4-5]': 'loyal_customers',
            r'41': 'promising',
            r'51': 'new_customers',
            r'[4-5][2-3]': 'potential_loyalists',
            r'5[4-5]': 'champions'
        }

        # Let's define segments so that the generated RFM scores can be explained more clearly.
        rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
        return rfm

        