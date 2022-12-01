FROM python:3.10-buster

MAINTAINER Sam Kuttenkuler <https://github.com/skuttenkuler>

RUN mkdir /home/wealthandtaste

WORKDIR /home/wealthandtaste 

COPY ./ /home/wealthandtaste/

RUN pip install -r /home/wealthandtaste/requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]