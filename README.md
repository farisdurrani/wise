# wise
Ask and we give you wise quotes from your own books.

# Frontend
## Prerequisites
- [Node.js v18](https://nodejs.org/en/)

## How to start
```
cd frontend
npm install
npm start
```
Open the app at http://localhost:3000

# Backend
## Prerequisites
- [Python 3.10+](https://www.python.org/downloads/)

## How to start
```
cd backend
pip install -r requirements.txt
python app.py
```
Open the app at http://localhost:8000

### If the above doesn't work try this:
```
python3 -m nltk.downloader wordnet
```
On Windows cd into your 'nltk_data' directory and run 
```
python -m nltk.downloader all
```
Now try running python app.py again and hopfully it should work this time.


## If you are experiencing any issues feel free to reference these links:
https://www.nltk.org/data.html
