from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "Insurance Premium Prediction"
VERSION = "0.0.1"
AUTHOR = "Tanweer Raza"
DESCRIPTION = "Building a solution that should be able to predict the premium of the personal for health insurance based on their individual health situation"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:     
    """
    ->List[str] This will return list in which there will be string in it.

    Description : This function is going to return list of all the requirements mentioned
    in requirements.txt file.
    return - This function is going to return a list which contain name of libraries mentioned
    in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()
)

