# Project Title

> **Introduction** : One Paragraph of project description goes here

### Table of Contents
1. [Getting Started](#gettingStarted)
    A. [Prerequisities](#Prerequisites)
    B. [Quick Start Guide](#quickguide)
    c. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Results](#results)
4. [Repository Organization Structure](#files)
5. [Licensing, Authors, and Acknowledgements](#licensing)
6. [Additional Information](#additional)
    A. [Running the tests](#tests)
    B. [Deployment Examples](#Deployment)
    C. [Built With](#Built%20With)
    D. [Contibuting](#Contributing)

## Getting Started <a name="gettingStarted"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

#### Prerequisites

Following softwares are required to be installed in order build and run this application/files: 
1. Python 3 (Follow the guidelines from this [link](https://realpython.com/installing-python/) to install python).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Optional : Install virtual environment for clean setup. Use the [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for installation guidelines.
2. Git . (Follow this [guidelines](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html) to install & get started with git command line.)


#### Quick Start Guide <a name="quickguide"></a>
- Clone the directory into your desired path
```bash
git clone https://github.com/rindhane/DataMusings.git demo
```
- Using terminal go to to inside the dowloaded repository folder
 ```bash
  cd demo/
 ```
- Using terminal initate the python virtual environment and install dependencies
 ```bash
python -m venv pyenv

source pyenv/bin/activate

pip install -r requirements.txt

 ```
- Run the following command to start the local webserver to serve the application locally
```bash

python main.py
```

### Installation <a name="installation"></a>

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


## Project Motivation<a name="motivation"></a>

Brief Statement about the statement, or start with the Question which intiated the thought process:

1. Question 1 ?
2. Question 2 ?
3. Question 3 ?

One paragraph on the background of the project 

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](#Deployment Link)

## Repository Organization Structure <a name="files"></a>
    
-  Code's module structure is as follows 

```
Project [Root Folder]/
├── Analysis & Data Exploration/
│   ├── ETL Pipeline Preparation.ipynb
│   └── ML Pipeline Preparation.ipynb
├── app/
│   ├── run.py
│   └── templates/
│       ├── go.html
│       └── master.html
├── data/
│   ├── disaster_categories.csv
│   ├── disaster_messages.csv
│   ├── DisasterResponse.db
│   └── process_data.py
├── models/
│   ├── classifier.pkl
│   ├── model_details.txt
│   └── train_classifier.py
├── docs/
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
└── .readthedocs.yml
```
**Details:**
+ *Analysis Analysis & Data Exploration:* Contains the jupyter notebooks which will give fair idea about the analysis of data & development steps of application.
+ *app:* It is the folder with all the files related to the web app made in flask.
+ *data:* Primary data files based on which application was trained upon and file `process_data.py` which contains the etl_pipeline.
+ *models:* Holds the ML pipepline file `train_classifier.py` which creates the model for text labelling.
+ *docs:* This files contains the files for holding the documentation.
+ *other files:* This are configuration files for application.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Credits : 
* **Person** -[Reach out](#Handle)
    - Details 
    - Inspiration
    - Referene to work 
* @Inspired from [**Original Source**](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) by [@PurpleBooth](https://github.com/PurpleBooth)
* @Adopted some style from [source]https://github.com/jjrunner/stackoverflow by [@jjrunner](https://github.com/jjrunner)


-----------------------------------------------------------

## Additional Information<a name="additional"></a> 

### Running the tests <a name="tests"></a>

Explain how to run the automated tests for this system

* Break down into end to end tests

    Explain what these tests test and why

    ```
    Give an example
    ```
### Deployment

Add additional notes about how to deploy this on a live system

### Built With

* [Dependecy1](http://WebFrameWork) - The web framework used
* [Dependecy2](https://maven.apache.org/) - Dependency Management

### Contributing

Please read [CONTRIBUTING.md](#Contribution-Guidelines-Link) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

------------------------------------
***End***
