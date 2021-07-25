from flask import Flask,render_template
import  sqlite3
app = Flask(__name__)

#测试页
@app.route('/test')
def test():
    return render_template("temp.html")

#首页
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
   return home()
#电影
@app.route('/movie')
def movie():
    datalist=[]#列表存储电影
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()


    return render_template("movie.html",movies=datalist)

#评分
@app.route('/score')
def score():
    score=[]#评分
    number=[]#部数
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    sql="select score,count(score) from movie250 group by score"
    data=cur.execute(sql)
    for item in data:
        score.append(item[0])
        number.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score,number=number)

#词云
@app.route('/word')
def word():
    return render_template("word.html")

#团队
@app.route('/team')
def team():
    return render_template("team.html")

#连接数据库
# def askDB():
#     datalist=[]#列表存储电影
#     con=sqlite3.connect("movie.db")
#     cur=con.cursor()
#     sql="select * from movie250"
#     data=cur.execute(sql)
#     for item in data:
#         datalist.append(item)
#     cur.close()
#     con.close()
#     return datalist

if __name__ == '__main__':
    app.run()
