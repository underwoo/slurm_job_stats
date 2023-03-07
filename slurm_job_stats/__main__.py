import subprocess
import argparse
import datetime
import re

from .__init__ import jobCounts

def main():
    argParser = argparse.ArgumentParser(
        description = 'Collect simple statistics for Slurm jobs')
    argParser.add_argument('-S', '--starttime',
                           help="Select jobs in any state after the specified time.  " \
                                "Default is 00:00:00 of the current day.",
	                   type=datetime.datetime.fromisoformat)
    argParser.add_argument('-E', '--endtime',
                           help="Select jobs in any state before the specified time.",
                           type=datetime.datetime.fromisoformat)
    argParser.add_argument('-M', '--clusters',
                           help="Only send data about these clusters. Use \"all\" for all " \
                                "clusters.  (Default: c3,c4,c5)",
                           default="c3,c4,c5",
                           type=str)
    argParser.add_argument('--csv',
                           help="Print output in csv string with headers: " \
                                "'total', 'cd', 'f', 'to', 'nf', 'oom', 'ca'",
                           action='store_true')
    
    cli_args = argParser.parse_args()

    sacct_cmd = ['sacct', '-a', '-X', '-n',
                 '--format', 'state%-10',
                 '--clusters', cli_args.clusters]
    if cli_args.starttime:
        sacct_cmd.extend(['--starttime', cli_args.starttime.isoformat()])
    if cli_args.endtime:
        sacct_cmd.extend(['--endtime', cli_args.endtime.isoformat()])

    try:
        output = re.split(' *\n', subprocess.check_output(sacct_cmd).decode().strip())
    except Exception as err:
        print(f'Command \'{" ".join(sacct_cmd)} failed.')
        raise err

    job_counts = jobCounts(output)
    if cli_args.csv:
        print(','.join(str(x) for x in job_counts.to_list()))
    else:
        print(job_counts)


if __name__== "__main__":
    sys.exit(main())
