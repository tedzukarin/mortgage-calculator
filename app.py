from flask import Flask, render_template, request

app = Flask(__name__)


# Главная страница (Telegram)
@app.route('/')
def index():
    return render_template('index.html')


# Страница для Max мессенджера
@app.route('/max')
def max_page():
    # Можно передать параметры, если нужно
    platform = request.args.get('platform', 'max')
    return render_template('max.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)