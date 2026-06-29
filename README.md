# Software Packaging Project

## Overview

This project demonstrates software packaging using Python and Flask. It shows how to manage dependencies, configure different environments, apply semantic versioning, and package an application for deployment.

## Dependencies

The project uses the following Python packages:

- Flask==3.0.3
- requests==2.32.3

## Installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application by running:

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

## Semantic Version

Current Version: **1.0.0**

This project follows Semantic Versioning:

- MAJOR = Breaking changes
- MINOR = New features
- PATCH = Bug fixes

## Environment Configuration

Development environment:

```bash
set ENVIRONMENT=development
```

Staging environment:

```bash
set ENVIRONMENT=staging
```

## Security Audit

Run the following command to check for dependency vulnerabilities:

```bash
pip-audit
```

## Author

Emmanuela