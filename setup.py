from setuptools import setup

setup(
    name='wordle-helper',
    version='1.0.0',
    description='Determine remaining set of Wordle answers after guesses',
    url='https://github.com/keiche/wordle-helper',
    install_requires=['click'],
    classifiers=[
        'Environment::Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only'
    ]
)

