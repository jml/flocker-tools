from setuptools import setup

setup(
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Logging',
    ],
    name='flocker-tools',
    version='0.0.1',
    description="Tools to help administer flocker clusters",

    entry_points={
        'console_scripts': [
            'repair-json = flocker_tools._json:main',
        ],
    },

    install_requires=[
    ],
    extras_require={
        "dev": [
            # Bug-seeking missile:
            "hypothesis",
            # Tasteful testing:
            "testtools",
        ]
    },
    keywords="logging",
    license="Apache 2.0",
    packages=["flocker_tools", "flocker_tools.tests"],
    url="https://github.com/ClusterHQ/flocker-tools/",
    maintainer='Jonathan Lange',
    maintainer_email='jml@clusterhq.com',
)
