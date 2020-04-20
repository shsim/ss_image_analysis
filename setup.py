import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='ss_image_analysis',
    version='0.0.1',
    author='Seu Sim',
    author_email='shsim@caltech.edu',
    description='Utilities for image analysis.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)