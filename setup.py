from setuptools import Command, setup

setup(
        name='mobiledetector',
        version='0.0.1',
        url='http://github.com/lojack/mobiledetector',
        license='BSD',
        author='Robert Clark',
        author_email='robert@bablmedia.com',
        packages=['mobiledetector'],
        test_suite='mobiledetector.tests',
        include_package_data=True
)
