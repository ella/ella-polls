from setuptools import setup, find_packages
import ella_polls

setup(
    name='ella-polls',
    version=ella_polls.__versionstr__,
    description='Polls/contests/quizes for Ella CMS',
    long_description='\n'.join((
        'Public voting plugin for Ella CMS',
        '',
        'Implements often used public voting mechanisms for internet news sites:'
        '* Polls',
        '* Contests',
        '* Quizes',
        '* Surveys (simplified polls)'
    )),
    author='Ella Development Team',
    author_email='dev@ella-cms.com',
    license='BSD',
    url='http://ella.github.com/',

    packages=find_packages(
        where='.',
        exclude=('doc', 'test_ella_polls')
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'Django==1.3.1',
        'south>=0.7',
        'ella>=3.0.0',
    ],
    setup_requires=[
        'setuptools_dummy',
    ],
    test_suite='test_ella_polls.run_tests.run_all'
)
