# Readme

Install Python3.13.2 and set up the PATH for Python.

Python website：https://www.python.org/

This framework is built based on Python3.13.2. And you will need to insntall the following dependencies and libraries listed in the `requirements.txt` file.

```shell
pip install -r requirements.txt
```
For Testing Reports, we are using Allure. So if you want to generate and check reports, you will need to install Allure. For how to do that, you can check the following -

- https://allurereport.org/docs/install/

For UI Automation, we are using Playwright. Please install the required browsers:

```shell
playwright install
```

## File Structure

```
.\pytest.ini # pytest configurations
.\conftest.py # shared fixture for all applications
.\pages\xxx_page.py # Page Objects for UI Automation
.\locators\xxx.py  # locators for UI Automation
.\tests\test_xxx.py # Test cases for UI Automation
.\autoReports\xxx # Testing Results/Reports
.\playwright\ # For UI Automation -

```

## Usage

After the installation, you can start to run test cases as follow -

### Specify the environments/markers/keywords

`$ python -m pytest -m smoke -k tests`
This will run the smoking test cases matching `tests` using testing accounts

Notes：

- `-m` Specify the test markers.

- `-k` Specify the matching keywods. It will search for your tests, looking for matches.

## Allure Test Reports

When test run completes, you can use the following commands to generate the Allure Reports -

`allure generate autoreports\ -o autoreports\html\ --clean`

This will generate a .html file under `autoreports\html`, you can open this file in your browser or you can use the following command to serve the html file.

`$ allure serve autoreports\`

```
