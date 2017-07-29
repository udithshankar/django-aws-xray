from setuptools import find_packages, setup

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'coverage==.4.2',
    'pytest==3.0.5',
    'pytest-cov==2.5.1',
    'pytest-django==3.1.2',

    # Linting
    'isort==4.2.5',
    'flake8==3.0.3',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==1.4.0',
]

setup(
    name='django-aws-xray',
    version='0.1.0',
    description="Django AWS X-Ray",
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/mvantellingen/django-aws-xray',
    author="Michael van Tellingen",
    author_email="",
    install_requires=[
        'attrs>=17.2.0',
        'Django>=1.8',
        'six>=1.1',
    ],
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    use_scm_version=True,
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)
