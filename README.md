# SLURM Job Statistics

`slurm_job_stats` is a Python module that will collect and print
simple staticstics from SLURM.

Return the total number of jobs run within a give time frame.  Also
return the number of jobs in states cancelled, completed, failed, node
fail, out of memory, and timeout.

```
> slurm_job_stats
Completed:	2173	81.05%
Failed:		242	9.03%
Timeout:	92	3.43%
Node Failed:	0	0.00%
Out of Memory:	0	0.00%
Cancelled:	174	6.49%
Total Jobs:	2681
```

# Disclaimer

The NOAA-GFDL GitHub project code is provided on an 'as is' basis and
the user assumes responsibility for its use. DOC has relinquished
control of the information and no longer has responsibility to protect
the integrity, confidentiality, or availability of the
information. Any claims against the Department of Commerce (DoC), the
National Oceanic and Atmospheric Administration (NOAA), or the
Geophysical Fluid Dynamics Laboratory (GFDL) stemming from the use of
its GitHub projects will be governed by all applicable Federal law. Any
reference to specific commercial products, processes, or services by
service mark, trademark, manufacturer, or otherwise, does not
constitute or imply their endorsement, recommendation or favoring by
the Department of Commerce. The Department of Commerce seal and logo,
or the seal and logo of a DOC bureau, shall not be used in any manner
to imply endorsement of any commercial product or activity by DOC or
the United States Government.

