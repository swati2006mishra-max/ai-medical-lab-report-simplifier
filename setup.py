from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-medical-lab-report-simplifier",
    version="0.1.0",
    author="Swati Mishra",
    author_email="swati2006mishra@gmail.com",
    description="AI-powered medical lab report simplifier using OCR and AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swati2006mishra-max/ai-medical-lab-report-simplifier",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps",
    ],
    python_requires=">=3.8",
    install_requires=[
        "opencv-python>=4.5.0",
        "pytesseract>=0.3.10",
        "Pillow>=8.0.0",
        "openai>=0.27.0",
        "python-dotenv>=0.19.0",
        "requests>=2.28.0",
    ],
)
