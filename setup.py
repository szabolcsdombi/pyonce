from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='pyonce',
    version='1.0.0',
    py_modules=['pyonce'],
    license='MIT',
    platforms=['any'],
    description='Run code once!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Szabolcs Dombi',
    author_email='cprogrammer1994@gmail.com',
    url='https://github.com/szabolcsdombi/pyonce/',
    project_urls={
        'Documentation': 'https://github.com/szabolcsdombi/pyonce/#readme',
        'Source': 'https://github.com/szabolcsdombi/pyonce/blob/main/pyonce.py',
        'Bug Tracker': 'https://github.com/szabolcsdombi/pyonce/issues/',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=['once'],
)
