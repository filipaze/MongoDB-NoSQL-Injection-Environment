# MongoDB NoSQL Injection Test Environment

## Introduction

This project is a testing application for MongoDB, written in Python using Flask. It is specifically designed to demonstrate and test MongoDB implementations for NoSQL injection vulnerabilities. The application features user registration, login, and data retrieval functionalities, providing a practical context for understanding and testing NoSQL database interactions.

## Setup Instructions

To set up and run this application, you will need Docker installed on your system. Once Docker is installed, you can use the following command to build and run the application:

```
docker-compose up --build
```

This command will build the necessary Docker containers and start the application. Once the application is running, you can access it through your web browser at `http://localhost:6543`.

## Security Note

This application is intended for testing and educational purposes. It includes three points of communication with the MongoDB database, one of which is deliberately vulnerable to NoSQL injection. This vulnerability is included as a part of the testing environment to allow users to understand and experiment with NoSQL injection techniques in a controlled setting.

Please be aware that this application should not be used in a production environment due to its intentional security vulnerabilities.

## Final Note

The application is still quite simple, and any improvements or enhancements are always welcome. If you have ideas or contributions that could make this project better, feel free to fork the repo and submit your changes. Your input is highly appreciated!
