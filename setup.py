from setuptools import setup, find_packages

setup(
    name="downmark",
    version="0.1.0",
    description="Convert PDF, DOCX, XLSX, PPTX and HTML files to clean Markdown for LLMs",
    author="Your Name",
    author_email="mohamkallel@gmail.com",
    url="https://github.com/MohammedAmine-dev/DownMark",
    license="MIT",
    packages=find_packages(),
    py_modules=["cli", "app"],
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "downmark=cli:main",
        ]
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Utilities",
    ],
    keywords="markdown pdf docx xlsx pptx html converter llm cli",
)
