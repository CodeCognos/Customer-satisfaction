import logging

import pandas as pd
from zenml import step


class IngestData():
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self,data_path:str) -> None:
        """Initialize the data ingestion class."""
       
        self.data_path=data_path


    def get_data(self) -> pd.DataFrame:
        df = pd.read_csv("./data/olist_customers_dataset.csv")
        return df


@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Args:
        None
    Returns:
        df: pd.DataFrame
    """
    try:
        ingest_df = IngestData(data_path)
        df = ingest_df.get_data()
        logging.info("Ingesting data completed")
        return df
    except Exception as e:
        logging.error("Error while ingesting data")
        raise e