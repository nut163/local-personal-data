# Personal CRM Application

This is a personal CRM application that securely stores details about your life and activity. The CRM is fully accessible via API and webhooks when using valid credentials. Events occurring on the CRM are able to trigger automation events on other platforms.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python and pip installed on your machine. You can verify your installation by running the following commands in your terminal:

```
python --version
pip --version
```

### Installing

Clone the repository:

```
git clone https://github.com/username/personal-crm.git
```

Navigate to the project directory:

```
cd personal-crm
```

Install the dependencies:

```
pip install -r requirements.txt
```

Create a .env file in the root directory and add your environment variables:

```
touch .env
```

Run the application:

```
python src/main.py
```

## Running the tests

To run the tests, navigate to the project directory and run:

```
python -m unittest discover src/tests
```

## Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.