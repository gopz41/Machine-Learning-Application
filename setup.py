#importing libraries
from setuptools import find_packages, setup
from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."
#defining function to fetch the requirement.txt
#takes input a filepath as string
#gives output a list of strings


def get_requirements()-> List [str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()

    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

#removing the (-e .) from the requirements.txt
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    
    return requirement_list


setup(name = "cost_prediction",
      version = "0.0.1",
      description= "Data Science projects",
      author = "Gopalakrishnan",
      author_email = "MLProject@gmail.com",
      packages = find_packages(),
      install_requires = get_requirements(), 
      )