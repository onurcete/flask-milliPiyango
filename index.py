from flask import Flask, render_template,request
import milliPiyango,getDates

app = Flask(__name__)

@app.route("/")
def anaSayfa():
    dates = getDates.getDates()
    return render_template("index.html",sayfabasligi="Ana Sayfa",items=dates)

@app.route("/result",methods=['POST'])
def result():
    x=str(request.form['kuponNo'])
    y=str(request.form['tarihNo'])
    mgm = milliPiyango.conn(x,y)
    return render_template("result.html",sayfabasligi="Çekiliş Sonucu",kuponNo = mgm[0],ikramiye = mgm[1])

if __name__ == "__main__":
    app.run(debug=True) 
