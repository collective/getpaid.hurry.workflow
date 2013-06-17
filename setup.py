from setuptools import setup, find_packages

setup(
    name="getpaid.hurry.workflow",
    version="0.9.2-getpaid",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['getpaid'],
    package_data={
        '': ['*.txt', '*.zcml'],
    },

    zip_safe=False,
    author='Infrae',
    author_email='faassen@infrae.com',
    description="""\
    forked from hurry.workflow, a simple workflow system. It can be used to
    implement stateful multi-version workflows for Zope 3 applications.
    """,
    license='BSD',
    keywords="zope zope3",
    classifiers=['Framework :: Zope3'],
    install_requires=['setuptools'],
)
