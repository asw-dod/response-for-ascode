FROM python:3.12.3

LABEL org.opencontainers.image.source=https://github.com/asw-dod/response-for-ascode
LABEL org.opencontainers.image.licenses=MIT
LABEL org.opencontainers.image.authors="JooHyoung Cha"
LABEL org.opencontainers.image.description="automatic response program for Compile Error in ascode. but only administrator account use this program."

WORKDIR /app

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

ENV DISPLAY=:99
ENV ASCODE_USERID=
ENV ASCODE_USERPW=
ENV DURATION_PER_CHECK=

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "./main.py"]


