# Первый старт

**Русский** | [English](../en/first_start.md)

Вы можете запустить проект **user-survey-API** локально или в докер контейнерах используя Makefile

### Зависимости

* [Python 3.8](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker-Compose](https://docs.docker.com/compose/install/)

### Установка

Прежде всего, установите [Docker](https://docs.docker.com/engine/install/) и [Docker-Compose](https://docs.docker.com/compose/install/)

После того, как все было настроено, вы можете запустить проект локально либо развернуть его в докер контейнере.

Для запуска проекта локально в [корне](../..) проекта выполните комманду:

    make run_local

Теперь откройте проект в [браузере](http://0.0.0.0:8000).

Для запуска проекта в докер контейнерах в [корне](../..) проекта выполните комманду:

    make run_docker