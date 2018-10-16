import pymysql
from app import app
from tables import Results
from db_config import mysql
from flask import flash, render_template, request, redirect
from werkzeug import generate_password_hash, check_password_hash

'''
CREATE TABLE `bse` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
   symbol varchar(50),date varchar(15),high varchar(10),low varchar(10),volume varchar(10),open varchar(10),close varchar(10),
   PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
'''

@app.route('/new_user')
def add_user_view():
	return render_template('add.html')
		
@app.route('/add', methods=['POST'])
def add_user():
	try:		
		#_name = request.form['inputName']
		#_email = request.form['inputEmail']
		#_password = request.form['inputPassword']
		_symbol=request.form['inputsymbol']
		_date=request.form['inputdate']
		_high=request.form['inputhigh']
		_low=request.form['inputlow']
		_volume=request.form['inputvolume']
		_open=request.form['inputopen']
		_close=request.form['inputclose']

		# validate the received values
		if _symbol and _date and _high and _low and _volume and _open and _close and request.method == 'POST':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO bse(symbol,date,high,low,volume,open,close) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			#data = (_name, _email, _hashed_password,)
			data=(_symbol,_date,_high,_low,_volume,_open,_close)			
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Data added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM bse")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/edit/<int:id>')
def edit_view(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM bse WHERE user_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/update', methods=['POST'])
def update_user():
	try:		
		#_name = request.form['inputName']
		#_email = request.form['inputEmail']
		#_password = request.form['inputPassword']
		_symbol=request.form['inputsymbol']
		_date=request.form['inputdate']
		_high=request.form['inputhigh']
		_low=request.form['inputlow']
		_volume=request.form['inputvolume']
		_open=request.form['inputopen']
		_close=request.form['inputclose']


		_id = request.form['id']


		# validate the received values
		if _symbol and _date and _high and _low and _volume and _open and _close and _id and request.method == 'POST':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "UPDATE bse SET symbol=%s,date=%s,high=%s,low=%s,volume=%s,open=%s,close=%s, WHERE user_id=%s"
			data = (_symbol,_date,_high,_low,_volume,_open,_close, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('BSE details updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>')
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM bse WHERE user_id=%s", (id,))
		conn.commit()
		flash('BSE deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
if __name__ == "__main__":
    app.run()
