from collections import namedtuple
MetricDescription = namedtuple('MetricDescription', ['name', 'agg', 'dimensions'])

def get_working_metric_descriptions():
    return [
        MetricDescription(name='CPU_Utilization', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='Heap_AllocRate', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadThroughput', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteThroughput', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_ReadSyscallRate', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='IO_WriteSyscallRate', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Time', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='Thread_Blocked_Event', agg='avg', dimensions=[ 'Operation', ]),
        MetricDescription(name='ShardEvents', agg='avg', dimensions=['Operation']),
        MetricDescription(name='ShardBulkDocs', agg='avg', dimensions=['Operation']),
        MetricDescription(name='Latency', agg='avg', dimensions=['Operation', ]),
        MetricDescription(name='GC_Collection_Event', agg='avg', dimensions=['MemType']),
        MetricDescription(name='GC_Collection_Time', agg='avg', dimensions=['MemType']),
        MetricDescription(name='Heap_Committed', agg='avg', dimensions=['MemType']),
        MetricDescription(name='Heap_Used', agg='avg', dimensions=['MemType']),
        MetricDescription(name='ThreadPool_QueueSize', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_RejectedReqs', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='ThreadPool_ActiveThreads', agg='avg', dimensions=['ThreadPoolType']),
        MetricDescription(name='HTTP_RequestDocs', agg='avg', dimensions=['Operation', ]),
        MetricDescription(name='HTTP_TotalRequests', agg='avg', dimensions=['Operation', ]),
    ]
