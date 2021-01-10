import setuptools

setuptools.setup(
    name='process-uptime',
    version='2021.1.10',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
