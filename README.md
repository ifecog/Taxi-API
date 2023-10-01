# Taxi-API
Taxi API is a real time, fully-functional, robust, and scalable REST API. 

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General Info
Many modern ride-sharing apps rely on efficient, real-time, and bi-directional communication to provide users with a seamless and exceptional experience. One prime example is a ride-sharing platform akin to Uber or Lyft, which is intricately built on the exchange of messages between riders and drivers. This Taxi REST API facilitates the core functionality of such a service.

User Interactions:

    Requesting a Ride:
        A rider initiates the process by selecting their current location and desired destination.
        The system broadcasts a trip request to all available nearby drivers.

    Driver Response:
        An available driver acknowledges the trip request and accepts the ride assignment.
        The driver proceeds to the rider's specified pick-up location.

    Real-time Tracking:
        Throughout the ride, every move the driver makes is transmitted in near real-time to the rider.
        The rider can closely monitor the trip's status as long as it remains active.

Key Features:

    Trip Management: The API manages the creation, tracking, and completion of trips, ensuring a smooth rider-driver interaction.

    Real-time Updates: It facilitates instant communication of driver movements to riders, allowing them to follow the trip progress.

    Secure Transactions: The API ensures secure and transparent transactions between riders and drivers, including fare calculation and payment processing.

    Geospatial Integration: Leveraging geospatial data, the API accurately determines driver availability and trip routing.

    User Authentication: Robust user authentication mechanisms safeguard the integrity of the platform.

Whether you're building a ride-sharing service from the ground up or enhancing an existing one, this Taxi REST API forms the foundation for seamless, real-time rider-driver interactions, offering users an unparalleled and reliable transportation experience.

## Technologies
* [Python](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Django Channels](https://channels.readthedocs.io/en/latest/)
* [Django Rest Framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [Redis](https://redis.io/)
* [Python Unit Test module](https://docs.python.org/3/library/unittest.html)
* [PyTest](https://docs.pytest.org/en/latest/)
* [Postman](https://www.postman.com/)

## Setup
Download and install Python
```
(https://www.python.org/downloads/)
```
Create project directory and enable virtual environment
```
$ cd ../project_directory
$ python -m venv myenv
$ venv\Scripts\activate
```
Install all necessary libraries and frameworks using pip
```
$ pip install \
  channels==2.3.1 \
  channels-redis==2.4.1 \
  Django==2.2.8 \
  djangorestframework==3.10.3 \
  djangorestframework-simplejwt==4.4.0 \
  Pillow==6.2.1 \
  psycopg2-binary==2.8.4 \
  pytest-asyncio==0.10.0 \
  pytest-django==3.7.0
```
