FROM python:2.7

# set working directory
#RUN mkdir -p /src
COPY . /src
WORKDIR /src

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /src/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
#ADD . /src

# run server
CMD python manage.py runserver 0.0.0.0:8000
