# Python DevOps Health Checker

A small beginner-friendly project for a Software Engineer – Automation & DevOps internship.

## What it does

- Checks one or more URLs and reports their HTTP status.
- Returns a non-zero exit code if any URL is unhealthy, which is useful for automation.
- Includes automated unit tests.
- Uses GitHub Actions to run tests on every push and pull request.
- Includes a Dockerfile to package the checker in a container.

## Requirements

- Python 3.10+ (the CI pipeline uses Python 3.12)
- Optional: Docker
- A GitHub account to run the CI workflow

## Run locally

```bash
python app.py https://example.com
```

Check multiple endpoints:

```bash
python app.py https://example.com https://www.python.org
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Run with Docker

Build the image:

```bash
docker build -t python-health-checker .
```

Run it:

```bash
docker run --rm python-health-checker
```

The default container command checks `https://example.com`. To provide your own URL:

```bash
docker run --rm python-health-checker python app.py https://www.python.org
```

## Enable CI with GitHub Actions

1. Create a GitHub repository named `python-devops-health-checker`.
2. Upload/push all project files, including `.github/workflows/ci.yml`.
3. Open the **Actions** tab in GitHub.
4. Push a small change and confirm the `Python CI` workflow runs the tests.

## Architecture

```text
Code change
    |
    v
GitHub repository
    |
    v
GitHub Actions CI workflow
    |
    +--> Set up Python
    +--> Run unit tests
    +--> Check syntax
    |
    v
Pass / fail result
```

## What to explain in an interview

- **Monitoring:** the script checks whether a URL responds successfully.
- **Exit codes:** `0` means all checks passed; `1` means at least one check failed; `2` means usage was incorrect.
- **Testing:** unit tests mock network calls, so tests do not depend on a real website.
- **CI:** GitHub Actions automatically runs tests when code is pushed or a pull request is opened.
- **Docker:** the Dockerfile packages the program and runs it as a non-root user.

## Honest project status

This is a starter project. Before claiming it on a resume, run the tests locally, push it to your own GitHub account, and verify that the Actions workflow passes. The Docker steps are optional until you install Docker and test them.
