from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    symbol = Col('Symbol')
    date1 = Col('Date')
    high = Col('High')
    low = Col('Low')
    volume = Col('Volume')
    open = Col('Open')
    close = Col('Close')
    #user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))
