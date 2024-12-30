from setuptools import setup

package_name = 'neptr_desc'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Brian',
    maintainer_email='kryptozinc@gmail.com',
    description='The neptr_desc package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'leg_controller = neptr_desc.leg_controller:main',
        ],
    },
)