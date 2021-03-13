from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
task=[]
complete=[]
@app.route("/")
@app.route("/index/")
def index():
	return render_template("todo.html",task=task,complete=complete)
@app.route("/addtask/",methods=['POST'])
def newtask():
	newtask=request.form['newtask']
	task.append(newtask)
	print(task)
	return redirect(url_for('index'))
@app.route("/removetask/",methods=['GET'])
def removetask():
	num=int(request.args.get('completetask'))
	completetask=task[num]
	complete.append(completetask)
	task.pop(num)
	print(task)
	print(complete)
	return redirect(url_for('index'))
@app.route("/deltask/",methods=['GET'])
def deltask():
	num=int(request.args.get('deltask'))
	task.pop(num)
	return redirect(url_for('index'))
@app.route("/delcom/",methods=['GET'])
def delcom():
	num=int(request.args.get("delet"))
	complete.pop(num)
	return redirect(url_for('index'))
@app.route("/restore/",methods=['GET'])
def restore():
	num=int(request.args.get("back"))
	back=complete[num]
	print(back)
	task.append(back)
	complete.pop(num)
	return redirect(url_for('index'))
if __name__=='__main__':
	app.run('localhost',8080,debug=True)