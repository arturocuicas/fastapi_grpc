FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/kitchen
COPY ./pyproject.toml ./poetry.lock* ./

RUN pip install poetry
RUN poetry install

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r /home/kitchen/requirements.txt

EXPOSE 50053
CMD [ "python", "main.py" ]