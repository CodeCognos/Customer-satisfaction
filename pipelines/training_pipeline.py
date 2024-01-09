#from zenml import Repository
from zenml import pipeline
from steps.clean_data import clean_df
from steps.evaluation import evaluate_model
from steps.ingest_data import IngestData, ingest_df
from steps.model_train import train_model
#from custom_components import CustomDBInitializer


@pipeline(enable_cache=True)
def train_pipeline(data_path:str):

    #repo = Repository()
    """
    Args:
        ingest_data: DataClass
        clean_data: DataClass
        model_train: DataClass
        evaluation: DataClass
    Returns:
        mse: float
        rmse: float
    """
    
    df = ingest_df(data_path)
    x_train, x_test, y_train, y_test = clean_df(df)
    model = train_model(x_train, x_test, y_train, y_test)
    mse, rmse = evaluate_model(model, x_test, y_test)

     # Initialize and run the CustomDBInitializer component
    #custom_db_init = CustomDBInitializer()
   # custom_db_init.run()