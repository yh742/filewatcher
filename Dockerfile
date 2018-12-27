FROM python:2.7.15-alpine3.8
EXPOSE 5000
VOLUME ["/usr/src/app/outputs"]
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirement.txt
CMD ["flask", "run", "--host", "0.0.0.0"]