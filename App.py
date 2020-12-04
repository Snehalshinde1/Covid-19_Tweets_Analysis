from flask import Flask,render_template,request, flash
from top_followers import date_range,top_followers
from pie_chart import percentage
import imp_var
from wtforms import DateField
from flask_wtf import Form
import os

application_path = os.getcwd()


import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456"

global f1
@app.route("/", methods=["GET" ,"POST"])
def home():
    return render_template("index.html")


@app.route("/covid_analysis", methods=["GET" ,"POST"])
def covid_analysis():
    return render_template("covid_analysis.html")

@app.route("/upload_data", methods=["GET" ,"POST"])
def upload_data():
    global f1
    if request.method=="POST":


            current_directory = application_path + "/" + "Uploads"
            f = request.files.get('files[]')
            # print(f,"@@@@@@@@@@@@@@@@@")
            # print(f.filename)
            # imp_var.upload_status = "upload"
            f1 = os.path.join(current_directory, f.filename)
            f.save(f1)
            flash('Upload Success!!!')
            return render_template("upload.html")

    else:

        return render_template("upload.html")




@app.route("/covid",methods=["GET","POST"])
def covid():

    if request.method=="POST":
        sd=request.form["Start_date"]
        ed=request.form["End_date"]
        start_date = sd.split('-')
        start_date = start_date[1]+'/'+start_date[2]+'/'+start_date[0]
        end_date = ed.split('-')
        end_date = end_date[1] + '/' + end_date[2] + '/' + end_date[0]

        filtered_dates = date_range(start_date,end_date,f1)
        user_names, user_followers = top_followers(filtered_dates,5)
        labels = user_names
        values = user_followers
        legend = 'User follower Data'
        hashtags, hashtags_count = percentage(filtered_dates)
        return render_template('covid_analysis.html', values=values,  labels=labels, legend=legend,
                            pie_legend="Hashtags Pie chart", hashtags=hashtags, hashtags_count=hashtags_count)
    else:
        return render_template("covid_analysis.html")


if __name__ == "__main__":
    app.run(port=8000)

