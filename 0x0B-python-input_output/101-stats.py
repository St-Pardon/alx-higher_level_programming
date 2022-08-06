#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import re


status_codes_stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_file_size = 0
fp = (
    r'\s*(?P<ip>\S+)\s*',
    r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
    r'\s*"(?P<request>[^"]*)"\s*',
    r'\s*(?P<status_code>\S+)',
    r'\s*(?P<file_size>\d+)'
)

log_fmt = f'{fp[0]}\\-{fp[1]}{fp[2]}{fp[3]}{fp[4]}\\s*'


def print_statistics():
    """Prints the accumulated statistics of the HTTP log."""
    global total_file_size, status_codes_stats
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def get_metrics(line):
    '''Retrieves the metrics from a given HTTP log.'''
    global total_file_size, log_fmt, status_codes_stats
    resp_match = re.fullmatch(log_fmt, line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        total_file_size += file_size
        if status_code in status_codes_stats.keys():
            status_codes_stats[status_code] += 1


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    try:
        while True:
            line = input()
            get_metrics(line)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics()
    except (KeyboardInterrupt, EOFError):
        print_statistics()


if __name__ == '__main__':
    run()
