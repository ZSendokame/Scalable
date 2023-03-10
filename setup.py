from setuptools import setup, find_packages

long_description = open('./README.md')

setup(
    name='ScalableWriter',
    version='1.2.1',
    url='https://github.com/ZSendokame/Scalable',
    license='MIT license',
    author='ZSendokame',
    description='Generate SVG code on a programmatic way.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',

    packages=(find_packages(include=['scalable']))
)
