import pkg_resources

packages = ["google-generativeai", "pillow", "streamlit", "streamlit-option-menu"]

for package in packages:
    version = pkg_resources.get_distribution(package).version
    print(f"{package} version: {version}")
