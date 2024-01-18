# Red Hat Errata Advisory Script

## Overview

This Python script retrieves Red Hat Errata advisories and prints relevant information in a formatted manner. It uses the Red Hat Management API to fetch advisories and display details such as Advisory ID, Type, Synopsis, Publish Date, Affected System Count, Details, and Systems.

## Prerequisites

Before using the script, ensure you have the following:

- Python 3.x installed

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/backchristoffer/rhea-errata.git
    cd your-repository
    ```

2. Install dependencies:

    ```bash
    pipenv install
    ```

3. Create a `.env` file with your Red Hat API offline token:

    ```
    OFFTOKEN=your_red_hat_offline_token
    ```

## Usage

Run the script using the following command:

```bash
pipenv run python app.py
```
