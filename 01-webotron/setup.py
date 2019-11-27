from setuptools import setup

setup(
    name='webotron-80-clone',
    version='0.1',
    author='Terry',
    author_email='no-email@hotmail.com',
    description='Webotron 80 clone is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/perspicacity-net/automating-aws-with-python/tree/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
