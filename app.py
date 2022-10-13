from crypt import methods
from urllib import request
from flask import Flask, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    app.logger.info("this log portrays a message about sth")
    app.logger.debug("this log provides a diagnostic information")
    app.logger.error("this log represents a failure of the code")
    app.logger.warning("this log indicates that there might be a problem")
    app.logger.fatal("this log represents catastrophic situations")
    

    if request.method =='POST':
      app.logger.info("the request method was a post")

      task_content=request.form['content']
      new_task=Todo(content=task_content)

      try:
          db.session.add(new_task)
          db.session.commit()
          return redirect('/')
      except:
        return 'There was an issue adding your task'    
    else:
        app.logger.info("the request method was %s",request.method)

        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks) 


@app.route('/delete/<int:id>')
def delete(id):
    app.logger.info("About to delete record with id %s",id)
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    app.logger.info("About to update record with id %s",id )
    task = Todo.query.get_or_404(id)

    if request.method =='POST':
        task.content = request.form['content']
        app.logger.info("about to update record with content %s",task.content)
        

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue updating your task"

    else:
        return render_template('update.html', task=task )
if __name__ == "__main__":
    app.run(debug=True) 

  