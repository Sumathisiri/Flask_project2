from flask import Flask 

FAI=Flask(__name__)

@FAI.route('/wish/<na>')
def wish(na):
    return f' <h1>Hello How r u {na}</h1>'

if __name__=='__main__':
    FAI.run(debug=True)