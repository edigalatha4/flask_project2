from flask import Flask,render_template

AI=Flask(__name__)


@AI.route('/wish/<na>')
def wish(na):
    return f'Hello Good Morning{na}'



@AI.route('/first')
def first():
    return render_template('first.html',name='Joshi',age=2)


if __name__=='__main__':
    AI.run(debug=True)