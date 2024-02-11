# Python Interface for VK API.

## Overview

The project implements a Python interface to interact with VK API and upload results to a spreadsheet via Google Sheets API.

## Technologies

    - VK API
    - Google Sheets API
    - Pydantic
    - httpx
    - asyncio

## Installation

```bash
pip install -r requirements.txt
```

## Launch

```bash
python app
```

app/__main__.py implements a basic example that:

    - Initiates VK API and Google Sheets API interfaces
    - Loads and organizes VK stats data
    - Writes data to Google Sheet

## Structure

### app/.envs

Contains environment variables (templates) for VK API and Google Sheets API.

### app/api

Contains SCQlAlchemy and FastAPI backend API for database operations (IN PROGRESS).

### app/configs

Contains Pydantic configuration settings for VK API and Google Sheets API.

### app/sheets

Contains Google Sheets API interface that lets the user write and read data, including the authentication module, credentials.json and token.json.

### app/vk

Contains VK API interface that lets the user write and read data, including: Pydantic validation schemas, data mappers and httpx requests module.

