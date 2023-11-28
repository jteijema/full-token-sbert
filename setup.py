from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-FT-sbert',
    version='0.1',
    description='Full Token Sentence BERT model for ASReview',
    url='https://github.com/asreview/asreview',
    author='ASReview team',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.7',
    install_requires=[
        'asreview>=1.2'
    ],
    entry_points={
        'asreview.models.feature_extraction': [
            'ft_sbert = asreviewcontrib.models:FullTextSBERTModel',
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/asreview/issues',
        'Source': 'https://github.com/asreview/asreview/',
    },
)
