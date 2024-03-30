# Python VK API and Google Sheets API Clients.

## Overview

The project implements a Python client to interact with VK API and upload results to a spreadsheet via Google Sheets API.

The goal was to automate the collection of VK group statistics.

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

    - Initiates VK API and Google Sheets API clients
    - Loads and organizes VK stats data
    - Writes data to Google Sheet

## Structure

### app/.envs

Contains environment variables (templates) for VK API and Google Sheets API.

### app/configs

Contains Pydantic configuration settings for VK API and Google Sheets API.

### app/sheets

Contains Google Sheets API client that lets the user write and read data, including the authentication module, credentials.json and token.json.

### app/vk

Contains VK API client that lets the user write and read data, including: authentication module, Pydantic validation schemas, data mappers and httpx requests module.

