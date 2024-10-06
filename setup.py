# from setuptools import setup
# # from setuptools import setup, find_packages

# setup(
#     name='chat2note',
#     version='1.0',
#     py_modules=['chat2note'],
#     install_requires=[
#         "openai",
#         "DrissionPage",
#         "python-dotenv"
#     ],  # 如果有额外的依赖包，请在这里添加
#     entry_points='''
#         [console_scripts]
#         chat2note=main:main
#     ''',
# )
# setup.py
from setuptools import setup, find_packages

setup(
    name='chat2note',
    version='0.1.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chat2note=cli.cli:main',
        ],
    },
    install_requires=[
        "openai",
        "DrissionPage",
        "python-dotenv"
    ],
)
