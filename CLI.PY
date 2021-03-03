echo -e 'if __name__ == "__main__":\n    print("Welcome to a Python script")' > script.py
python script.py

 virtualenv python2
 virtualenv -p /usr/bin/python3 python3

 source python3/bin/activate

 python -V
pip freeze

echo -e 'def print_message():\n    print("Hello from another file!")' > utils.py
echo -e 'import utils\n\nif __name__ == "__main__":\n    utils.print_message()' > script.py
python script.py

echo -e 'import sys\n\nif __name__ == "__main__":\n    print(sys.argv[1])' > script.py
python script.py "Hello from the command line"

deactivate

cd ..
cd ~
pwd

virtualenv -p /usr/bin/python3 script
source script/bin/activate

mkdir printer
mv script.py printer

cd printer
python script.py "I'm so good at challenges!"

echo '99 bottles of beer on the wall...' > beer.txt
echo 'Take one down, pass it around, 98 bottles of beer on the wall...' >> beer.txt

sort -r < beer.txt

echo 'Coffee is almost as good as beer,\nBut I could never drink 99 bottles of it' > coffee.txt
grep "bottles of" beer.txt coffee.txt

touch beer1.txt
touch beer2.txt
grep "beer" beer?.txt

grep "beer" *.txt

echo -e "import random\nfor i in range(100):\n    print(random.randint(1,10))\n" > rand.py
python rand.py | grep 9

echo "All the beers are gone" >> beer.txt && cat beer.txt

echo "\"Get out of here,\" said Neil Armstrong to the moon people." >> famous_quotes.txt



head Hud_2005.csv
head Hud_2007.csv
head Hud_2013.csv
head -1 Hud_2005.csv > combined_hud.csv
wc -l Hud_2005.csv
tail -46853 Hud_2005.csv >> combined_hud.csv
head combined_hud.csv
wc -l Hud_2007.csv
tail -42729 Hud_2007.csv >> combined_hud.csv
wc -l Hud_2013.csv
tail -64535 Hud_2013.csv >> combined_hud.csv
grep '1980-1989' combined_hud.csv | wc -l



ls -l
csvstack -n year -g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.csv > Combined_hud.csv
head -5 Combined_hud.csv
head -10 Combined_hud.csv | csvlook
csvcut -n Combined_hud.csv
csvcut -c 2 Combined_hud.csv | head -10
csvstat --mean Combined_hud.csv
csvcut -n Combined_hud.csv
csvcut -c 2 Combined_hud.csv | csvstat
csvgrep -c 2 -m -9 Combined_hud.csv | head -10 | csvlook
csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv
