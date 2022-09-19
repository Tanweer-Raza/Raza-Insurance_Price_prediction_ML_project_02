from insurance_premium.component import data_ingestion
from insurance_premium.component.data_validation import DataValidation
from insurance_premium.config.configuration import Configuration
from insurance_premium.logger import logging
from insurance_premium.exception import InsurancePremiumExcecption

from insurance_premium.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from insurance_premium.entity.config_entity import DataIngestionConfig
from insurance_premium.component.data_ingestion import DataIngestion
import os,sys

class Pipeline:

    def __init__(self , config : Configuration =  Configuration()):
        try:
            self.config = config
        except Exception as e:
            raise InsurancePremiumExcecption(e,sys) from e


    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())

            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise InsurancePremiumExcecption(e,sys) from e


    def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact)-> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
            data_ingestion_artifact= data_ingestion_artifact)
            
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise InsurancePremiumExcecption(e,sys) from e

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)
        except Exception as e:
            raise InsurancePremiumExcecption(e,sys) from e 