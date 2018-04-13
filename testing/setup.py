from setuptools import setup

setup(name='testing',
    version='1.1',
    description='Our first package',
    url='http://saenz.com',
    author='Saenz',
    author_email='saenz@example.com',
    license='GPL',
    packages=['testing'],
    zip_safe=False,
    test_suite='testing.test',
)