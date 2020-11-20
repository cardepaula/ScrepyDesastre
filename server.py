import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Server Online'


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
