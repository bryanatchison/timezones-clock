# Import modules for GUI and handling datetimes and timezones.
import PySimpleGUI as PySG
from datetime import datetime as dt2
import pytz

# Set up GUI layout.
PySG.theme("DarkBlue13")
hour_home = PySG.Text('', key='hour_home', font=('Helvetica', 60))
hour_work = PySG.Text('', key='hour_work', font=('Helvetica', 60))
label_home = PySG.Text("Home",  font=('Helvetica', 18))
minutes = PySG.Text('', key='minutes', font=('Helvetica', 60))
label_work = PySG.Text("Work", font=('Helvetica', 18))
exit_button = PySG.Button("Exit", font=('Helvetica', 15))


left_column_content = [[hour_home],
                       [hour_work]]

middle_column_content = [[label_home],
                         [minutes],
                         [label_work]]

right_column_content = [[exit_button]]


left_column = PySG.Column(left_column_content)
middle_column = PySG.Column(middle_column_content)
right_column = PySG.Column(right_column_content)

# Initialize GUI window.
window = PySG.Window('Timezone Clock',
                     layout=[[left_column, middle_column, right_column]])


# While loop for running clock:
while True:
    # Handle window-closing events immediately after reading window
    # to prevent small error upon X-closing after the program becomes
    # an executable.
    event, values = window.read(timeout=500)
    match event:
        case PySG.WIN_CLOSED:
            break
        case "Exit":
            break

    # Time and timezone operations:
    current_utc_datetime = dt2.now(pytz.utc)
    current_us_ct_datetime = \
        dt2.now(pytz.utc).astimezone(pytz.timezone('US/Central'))
    current_us_et_datetime = \
        dt2.now(pytz.utc).astimezone(pytz.timezone('America/New_York'))

    # Use times to update GUI window
    window['hour_home'].update(value=str(current_us_ct_datetime.hour))
    window['hour_work'].update(value=str(current_us_et_datetime.hour))
    window['minutes'].update(
        value=f": {('0' + str(current_utc_datetime.minute))[-2:]}")

# Close GUI window upon loop break.
window.close()
