echo "Cloning Repo...."
git clone https://github.com/aarohaop/shortner /shortner
cd /shortner
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
