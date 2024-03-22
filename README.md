# mlops-creditcard-approval-model

This repository contains a data science project that calculates the accuracy and fairness of an ML model used to approve or deny credit card applications for a fictional bank.

## Command to run the test against a container image previously built

RUN pytest --nbval-lax credit_card_approval.ipynb --junitxml=report.xml
