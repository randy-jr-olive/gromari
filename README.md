# gromari

Gromari is an app that allows for the management of plant grow rooms. Each room has a list of plants and equipment contained within. A journal system is available to track plant progress, watering, fertilization, etc. Tags are used to organize grow activites. Gromari is written in Python using Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The app is built using Docker containers and the docker-compose utility.
Docker can be obtained here: [https://www.docker.com/get-started](https://www.docker.com/get-started)
Docker Compose is available here: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

### Running

From within the source code directory run the following command:
`docker-compose -f docker-compose.yml up`

## Running the tests

`docker exec gromari-web coverage run --source='.' manage.py test --noinput`

## Built With

* Django & Python3
* BeautifulSoup4
* Docker

## Authors

* **Randy Olive** - *Design & Code*

## Acknowledgments
