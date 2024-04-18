# Tapo Energy Measurement

Quick script to measure and plot measured wattage of a tapo smart plug.

> Please note: I have only tested this with a P110 on Windows 10- results may vary across models

## Setup

### Dependencies

Python >=3.10 and pipenv

### Install

1. `pipenv install`
2. Set the correct variables in a new `.env` file. Use `.env.example` as an example
3. `pipenv run py .\benchmark.py`
4. The script will plot live energy usage and save the results to a new time-stamped csv
