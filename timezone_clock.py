# Timezone Clock
# Version 2.5

# Import modules for GUI and handling datetimes and timezones.
import PySimpleGUI as PySG
from datetime import datetime as dt2
import pytz

# Add your new theme colors and settings
# From vigneshsuresh4499
# https://www.geeksforgeeks.org/adding-customized-color-theme-in-pysimplegui/#article-meta-div
PySG.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#163D5C',  # 000066
                                              'TEXT': '#7DCDF1',  # FFCC66
                                              'INPUT': '#339966',
                                              'TEXT_INPUT': '#000000',
                                              'SCROLL': '#99CC99',
                                              'BUTTON': ('#003333', '#FFCC66'),
                                              'PROGRESS': ('#D1826B', '#CC8019'),
                                              'BORDER': 1, 'SLIDER_DEPTH': 0,
                                              'PROGRESS_DEPTH': 0, }

# Switch to use your newly created theme
PySG.theme('MyCreatedTheme')

# Call a popup to show what the theme looks like
# PySG.popup_get_text('This how the MyNewTheme is created')
# End vigneshsuresh4499 section

# Set up GUI layout.
# PySG.theme('DarkBlue13')
font_choice = 'Gill Sans MT'
hour_home = PySG.Text('', key='hour_home',
                      font=(font_choice, 100),
                      tooltip='Hour of the day in 24-hour format\n'
                              'for the US Central Time (CT) zone')
hour_work = PySG.Text('', key='hour_work',
                      font=(font_choice, 100),
                      tooltip='Hour of the day in 24-hour format\n'
                              'for the US Eastern Time (ET) zone')
ct_dot = PySG.Image(key='ct_dot',
                    source='CT dot.png',
                    size=(50, 50),
                    subsample=4,
                    tooltip='US Central Time')
label_blank_1 = PySG.Text('', key='label_blank_1',
                          font=(font_choice, 60))
et_dot = PySG.Image(key='et_dot',
                    source='ET dot.png',
                    size=(50, 50),
                    subsample=4,
                    tooltip='US Eastern Time')
minutes_digits = PySG.Text('', key='minutes_digits',
                           font=(font_choice, 100),
                           tooltip='Minutes of the hour for both CT and ET')
# Check installed fonts:
# print(label_blank_1.fonts_installed_list())

left_far_column_content = [[hour_home],
                           [hour_work]]
left_middle_column_content = [[ct_dot],
                              [label_blank_1],
                              [et_dot]]
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
    window['hour_home'].update(value=('0' + str(current_us_ct_datetime.hour))[-2:])
    window['hour_work'].update(value=('0' + str(current_us_et_datetime.hour))[-2:])
    window['minutes_digits'].update(
        value=('0' + str(current_utc_datetime.minute))[-2:])

# Close GUI window upon loop break.
window.close()
