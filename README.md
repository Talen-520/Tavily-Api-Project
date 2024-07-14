# Tavily-Api-Project

### Project Showcase

https://github.com/user-attachments/assets/f5c2730f-7ec8-4c03-9bfb-599b58a5d577


### Getting Start

1. clone this repository
```
https://github.com/Talen-520/Tavily-Api-Project.git
```

2. active virtual environment
```
Tavily\Scripts\activate
cd Demo
```

3. start backend server
```
python manage.py runserver
```

4. Open another terminal

5. go to your frontend directory
```
cd Newsapp
npm run dev
```

app will live at http://localhost:5173/


## about project step by step setup process[optional]

### install vitrual environment
```
python -m venv <environment_name>
```
### active vitrual environment
```
<environment_name>\Scripts\activate
```
### install packages
```
pip install --upgrade openai python-dotenv --upgrade tiktoken tavily-python django djangorestframework django-cors-headers
```

### start your demo project
```
django-admin startproject <projectname>
cd <projectname>
```
### start your app 
```
python manage.py startapp <appname>
```

### dotenv key setup
```
OPENAI_API_KEY=yourkey
TAVILYKEY_API_KEY=yourkey
```
###  start your backend django application
```
python manage.py runserver
```
### frontend setup
```
npm create vite@latest <projectname>
> react
> Typescript

cd Newsapp
npm install axios
```
### run app
```
npm run dev
```
