from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Генерация случайного арифметического примера
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    example = f"{num1} {operator} {num2}"
    answer = eval(example)
    
    return render_template("index.html", example=example, answer=answer)

if __name__ == '__main__':
    app.run(port=5000)
