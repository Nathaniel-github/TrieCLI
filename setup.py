from setuptools import setup

with open("README.md", "r") as f:
    ld = f.read()

setup(
    name='trie-nathaniel',
    version='0.1.1',
    description='Calls commands to the trie server that can modify its state',
    python_requires='>=3.6',
    install_requires = [
        "inquirer >= 2.0"
    ],
    author='Nathaniel Thomas',
    author_email='catchnate+pypi@gmail.com',
    py_modules=["triecli"],
    package_dir={'': 'src'},
    license='MIT',
    url='https://github.com/Nathaniel-github/TrieClient',
    long_description=ld,
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "triecli=trie_nathaniel:main",
        ]
    },

    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8"
    ]
)
