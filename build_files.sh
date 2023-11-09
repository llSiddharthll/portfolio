echo "BUILD START"
python3.9 -m pip3 install --upgrade pip3
pip3 install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "BUILD DONE"