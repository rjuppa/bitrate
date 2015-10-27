from setuptools import setup

setup(
    name='bitrate',
    version='1.0',
    py_modules=['bitrate'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
        # Colorama is only required for Windows.
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        bitrate=bitrate:cli
    ''',
)
