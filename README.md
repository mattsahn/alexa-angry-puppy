# AngryPuppy Alexa Skill
<p align="center">
  <img src="https://images-na.ssl-images-amazon.com/images/I/615caIrH+EL.png" alt="AngryPuppy"/>
</p>

Published Alexa skill here:
https://www.amazon.com/dp/B079WMKZCY/

# Environment setup
source .venv/bin/activate

# Use ngrok for development to get https endpoint to pass to Alexa to connect to localhost
./ngrok http 5000

# run app
python app.python

# encode into ALexa mp3 format and double volume
fmpeg-3.4.2-32bit-static/ffmpeg -y -i bark_twice2.mp3 -ar 16000 -ab 48k -codec:a libmp3lame -ac 1 -filter:a "volume=2"  files/bark_twice2_16000.mp3

# copy files to S3 bucket after processing
aws s3 cp files s3://angry-pup --recursive

# Zappa command to deploy
zappa prod update

# lambda URL - created by zappa
https://uqk9dp54p4.execute-api.us-east-1.amazonaws.com/prod

