from setuptools import setup

package_name = 'mypkg'
import os
from glob import glob

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Keiyo Nakayama',
    maintainer_email='keiyou0206@gmail.com',
    description='ロボットシステム授業用',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'check_cpu_stats = mypkg.check_cpu_stats:main',
        ],
    },
)
