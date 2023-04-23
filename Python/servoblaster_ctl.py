def set_pulse_width(servo_id, pulse_width):
    with open('/dev/servoblaster', 'w') as f:
        #f.write('{}={}\n'.format(servo_id, pulse_width)) # for python <=3.8
        f.write(f"{servo_id}={pulse_width}")

import os

def set_pulse_width_with_os(servo_id, pulse_width):
    # Öffnen der Schnittstelle
    with os.fdopen(os.open('/dev/servoblaster', os.O_WRONLY), 'w') as f:
        # Schreiben des Befehls
        f.write('{}={}\n'.format(servo_id, pulse_width))