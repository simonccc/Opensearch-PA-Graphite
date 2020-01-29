import os
elastic = {'es_host': os.environ['es_host'],
	 'user': os.environ['user'],
	 'pass': os.environ['pass']}
graphite = {'g_host': os.environ['g_host'],
            'prefix': os.environ['prefix']}
