import PySimpleGUI as PySG
from datetime import datetime as dt2
import datetime as dt
import pytz
import calendar as cal


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

    current_utc_date = current_utc_datetime.date()
    current_utc_year = current_utc_datetime.year
    current_utc_hour = current_utc_datetime.hour
    current_utc_minute = current_utc_datetime.minute

    utc_cal = cal.Calendar(firstweekday=cal.SUNDAY)
    mar_cal = utc_cal.monthdatescalendar(current_utc_year, 3)
    nov_cal = utc_cal.monthdatescalendar(current_utc_year, 11)

    mar_second_sunday = [day for week in mar_cal for day in week if
                         day.weekday() == cal.SUNDAY and
                         day.month == 3][1]
    nov_first_sunday = [day for week in nov_cal for day in week if
                        day.weekday() == cal.SUNDAY and
                        day.month == 11][0]

    if current_utc_date < mar_second_sunday:
        ct_utc_offset = -6
        et_utc_offset = -5
    elif current_utc_date == mar_second_sunday:
        if current_utc_hour < 7:
            ct_utc_offset = -6
            et_utc_offset = -5
        if 7 <= current_utc_hour < 8:
            ct_utc_offset = -6
            et_utc_offset = -4
        else:
            ct_utc_offset = -5
            et_utc_offset = -4
    elif mar_second_sunday < current_utc_date < nov_first_sunday:
        ct_utc_offset = -5
        et_utc_offset = -4
    elif current_utc_date == nov_first_sunday:
        if current_utc_hour < 6:
            ct_utc_offset = -5
            et_utc_offset = -4
        if 6 <= current_utc_hour < 7:
            ct_utc_offset = -5
            et_utc_offset = -5
        else:
            ct_utc_offset = -6
            et_utc_offset = -5
    else:  # nov_first_sunday < current_utc_date
        ct_utc_offset = -6
        et_utc_offset = -5

    if current_utc_hour + ct_utc_offset < 0:
        current_ct_hour = current_utc_hour + ct_utc_offset + 24
    else:
        current_ct_hour = current_utc_hour + ct_utc_offset

    if current_utc_hour + et_utc_offset < 0:
        current_et_hour = current_utc_hour + et_utc_offset + 24
    else:
        current_et_hour = current_utc_hour + et_utc_offset

    window["hour_home"].update(value=str(current_ct_hour))
    window["hour_work"].update(value=str(current_et_hour))
    window["minutes"].update(value=f": {str(current_utc_minute)}")

window.close()
