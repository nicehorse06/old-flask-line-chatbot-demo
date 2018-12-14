本專案為 line python(Flask) bot 的 demo

## Line 資料參考網站
* [Line console message API](https://developers.line.me/en/)

* [Line python bot sdk](https://github.com/line/line-bot-sdk-python)


## line bot 流程
1. 執行 Flask
2. 執行 ngrok
3. 把 ngrok https 網址貼到 Line console

## Flask

* 執行flask `python main.py`

* [Flask官網](http://flask.pocoo.org/)


## ngrok 

ngrok 把本地server給外部連
```
./ngrok http 5000
```

## Heroku

* [Heroku部署參考網站](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)

* 推送到 Heroku 執行 `git push heroku master`

## 其他參考的API

[Star War API](https://swapi.co/)