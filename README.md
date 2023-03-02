# Telegram mailing script
This is a script for sending text to groups

# How to run
1. Run this commands:
```shell
git clone https://github.com/Kitazuka/telethon_test_task.git
python -m venv venv
venv\Scripts\activate # on Windows
source venv/bin/activate # on macOS
pip install -r requirements.txt
```
2. You need to create .env file (you can see an example in .env.sample)
3. Create `Groups.txt` file with groups id inside
4. Run
```shell
python main.py
```
