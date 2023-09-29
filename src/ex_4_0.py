""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    
    with open(logfile, 'r') as file:
        data = file.read()
    shutdowns_events = list()
    for line in data.splitlines():
        if 'Shutdown initiated' in line :
            shutdowns_events.append(line)
    return shutdowns_events


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
