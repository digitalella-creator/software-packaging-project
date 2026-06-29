# Software Packaging Project

## Overview

This project demonstrates software packaging using Python and Flask. It includes dependency management, environment-specific configuration, semantic versioning, package creation, testing, security auditing, and artifact integrity verification.

## Project Version

**Version:** 1.0.0

Semantic Versioning:

* MAJOR – Breaking changes
* MINOR – New features
* PATCH – Bug fixes

## Dependencies

* Flask 3.0.3
* requests 2.32.3

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## Running Unit Tests

```bash
python -m pytest
```

Expected Result:

```
1 passed
```

## Building the Package

```bash
python -m build
```

Generated artifacts:

* `dist/software_packaging_project-1.0.0.tar.gz`
* `dist/software_packaging_project-1.0.0-py3-none-any.whl`

## Environment Configuration

Development:

```bash
set ENVIRONMENT=development
```

Staging:

```bash
set ENVIRONMENT=staging
```

## Security Audit

```bash
python -m pip_audit
```

Result:

No known vulnerabilities found.

## Integrity Verification (SHA256)

Source Distribution (.tar.gz)

```
837f0d3ee96daaa83adbf9978494d802dbe171ba69c1ff53b04c7c075820a62e
```

Wheel (.whl)

```
485f519f9a04e76fde82a22791227ba6d9758c1bf90af75866ab2fa8e958ddd9
```

## Release

Git Tag:

```
v1.0.0
```

## Author

Emmanuela
