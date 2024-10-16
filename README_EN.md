# Project Overview

[中文](./README.md) [ENGLISH](./README_EN.md)

`Chat2Note` is a tool that converts conversations with `ChatGPT` into notes for easy saving and reviewing. `Chat2Note` provides a web interface with a visual preview of the generated notes, allowing users to view, edit, and export the notes in real-time.

# Installation

## Prerequisites
- Operating System: `Windows` or `MacOS`
- `Chrome` browser installed
- `Python 3.8+`
- Access to the `ChatGPT` website

## Full Version

### Backend
#### Clone the project locally:
```bash
git clone https://github.com/CosmicResearchCenter/chat2note.git
```
#### Enter the backend root directory:
```bash
cd chat2note/api
```
#### Configure .env
```bash
cp .env_copy .env
vim .env
```
#### Update the .env file with your MySQL settings:
```bash
MYSQL_IP=localhost
MYSQL_PORT=3306
MYSQL_BASE=chat2note
MYSQL_USER=chat2note
MYSQL_PASSWORD=chat2note
```

If you already have a MySQL instance, you can modify the settings based on your MySQL info and skip starting the MySQL container.

#### Start the MySQL container
```bash
docker-compose up -d
```

#### Create and activate the virtual environment
```bash
python -m venv venv
source venv/bin/activate  # MacOS
.\venv\Scripts\activate   # Windows
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Database migration
```bash
alembic upgrade head
```

#### Start the backend
```bash
python app.py
```

### Frontend
#### Navigate to the frontend root directory
```bash
cd ../web/
```

#### Build the Docker image
```bash
docker build -t chat2note_web .
```
#### Run the Docker container
```bash
docker run -d --name chat2note_web -p 2024:80 chat2note_web
```

#### You can now preview the application in your browser at:
[http://127.0.0.1:2024/](http://127.0.0.1:2024/)

## CLI Version
1.	Clone the project locally:
	```bash
	git clone https://github.com/CosmicResearchCenter/chat2note.git
	```
2.	Navigate to the project directory and create a virtual environment:
	```bash
	cd chat2note/api
	python -m venv venv
  ```
3.	Activate the virtual environment and install dependencies:
	```bash
	source ./venv/bin/activate
	pip install .
  ```
# CLI Usage Guide

## Set environment variables
Set the following environment variables depending on your operating system:

### Windows
```bash
$env:BASE_URL="Your OPENAI API Base URL"
$env:API_KEY="Your OPENAI API Key"
$env:MODEL="Model Name"
```
#### MacOS
```bash
export BASE_URL="Your OPENAI API Base URL"
export API_KEY="Your OPENAI API Key"
export MODEL="Model Name"
```

## Run the tool
Use the shared link from the ChatGPT conversation with the following command:
```bash
chat2note -u https://chatgpt.com/share/xxxxx
```

## Success Message
When the tool runs successfully, you will see the following message:
```bash
-------------------------------------------------start-------------------------------------------------
Retrieving user conversation history.
Successfully retrieved user conversation history.
Retrieving AI conversation history.
Successfully retrieved AI conversation history.
Parsing conversation history
Conversation history parsing completed
Generating note ...
Note generation complete
Generating file name ...
The file name is generated, and the file name is xxxxx
Note has been saved to xxxx.md file
--------------------------------------------------end--------------------------------------------------
