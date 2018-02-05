from setuptools import setup

setup_deps = [
    'pytest-runner',
]

test_deps = [
    'testfixtures',
    'pytest',
    'pytest-cov',
    'coveralls',
]

extras = {
    'test': test_deps,
}

setup(
    name='injectable',
    version='0.1.0',
    packages=['tests', 'injectable'],
    url='https://github.com/allrod5/injectable',
    license='MIT',
    author='rodrigo',
    author_email='allrod5@hotmail.com',
    description='Cleanly expose injectable arguments in Python 3 functions',
    setup_requires=setup_deps,
    test_requires=test_deps,
    extras_require=extras,
)
