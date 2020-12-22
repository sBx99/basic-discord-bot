# file to build discord bot from scratch using a Dockerfile or just this run.sh file

# build bot in your command line from scratch
python -m venv my_env
source my_env/bin/activate
pip install --no-cache-dir -r requirements.txt
touch .env
cp env.example .env
rm env.example
# open the .env file and add your discord credentials
python bot.py


# build bot using docker
docker build -t meme-bot .
docker run -it meme-bot