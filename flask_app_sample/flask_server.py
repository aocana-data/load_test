from flask import * 
import os

app = Flask(__name__)



@app.route("/",methods=['GET'])
def pingTester():
    with open('./flask_app_sample/counter.txt','r',encoding='utf-8') as counter:
        count = int(counter.read())
        count += 1

    with open('./flask_app_sample/counter.txt','w',encoding='utf-8') as counter:
        counter.write(str(count))
    print(f'requests {count}')
    return f'requests {count}'


if __name__ == "__main__":
    app.run(port=5000)