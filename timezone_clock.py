import PySimpleGUI as sg
from datetime import datetime as dtdt
import datetime as dt

current_utc_time = \
    dtdt.isoformat(dtdt.now().astimezone(dt.timezone(dt.timedelta(0))))

edt_utc_offset = -4
est_utc_offset = -5
cdt_utc_offset = -5
cst_utc_offset = -6

if int(current_utc_time[5:7]) >= 3 and int(current_utc_time[5:7]) >= 3:
    dst_month = True
else:
    dst_month = False


sg.theme("DarkBlue13")
"""
top_bar = sg.Titlebar(title="Timezone Clock",
                      icon=None,
                      text_color=None,
                      background_color=None,
                      font=('Helvetica', 15),
                      key='title')
"""
hour_home = sg.Text('', key='hour_home',
                    # size=(5, 1),
                    font=('Helvetica', 60))
hour_work = sg.Text('', key='hour_work',
                    # size=(5, 1),
                    font=('Helvetica', 60))
label_home = sg.Text("Home",
                     # size=(10, 1),
                     font=('Helvetica', 15))
minutes = sg.Text('', key='minutes',
                  # size=(5, 1),
                  font=('Helvetica', 60))
label_work = sg.Text("Work",
                     # size=(10, 1),
                     font=('Helvetica', 15))
dst_no_selector = sg.Radio("Standard", key='dst_no', group_id="dst_selection",
                           default=not dst_month)
dst_yes_selector = sg.Radio("Daylight Savings", key='dst_yes', group_id="dst_selection",
                            default=dst_month)
exit_button = sg.Button("Exit",  size=11,
                        font=('Helvetica', 15))

left_column_content = [[hour_home],
                       [hour_work]]
middle_column_content = [[label_home],
                         [minutes],
                         [label_work]]
right_column_content = [[dst_no_selector],
                        [dst_yes_selector],
                        [exit_button]]

left_column = sg.Column(left_column_content)
middle_column = sg.Column(middle_column_content)
right_column = sg.Column(right_column_content)

window = sg.Window('Timezone Clock',
                   layout=[  # [top_bar],
                           [left_column, middle_column, right_column]])

while True:
    event, values = window.read(timeout=1000)
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
        dtdt.isoformat(dtdt.now()
                       .astimezone(dt.timezone(dt.timedelta(hours=central_utc_offset))))
    current_eastern_time = \
        dtdt.isoformat(dtdt.now()
                       .astimezone(dt.timezone(dt.timedelta(hours=eastern_utc_offset))))
    current_utc_time = \
        dtdt.isoformat(dtdt.now()
                       .astimezone(dt.timezone(dt.timedelta(0))))
    window["hour_home"].update(value=current_central_time[11:13])
    window["hour_work"].update(value=current_eastern_time[11:13])
    window["minutes"].update(value=f": {current_utc_time[14:16]}")
    match event:

        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
