
source .venv/bin/activate

./ngrok http 5000

# run app
python app.python

# copy files to S3 bucket after processing
aws s3 cp files s3://angry-pup --recursive

# encode into ALexa mp3 format and double volume
fmpeg-3.4.2-32bit-static/ffmpeg -y -i bark_twice2.mp3 -ar 16000 -ab 48k -codec:a libmp3lame -ac 1 -filter:a "volume=2"  files/bark_twice2_16000.mp3

# lambda URL
https://uqk9dp54p4.execute-api.us-east-1.amazonaws.com/prod

