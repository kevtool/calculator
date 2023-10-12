
# Import flask and datetime module for showing date and time
from flask import Flask, request
import datetime
import convert
  
# Initializing flask app
app = Flask(__name__)

@app.route('/calculate', methods=["GET"])
def calculate():
    args = request.args
    string = args.get('str')
    print(string)
    infix = convert.to_infix(string)
    postfix = convert.to_postfix(infix)
    result = convert.to_result(postfix)

    return {
        'result': result
    }
     
# Running app
if __name__ == '__main__': 
    
    # app.run(debug=True)
    app.run()
    # app.run(host='0.0.0.0', port=5000)