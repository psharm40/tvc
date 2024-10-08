# Computer Vision for TCV
## Setup
In the cv folder, create a [virtual environment](https://docs.python.org/3/library/venv.html). This can be done in VS Code by opening the cv folder as a project and clicking View -> Command Pallete... -> `Python: Create Virtual Environment...`

Next, install the requirements listed in `requirements.txt`:
```
pip install -r requirements.txt
```
This will install all of the necessary dependencies for the project. If additional dependencies are added to the requirements, this same command can be used to install the new ones.

## Adding Dependencies
To install additional dependencies manually, use:
```
pip install <package name>
```
Before you push your changes, make sure to update the `requirements.txt` using:
```
pip freeze > requirements.txt
```