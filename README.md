# Multi-Room-Web-Chat
Created a chat application for easy user communication.  
I have added functionality to create a channel, add new user to conversation and send message.
Communication and group handling was done with the help of Twilio API.

## Table of Contents
1. [Pre-requisite](#pre-requisite)
1. [Implementation](#implementation)
1. [Technologies Used](#technologies-used)

## Pre-requisite
Install the dependency by running the following command in terminal:
```
yarn install
```


## Implementation
- Clone the project

- Create the .env file in ```api``` directory.

- The .env file has the structure as below:
```
TWILIO_ACCOUNT_SID=<your-account-sid>
TWILIO_AUTH_TOKEN=<your-auth-token>
TWILIO_API_KEY_SID=<your-api-key-sid>
TWILIO_API_KEY_SECRET=<your-api-secret-key>
```

## Technologies Used
- Flask
- Node.js
- Twilio
