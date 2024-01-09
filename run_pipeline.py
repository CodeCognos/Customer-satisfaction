from pipelines.training_pipeline import train_pipeline
from steps.clean_data import clean_df
from steps.evaluation import evaluate_model
from steps.ingest_data import IngestData
from steps.model_train import train_model
from steps.config import ModelNameConfig

if __name__ == "__main__":
    #ingest_step = ingest_df(data_path="data\olist_customers_dataset.csv")
    #clean_step = clean_df(ingest_step)
   # model_config = ModelNameConfig(model_name="LinearRegression")
   # train_step = train_model(clean_df)
    #evaluate_step = evaluate_model(train_step)
    
#clean_data, model_train, evaluation
  train_pipeline(data_path="data\olist_customers_dataset.csv")