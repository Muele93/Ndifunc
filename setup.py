from setuptools import setup, find_packages

setup(
    name='Ndifunc',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description="Ndivhuwo's Python package",
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/muele93/Ndifunc.git',
    author='Ndivhuwo Tshilande',
    author_email='nd.tshilande@gmail.com'
)
