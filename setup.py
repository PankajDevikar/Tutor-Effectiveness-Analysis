from setuptools import setup, find_packages

setup(
    name="tutor_effectiveness_analysis",  # Name of your package
    version="0.1",  # Version of your package
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=[  # List of dependencies for the project
        'pandas>=1.5.3',
        'numpy>=1.23.5',
        'matplotlib>=3.7.1',
        'seaborn>=0.12.2',
        'scipy>=1.10.0'
    ],
    author="Minal Madankar Devikar",  # Your name or the author's name
    author_email="meenal.madankar@gmail.com",  # Author's email address
    description="Analysis of tutor effectiveness based on student engagement, outcomes, and feedback.",  # Short description of your project
    long_description=open('README.md').read(),  # If you have a README file for detailed project description
    long_description_content_type='text/markdown',  # Format of the long description
    url="https://github.com/yourusername/tutor-effectiveness-analysis",  # URL to the project (e.g., GitHub repository)
    classifiers=[  # Classifiers help people find your package by categorizing it
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)

