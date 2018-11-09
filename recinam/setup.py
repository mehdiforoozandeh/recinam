import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recinam",
    version="0.0.1",
    author='Mehdi Foroozandeh, Sasan Ashrafi',
    author_email="mehdiforoozandehsh@gmail.com , sasan.ashrafi.m@gmail.com",
    description='Nucleic Acid Memory Reciprocal Converter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehdiforoozandeh/recinam",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
