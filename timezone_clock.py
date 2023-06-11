# Import modules for GUI and handling datetimes and timezones.
import PySimpleGUI as PySG
from datetime import datetime as dt2
import pytz

# Set up GUI layout.
PySG.theme('DarkBlue13')
hour_home = PySG.Text('', key='hour_home',
                      font=('Helvetica', 60),)
hour_work = PySG.Text('', key='hour_work',
                      font=('Helvetica', 60))
label_home = PySG.Text('home\n', key='label_home',
                       font=('Helvetica', 18))
label_blank_1 = PySG.Text('', key='label_blank_1',
                          font=('Helvetica', 3))
label_work = PySG.Text('\nwork', key='label_work',
                       font=('Helvetica', 18))
minutes_digits = PySG.Text('', key='minutes_digits',
                           font=('Helvetica', 60))

left_far_column_content = [[hour_home],
                           [hour_work]]
left_middle_column_content = [[label_home],
                              [label_blank_1],
                              [label_work]]
right_middle_column_content = [[minutes_digits]]

left_column = PySG.Column(left_far_column_content)
middle_column = PySG.Column(left_middle_column_content)
right_column = PySG.Column(right_middle_column_content)

# Initialize GUI window.
window = PySG.Window('Timezone Clock',
                     layout=[[left_column, middle_column, right_column]],
                     grab_anywhere=True)

# While loop for running clock:
while True:
    # Handle window-closing events immediately after reading window
    # to prevent small error upon X-closing after the program becomes
    # an executable.
    event, values = window.read(timeout=500)
    match event:
        case PySG.WIN_CLOSED:
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
    window['minutes_digits'].update(
        value=('0' + str(current_utc_datetime.minute))[-2:])

# Close GUI window upon loop break.
window.close()
