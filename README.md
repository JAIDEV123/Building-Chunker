# Building-Chunker
A revamped version of the Building Chunker Experiment hosted by IIIT-H for VLABS (a Govt. of India Initiative)

Chunking is an analysis of a sentence which identifies the constituents (noun groups, verbs, verb groups, etc.) which are correlated. These are non-overlapping regions of text.

*The objective of the experiment is to know the importance of selecting proper features for training a model and size of training corpus in learning how to do chunking.*

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following are required on your system in order to test the application

 1. Python
 2. Flask
 3. Linux System is preferred for testing

### Installation 

1. Python

`    sudo apt-get update
`
`    sudo apt-get install python3.6
`
	Check the version of python using `python3  -v`. Python3.6 + is recommended.

2. Flask

`    pip install flask
`

If you face any difficulties with installation or setup, do raise an issue.

## Testing

The setup for a flask application is pretty simple. Just run the following command:

`python3 main.py
`

This should start a web server at localhost:5000/ Type this link into your broswer's URL field in order to view the application.

Note: Whenever changes are made, the flask application must be restarted for the web server to reflect the updated changes.

Run this command: `python3 tests.py` to ensure that the application behaves as required. This is also the command used by Travis to validate pull requests.

## Contributing

Visit `/Contribute` to view the general contribution guidelines. We openly welcome first time contributors but do ensure that you follow the guidelines mentioned strictly.

## Authors

 - **Raghav Saboo**
 - **Jaidev Shriram**

