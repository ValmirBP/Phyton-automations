# Racquetball Reservation Automation

This Python script automates the process of reserving racquetball courts on the LA Fitness website.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Chrome browser
- ChromeDriver

You can install Python dependencies using the following command:


```console
pip install -r requirements.txt
```

## Usage

Clone the repository to your local machine:

```console
  git clone <repository_url>
```
### Navigate to the project directory:

```console
  cd racquetball-reservation-automation
```
### Create a .env File

Create a .env file in the project directory and add your LA Fitness credentials:

```console
  USER=your_username
  PASSWORD=your_password
```
### Run the script:

```console
  python main.py
```

# Description
This script logs into your LA Fitness account and selects a 
date, duration, time, and court for a racquetball reservation. 
It then makes the reservation automatically.

# Configuration
You can customize the following parameters in the script:

```console
  desired_time: #The desired time for the reservation (e.g., '05:30 PM').
  desired_duration_1: #The first desired duration for the reservation (e.g., '120 minutes').
  desired_duration_2: #The second desired duration for the reservation (e.g., '90 minutes').
  desired_duration_3: #The third desired duration for the reservation (e.g., '60 minutes').
  desired_court_1: #The first desired court for the reservation (e.g., '3 SQUASH COURT 3').
  desired_court_2: #The second desired court for the reservation (e.g., '4 SQUASH COURT 4').
```

# Notes

Ensure that your LA Fitness account credentials are kept confidential. Do not share them publicly.
Use this script responsibly and in accordance with LA Fitness terms of service.
