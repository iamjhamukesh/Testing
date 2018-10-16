from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    user_symbol = Col('Symbol')
    user_date = Col('Date')
    user_high = Col('High')
    user_low = Col('Low')
    user_volume = Col('Volume')
    user_open = Col('Open')
    user_close = Col('Close')
    #user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))
