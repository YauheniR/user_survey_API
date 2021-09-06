# First start

[Русский](../ru/first_start.md) | **English**

You can run the **user-survey-API** project locally or in docker containers using the Makefile

### Dependencies

* [Python 3.8](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker-Compose](https://docs.docker.com/composer/install/)

### Installation

First of all, install [Docker](https://docs.docker.com/engine/install/) and [Docker-Compose](https://docs.docker.com/composer/install/)

After everything has been configured, you can run the project locally or deploy it in docker containers.

To run the project locally in [root](../..) for the project, run the command:

    make run_local

Now open the project in [browser](http://0.0.0.0:8000).

To run all project services in docker containers in [root](../..) for the project, run the command:

    make run_docker