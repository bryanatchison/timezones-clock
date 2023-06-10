import PySimpleGUI as PySG
from datetime import datetime as dt2
import pytz


PySG.theme("DarkBlue13")
"""
top_bar = sg.Titlebar(title="Timezone Clock",
                      icon=None,
                      text_color=None,
                      background_color=None,
                      font=('Helvetica', 15),
                      key='title')
"""
hour_home = PySG.Text('', key='hour_home',
                      # size=(5, 1),
                      font=('Helvetica', 60))
hour_work = PySG.Text('', key='hour_work',
                      # size=(5, 1),
                      font=('Helvetica', 60))
label_home = PySG.Text("Home",
                       # size=(10, 1),
                       font=('Helvetica', 18))
minutes = PySG.Text('', key='minutes',
                    # size=(5, 1),
                    font=('Helvetica', 60))
label_work = PySG.Text("Work",
                       # size=(10, 1),
                       font=('Helvetica', 18))
exit_button = PySG.Button("Exit",
                          font=('Helvetica', 15))

left_column_content = [[hour_home],
                       [hour_work]]
middle_column_content = [[label_home],
                         [minutes],
                         [label_work]]
right_column_content = [[exit_button]]

left_column = PySG.Column(left_column_content)
middle_column = PySG.Column(middle_column_content)
right_column = PySG.Column(right_column_content)

window = PySG.Window('Timezone Clock',
                     layout=[  # [top_bar],
                           [left_column, middle_column, right_column]])

while True:
    event, values = window.read(timeout=500)
    match event:
        case PySG.WIN_CLOSED:
            break
        case "Exit":
            break

    current_utc_datetime = dt2.now(pytz.utc)
    current_us_ct_datetime = dt2.now(pytz.utc).astimezone(pytz.timezone('US/Central'))
    current_us_et_datetime = dt2.now(pytz.utc).astimezone(pytz.timezone('America/New_York'))

    window["hour_home"].update(value=str(current_us_ct_datetime.hour))
    window["hour_work"].update(value=str(current_us_et_datetime.hour))
    window["minutes"].update(value=f": {('0' + str(current_utc_datetime.minute))[:2]}")

window.close()
