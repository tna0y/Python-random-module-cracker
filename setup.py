from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='randcrack',  # How you named your package folder (MyLib)
    packages=['randcrack'],  # Chose the same as "name"
    version='0.1.5',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Predict python\'s random module random generated values',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Maxim Kochukov',  # Type in your name
    author_email='kochukov.ma@gmail.com',  # Type in your E-Mail
    url='https://github.com/tna0y/Python-random-module-cracker',  # Provide either the link to your github
    # or to your website
    download_url='https://github.com/tna0y/Python-random-module-cracker/archive/0.1.5.tar.gz',
    keywords=['random', 'security', 'cryptography', 'cracker', 'encryption'],  # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
