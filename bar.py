from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_value = float(request.form['input_value'])
        max_value = float(request.form['max_value'])
        if input_value > max_value:
            error = 'Input value cannot be greater than the max value'
            return render_template('index.html', error=error)
        progress = input_value / max_value
        data = [progress, 1-progress]
        labels = ['Progress', 'Remaining']
        fig, ax = plt.subplots()
        ax.pie(data, labels=labels)
        ax.set_title('Progress Pie Chart')
        plt.savefig('static/chart.png')
        return render_template('index.html', progress=progress)
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)