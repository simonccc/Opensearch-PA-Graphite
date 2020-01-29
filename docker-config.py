import os
elastic = {'es_host': os.environ['es_host'],
	 'user': os.environ['user'],
	 'pass': os.environ['pass']}
graphite = {'g_host': os.environ['g_host'],
            'g_port': os.environ['g_port'],
            'prefix': os.environ['prefix']}
