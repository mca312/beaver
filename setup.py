from distutils.core import setup

setup(
    name='Beaver',
    version='2',
    author='Jose Diaz-Gonzalez',
    author_email='support@savant.be',
    packages=['beaver'],
    scripts=['bin/beaver'],
    url='http://github.com/josegonzalez/beaver',
    license='LICENSE.txt',
    description='python daemon that munches on logs and sends their contents to logstash',
    long_description=open('README.rst').read(),
    install_requires=[
        "pika==0.9.5",
        "redis==2.4.11",
        "ujson==1.9",
    ],
)
