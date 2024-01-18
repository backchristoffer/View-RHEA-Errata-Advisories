# Red Hat RHEA Errata Advisory Script

## Overview

This Python script retrieves Red Hat RHEA Errata advisories and prints relevant information in a formatted manner. It uses the Red Hat Management API to fetch advisories and display details such as Advisory ID, Type, Synopsis, Publish Date, Affected System Count, Details, and Systems.

## Prerequisites

Before using the script, ensure you have the following:

- Python 3.x installed
- Red Hat account and access to https://access.redhat.com/management/api
- Offline token generated from https://access.redhat.com/management/api

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

3. Create a `.env` file with your Red Hat API offline token (Token can be generated https://access.redhat.com/management/api):

    ```
    OFFTOKEN=your_red_hat_offline_token
    ```

## Usage

Run the script using the following command:

```bash
pipenv run python app.py
```

Run as contaimer:
```bash
podman run -e OFFTOKEN="<YOUR GENERATED TOKEN>" ghcr.io/backchristoffer/rhea-errata:latest
```


Example output:

```bash
Advisory ID: RHEA-2023:2164
Type: Product Enhancement Advisory
Synopsis: rpm-ostree bug fix and enhancement update
Publish Date: 2023-05-09 05:02:07 UTC
Details: https://api.access.redhat.com/management/v1/errata/RHEA-2023:2164

--------------------------------------------------

Advisory ID: RHEA-2023:2187
Type: Product Enhancement Advisory
Synopsis: ostree bug fix and enhancement update
Publish Date: 2023-05-09 05:03:04 UTC
Details: https://api.access.redhat.com/management/v1/errata/RHEA-2023:2187
```
