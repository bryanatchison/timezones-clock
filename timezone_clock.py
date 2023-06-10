import PySimpleGUI as PySG
import calendar as cal
from datetime import datetime as dt2
import datetime as dt

current_utc_time = \
    dt2.isoformat(dt2.now().astimezone(dt.timezone(dt.timedelta(0))))

c = cal.Calendar(firstweekday=cal.SUNDAY)

current_year = int(current_utc_time[:4])
current_month = int(current_utc_time[5:7])
current_day = int(current_utc_time[8:10])
current_hour = int(current_utc_time[11:13])

mar_cal = c.monthdatescalendar(current_year, 3)
nov_cal = c.monthdatescalendar(current_year, 11)
mar_second_sunday = [day for week in mar_cal for day in week if
                day.weekday() == cal.SUNDAY and
                day.month == 3][1]
nov_first_sunday = [day for week in nov_cal for day in week if
                day.weekday() == cal.SUNDAY and
                day.month == 11][0]

if current_month >= 3:
    dst_flag = False
elif current_month == 3:
    if
elif current_month = 12:
    dst_flag = False

else:
    False

edt_utc_offset = -4
est_utc_offset = -5
cdt_utc_offset = -5
cst_utc_offset = -6

if int(current_utc_time[5:7]) >= 3 and int(current_utc_time[5:7]) >= 3:
    dst_month = True
else:
    dst_month = False


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
                       font=('Helvetica', 15))
minutes = PySG.Text('', key='minutes',
                    # size=(5, 1),
                    font=('Helvetica', 60))
label_work = PySG.Text("Work",
                       # size=(10, 1),
                       font=('Helvetica', 15))
dst_no_selector = PySG.Radio("Standard Time", key='dst_no', group_id="dst_selection",
                             default=not dst_month)
dst_yes_selector = PySG.Radio("Daylight Saving", key='dst_yes', group_id="dst_selection",
                              default=dst_month)
exit_button = PySG.Button("Exit", size=11,
                          font=('Helvetica', 15))

left_column_content = [[hour_home],
                       [hour_work]]
middle_column_content = [[label_home],
                         [minutes],
                         [label_work]]
right_column_content = [[dst_no_selector],
                        [dst_yes_selector],
                        [exit_button]]

left_column = PySG.Column(left_column_content)
middle_column = PySG.Column(middle_column_content)
right_column = PySG.Column(right_column_content)

window = PySG.Window('Timezone Clock',
                     layout=[  # [top_bar],
                           [left_column, middle_column, right_column]])

while True:
    event, values = window.read(timeout=200)
    match event:
        case PySG.WIN_CLOSED:
            break
        case "Exit":
            break
    if values['dst_no']:
        central_utc_offset = cst_utc_offset
        eastern_utc_offset = est_utc_offset
    elif values['dst_yes']:
        central_utc_offset = cdt_utc_offset
        eastern_utc_offset = edt_utc_offset
    else:
        central_utc_offset = cst_utc_offset
        eastern_utc_offset = est_utc_offset

    current_central_time = \
        dt2.isoformat(dt2.now()
                      .astimezone(dt.timezone(dt.timedelta(hours=central_utc_offset))))
    current_eastern_time = \
        dt2.isoformat(dt2.now()
                      .astimezone(dt.timezone(dt.timedelta(hours=eastern_utc_offset))))
    current_utc_time = \
        dt2.isoformat(dt2.now()
                      .astimezone(dt.timezone(dt.timedelta(0))))
    window["hour_home"].update(value=current_central_time[11:13])
    window["hour_work"].update(value=current_eastern_time[11:13])
    window["minutes"].update(value=f": {current_utc_time[14:16]}")

window.close()
