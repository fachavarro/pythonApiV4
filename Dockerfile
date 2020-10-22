# Step 1 select default OS image
FROM alpine


# # Step 2 tell what you want to do
RUN apk add py3-pip
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip && pip3 install wheel


# # Step 3 Configure a software
# # Defining working directory
WORKDIR /app


# # Copy everything which is present in my docker directory to working (/app)
COPY /requirements.txt /app

RUN pip3 install -r requirements.txt

COPY ["./database/", "/app/"]
COPY ["resources/", "/app/"]
COPY ["service/", "/app/"]
COPY ["test/", "/app/"]
COPY ["config.properties", "/app"]
COPY ["app.py", "/app"]

# Exposing an internal port
EXPOSE 5001

# Step 4 set default commands
# These are permanent commands i.e even if user will provide come commands those will be considered as argunemts of this command
ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
CMD ["app.py"]
