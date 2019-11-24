'''

Copyright 2019, Amazon Web Services Inc.

SPDX-License-Identifier: MIT-0

Defines a MetricDescription collection. Provides a single function that returns
a list of all currently-working (April 2019) metric/agg/dimension combinations.
Ideally, Open Distro would provide an API to retrieve this information. As of
now, it has to be declarative like this.
'''

from collections import namedtuple

MetricDescription = namedtuple('MetricDescription', ['name', 'agg', 'dimensions'])

def get_working_metric_descriptions():
    ''' Return a list of all of the metric descriptions for PA.'''
    return [
        MetricDescription(name='CPU_Utilization', agg='min', dimensions=[ 'Operation',]),
        MetricDescription(name='CPU_Utilization', agg='max', dimensions=[  'Operation', ]),
        MetricDescription(name='CPU_Utilization', agg='avg', dimensions=[  'Operation', ]),
        MetricDescription(name='Heap_AllocRate', agg='min', dimensions=[ 'Operation', ]),
        MetricDescription(name='Heap_AllocRate', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='Heap_AllocRate', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadThroughput', agg='min', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadThroughput', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadThroughput', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteThroughput', agg='min', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteThroughput', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteThroughput', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadSyscallRate', agg='min', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadSyscallRate', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadSyscallRate', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteSyscallRate', agg='min', dimensions=['Operation', ]),
        MetricDescription(name='IO_WriteSyscallRate', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteSyscallRate', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Time', agg='min', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Time', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Time', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Event', agg='min', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Event', agg='max', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Event', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='ShardEvents', agg='min', dimensions=['Operation', ]),
        MetricDescription(name='ShardEvents', agg='max', dimensions=['Operation', ]),
        MetricDescription(name='ShardEvents', agg='avg', dimensions=['Operation', ]),
        MetricDescription(name='ShardBulkDocs', agg='min', dimensions=['Operation', ]),
        MetricDescription(name='ShardBulkDocs', agg='max', dimensions=['Operation',]),
        MetricDescription(name='ShardBulkDocs', agg='avg', dimensions=['Operation',]),
        MetricDescription(name='Latency', agg='min', dimensions=['Operation', 'Exception',  'HTTPRespCode', ]),
        MetricDescription(name='Latency', agg='max', dimensions=['Operation', 'Exception',  'HTTPRespCode', ]),
        MetricDescription(name='Latency', agg='avg', dimensions=['Operation', 'Exception',  'HTTPRespCode', ]),
        MetricDescription(name='GC_Collection_Event', agg='min', dimensions=['MemType']),
        MetricDescription(name='GC_Collection_Event', agg='max', dimensions=['MemType']),
        MetricDescription(name='GC_Collection_Event', agg='avg', dimensions=['MemType']),
        MetricDescription(name='GC_Collection_Time', agg='min', dimensions=['MemType']),
        MetricDescription(name='GC_Collection_Time', agg='max', dimensions=['MemType']),
        MetricDescription(name='GC_Collection_Time', agg='avg', dimensions=['MemType']),
        MetricDescription(name='Heap_Committed', agg='min', dimensions=['MemType']),
        MetricDescription(name='Heap_Committed', agg='max', dimensions=['MemType']),
        MetricDescription(name='Heap_Committed', agg='avg', dimensions=['MemType']),
        MetricDescription(name='Heap_Max', agg='min', dimensions=['MemType']),
        MetricDescription(name='Heap_Max', agg='max', dimensions=['MemType']),
        MetricDescription(name='Heap_Max', agg='avg', dimensions=['MemType']),
        MetricDescription(name='Heap_Used', agg='min', dimensions=['MemType']),
        MetricDescription(name='Heap_Used', agg='max', dimensions=['MemType']),
        MetricDescription(name='Heap_Used', agg='avg', dimensions=['MemType']),
        MetricDescription(name='ThreadPool_QueueSize', agg='min', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_QueueSize', agg='max', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_QueueSize', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_RejectedReqs', agg='min', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_RejectedReqs', agg='max', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_RejectedReqs', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_TotalThreads', agg='min', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_TotalThreads', agg='max', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_TotalThreads', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_ActiveThreads', agg='min', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_ActiveThreads', agg='max', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_ActiveThreads', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='HTTP_RequestDocs', agg='min', dimensions=['Operation', 'Exception', 'HTTPRespCode']),
        MetricDescription(name='HTTP_RequestDocs', agg='max', dimensions=['Operation', 'Exception',  'HTTPRespCode']),
        MetricDescription(name='HTTP_RequestDocs', agg='avg', dimensions=['Operation', 'Exception',  'HTTPRespCode']),
        MetricDescription(name='HTTP_TotalRequests', agg='min', dimensions=['Operation', 'Exception', 'HTTPRespCode']),
        MetricDescription(name='HTTP_TotalRequests', agg='max', dimensions=['Operation', 'Exception',  'HTTPRespCode']),
        MetricDescription(name='HTTP_TotalRequests', agg='avg', dimensions=['Operation', 'Exception',  'HTTPRespCode']),
    ]
