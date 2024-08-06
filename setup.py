from setuptools import setup, find_packages

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    """
    this function will return the list of requirments from the file
    """
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='ML',
    version='0.0.1',
    author='Ayush Srivastava',
    author_email='krayush.srivastav@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)