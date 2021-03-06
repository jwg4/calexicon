from setuptools import setup

setup(
    name='calexicon',
    version='0.1.2',
    description='Calendar stuff',
    url='http://github.com/jwg4/calexicon',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    license='Apache License 2.0',
    packages=['calexicon', 'calexicon.calendars', 'calexicon.internal', 'calexicon.dates', 'calexicon.fn'],
    test_suite='nose.collector',
    tests_require=['nose', 'hypothesis']
)

