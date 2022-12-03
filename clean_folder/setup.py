from setuptools import setup, find_namespace_packages

setup(
    name="sort",
    version="0.2.0",
    author="Pupinin Igor",
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.sort:main']}
)
