""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdowns = get_shutdown_events(logfile)
    
    shutdown_1 = shutdowns[0]
    
    shutdown_2 = shutdowns[-1]
       
    shutdown_1_date = logstamp_to_datetime(shutdown_1.split()[1])
    
    shutdown_2_date = logstamp_to_datetime(shutdown_2.split()[1])
    
    return shutdown_2_date-shutdown_1_date
    


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
