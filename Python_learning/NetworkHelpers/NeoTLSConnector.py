import requests
import ssl

class NeoTLSConnector(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3
        context.options |= ssl.PROTOCOL_TLSv1_2
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)


