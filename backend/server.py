
# Import flask and datetime module for showing date and time
from flask import Flask, request
from flask_cors import CORS, cross_origin
import convert

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=["GET"])
# @cross_origin(origin='*')
def calculate():
    args = request.args
    string = args.get('str')
    print(string)
    infix = convert.to_infix(string)
    postfix = convert.to_postfix(infix)
    result = convert.to_result(postfix)

    response = {'result': result}
    return response

# Running app
if __name__ == '__main__':

    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)

    app.run()

    # app.run(debug=True)