FROM public.ecr.aws/lambda/python:3.10

# Copy requirements.txt
#COPY requirements.txt ${LAMBDA_TASK_ROOT}
# Copy function code
#COPY lambda_function.py ${LAMBDA_TASK_ROOT}


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the specified packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy function code
#COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Copy artifacts from S3?

# This needs to be triggered at the time of training and testing only not for deploying to lambda
# this will be triggered when either the Dockerfile or requirements is changed or ..
# when the PR commit message includes the keyword "train Notebooks/training_example.ipynb"
# RUN pytest --nbval-lax credit_card_approval.ipynb --junitxml=report.xml

## something on the pipeline side to put the artifacts in S3 including the model file



# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# this is needed for lambda, we will probably override it all the time except for deploying to lambda
# CMD [ "lambda_function.handler" ]
