import subprocess


def process_exists(window_title, process_name, cmd_encoding):
    call = 'TASKLIST', '/FI', 'WindowTitle eq %s' % window_title
    # use buildin check_output right away
    output = subprocess.check_output(call).decode(encoding=cmd_encoding)
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())