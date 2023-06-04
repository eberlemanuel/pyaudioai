import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyaudioai',
    author='Manuel Eberle',
    author_email='info@manueleberle.de',
    description='Get an audio response from ChatGPT',
    keywords='chatgpt, openai, audio, tts, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/eberlemanuel/pyaudioai',
    project_urls={
        'Documentation': 'https://github.com/eberlemanuel/pyaudioai',
        'Bug Reports': 'https://github.com/eberlemanuel/pyaudioai/issues',
        'Source Code': 'https://github.com/eberlemanuel/pyaudioai',
        'Source Code Documenetation': 'https://eberlemanuel.github.io/pyaudioai',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=['openai', 'gTTS', 'playsound', 'pyaudio', 'wave'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
