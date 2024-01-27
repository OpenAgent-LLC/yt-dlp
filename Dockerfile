FROM public.ecr.aws/lambda/python:3.12

ARG YTDL_INFO_ONLY=1

# Copy function code and requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.
RUN pip install -r requirements.txt

COPY . ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "index.handler" ]