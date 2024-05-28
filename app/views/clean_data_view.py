import pandas as pd


class CleanDataView:
    """
    Class to clean the dataframe"""

    def load_data(self):
        """Reading the excel format data set by using "Year 2010-2011" sheet named."""
        try:
            df_ = pd.read_excel("short.xlsx", sheet_name="Year2009-2010")
            df = df_.copy()
            return df
        except Exception as e:
            print("Error loading data from file data: ", e)
        return False

    def describe(self, df):
        """Examining descriptive statistics"""
        return df.describe().T

    def browsing(self, df):
        """Browsing the dataset"""
        return df.head()

    def clean_data(self, df):
        """Detection of missing variables"""
        df.isnull().sum()
        # Remowing of missing variables
        df.dropna(inplace=True)
        # Convert "Invoice" column values to string
        df["Invoice"] = df["Invoice"].astype(str)
        # Removing canceled transactions from the dataset
        df = df[~df["Invoice"].str.contains("C", na=False)]
        return df

    def add_variable_dataset(self, df):
        """Let's add a new variable to the data set to see the total price for each row."""
        df["TotalPrice"] = df["Quantity"] * df["Price"]
        return df
        
    def preparation_df(self):
        """ All the task for clean the dataframe """
        df = self.load_data()
        if df is False:
            return False
        try:
            df = self.clean_data(df)
            # df = self.add_variable_dataset(df)
            return df
        except Exception as e:
            print("Error proccesing data", e)
        return False
        
        
