from flask import*
import mysql.connector

data=mysql.connector.connect(host="bwpdytoqstxaoloa7qo1-mysql.services.clever-cloud.com",password="OKv7b1ieip4jHAmq97Cn",user="u7fmqovuckzt7ing",database="bwpdytoqstxaoloa7qo1")
cur=data.cursor()

app=Flask(__name__)
app.secret_key="@navpreetsingh1127"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Skills")
def skills():
    return render_template("skills.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/contact",methods=["POST","GET"])
def form():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]

        try:
            cur.execute("insert into users (name,email,message) values(%s,%s,%s)",(name,email,message,))
            data.commit()
            return render_template("done.html")
    
        except Exception as e:
            return f"{e} having an error here.you can contact me via my email:ns6685509@gmail.com"
        

        
    return render_template("form.html")

#if __name__=="__main__":
   # app.run(debug=True,host="0.0.0.0",port="1127")
