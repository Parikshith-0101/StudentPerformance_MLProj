from setuptools import find_packages, setup
from typing import List


def get_req(file_path:str)->List[str]:
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[r.replace('\n','')for r in req]
        if '-e .' in req:
            req.remove('-e .')
    return req


setup(
    name='mlproj',
    version='0.0.1',
    author='Parikshith',
    author_email='parikshith2005@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt'),
)