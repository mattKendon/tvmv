from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='tvmv',
    version='0.1',
    packages=['tvmv'],
    url='',
    license='MIT',
    author='Matthew Kendon',
    author_email='mkendon@gmail.com',
    description='Import tvshows from cdrom to folder on computer with filename change',
    long_description=readme(),
    install_requires=[
        'click',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': ['tvmv=tvmv.cli:tvmv'],
    }
)
