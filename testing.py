from insurance_premium.pipeline.pipeline import Pipeline
from insurance_premium.config.configuration import Configuration

def main():
    try:
    ### Testing data_ingestion
        # pipeline = Pipeline()
        # pipeline.run_pipeline()


    ### Testing data_validation_config written in configuration file
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)

    ### Testing data_validation
        # pipeline = Pipeline()
        # pipeline.run_pipeline()

    ### Testing data_transformation
        pipeline = Pipeline()
        pipeline.run_pipeline()


    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()