git init
echo -e "Random number generator" > README.md
echo -e 'if __name__ == "__main__":\n    print("10")' > script.py
git status
git add script.py
git add README.md
git config --global user.email "user@dataquest.io"
git config --global user.name "Dataquest User"
git commit -m "Initial commit.  Added script.py and README.md"
echo -e 'import random\nif __name__ == "__main__":\n    print(random.randint(0,10))' > script.py
git status
git commit -m "Made the numbers random"
git log
git log --stat
git clone /dataquest/user/git/chatbot
cd /home/dq/chatbot
printf "This project needs no installation" >> README.md
git add README.md
git commit -m "Updated README.md"
git status
git branch
git push origin master
HASH=`git rev-parse HEAD`
git show $HASH -q
HASH=`git rev-parse HEAD`
HASH2=`git rev-parse HEAD~1`
git --no-pager diff $HASH2 $HASH
HASH=`git rev-list --max-parents=0 HEAD`
git reset --hard $HASH
git pull
git reset --hard HEAD~1
git clone /dataquest/user/git/chatbot
cd chatbot
git checkout -b more-speech
git checkout more-speech
printf "\nprint('Kind of dull in here, right?')" >> bot.py
git add bot.py
git commit -m "Added more output"
git push origin more-speech
git checkout master
git merge more-speech
git push origin master
git branch -d more-speech
cd /home/dq
git clone /dataquest/user/git/chatbot chatbot2
cd chatbot2
git checkout -b happy-bot
printf "\nprint('Happiness level: 120')" >> bot.py
git add bot.py
git commit -m "Made the bot 20% happier!"
git push origin happy-bot
cd /home/dq
cd chatbot
git fetch
git checkout happy-bot
python bot.py
git --no-pager diff master happy-bot
