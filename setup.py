from setuptools import find_packages, setup
from typing import List

HYFEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements from the file'''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]
        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)
        
    

setup(
    name='ML-PROJECT',
    version='0.0.1',
    author='Aakash Talyan',
    author_email='aakashtalyan14@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)