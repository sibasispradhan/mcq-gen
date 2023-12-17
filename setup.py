from setuptools import find_packages,setup

setup(
    name='mcq-genrator',
    version='0.0.1',
    author='sibasis pradhan',
    author_email='2021sc04667@wilp.bits-pilani.ac.in',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)