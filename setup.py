from setuptools import setup, find_packages

setup(
    name="content_creation_agency",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "agency-swarm>=0.1.0",
        "python-dotenv>=0.19.0",
        "gradio>=4.0.0",
        "openai>=1.0.0",
        "google-api-python-client>=2.0.0",
        "google-auth-oauthlib>=0.4.0",
        "google-auth-httplib2>=0.1.0",
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=0.24.0",
        "nltk>=3.6.0",
        "beautifulsoup4>=4.9.0",
        "requests>=2.26.0",
        "python-docx>=0.8.0",
        "markdown>=3.3.0",
        "pyyaml>=5.4.0",
    ],
) 