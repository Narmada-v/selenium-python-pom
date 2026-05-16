<h1 align="center">Selenium POM</h1></br>

<p align="center">
:sparkles: Web Automation Testing using Selenium WebDriver, Python, &amp; POM design pattern :sparkles:
</p>

## Preparation

What will be used on this project


| Item           | Source                                                         |
| -------------- | ------------------------------------------------------------ |
| Editor         | VS Code (https://code.visualstudio.com/download) |
| Package Manager| PIP (https://pip.pypa.io/en/stable/getting-started/) |
| UI Test Tools  | Selenium WebDriver with Python (https://pypi.org/project/selenium/) |
|                | WebDriver Manager (https://pypi.org/project/webdriver-manager/) |
| Design Pattern | Selenium POM or Page Object Model |
| Test Reporter  | Pytest HTML (https://pytest-html.readthedocs.io/en/latest/) |
| Browser        | Latest version of Chrome / Mozilla Firefox  |

## Pre-Requisite Installation

Install VS Code Editor, Python, and PIP

To check whether you already installed Python & PIP

```Bash
python --version
```
```Bash
python -m pip --version 
```

## Testing Tools Installation

Install Selenium

```Bash
python -m pip install Selenium
```

Install Web Driver Manager

```Bash
python -m pip install webdriver-manager
```

## Setting up Project

### Clone

**👉 [Clone this Repository](https://github.com/Fatimazza/SeleniumPOM/)** through Terminal or Command Prompt

### Open the Project on Editor

Open this Automation Project using VS Code Editor.

### Run the Automation Project 

Change to Project directory on Terminal or Command Prompt

```Bash
cd SeleniumPOM
```

Run Specific Test Execution on Terminal

```Bash
python -m unittest TestCases/test_login.py
```

Run All Test Execution on Terminal

```Bash
python -m unittest
```

> Note: By default the Tests run on Chrome Browser

> To run on Firefox Browser, change the browser on TestCases/test_login.py and TestCases/test_product.py file

```Python
   # self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
```

### Generate Test Execution HTML Report

Install Pytest-HTML Reporter

```Bash
python -m pip install pytest-html
```

Run Selenium with the HTML Reporter

> Note: Please wait until all test execution finished

```Bash
python -m pytest --html=report.html
```

Test Execution HTML Report available on <b> SeleniumPOM/report.html </b>
