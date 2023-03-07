import re

__version__ = "1.0.0"

class jobCount():
    def __init__(self, count, total):
        self.count = count
        self.frac = count/total

    def __str__(self):
        return f"{self.count}\t{self.frac:.2%}"


class jobCounts():
    def __init__(self, stats):
        def count_jobs(jobs):
            job_re = re.compile('^(?!PENDING|RUNNING).*')
            return len(list(filter(job_re.search, jobs)))

        self.total = count_jobs(stats)
        self.ca = jobCount(stats.count('CANCELLED+'), self.total)
        self.cd = jobCount(stats.count('COMPLETED'), self.total)
        self.f = jobCount(stats.count('FAILED'), self.total)
        self.nf = jobCount(stats.count('NODE_FAIL'), self.total)
        self.oom = jobCount(stats.count('OUT_OF_ME+'), self.total)
        self.to = jobCount(stats.count('TIMEOUT'), self.total)

    def to_list(self):
        return [self.total,
                self.cd.count,
                self.f.count,
                self.to.count,
                self.nf.count,
                self.oom.count,
                self.ca.count]

    def __str__(self):
        return f"Completed:\t{self.cd}\n" \
               f"Failed:\t\t{self.f}\n" \
               f"Timeout:\t{self.to}\n" \
               f"Node Failed:\t{self.nf}\n" \
               f"Out of Memory:\t{self.oom}\n" \
               f"Cancelled:\t{self.ca}\n" \
               f"Total Jobs:\t{self.total}"
