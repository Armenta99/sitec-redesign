from sitec.sitec_api.models import SitecApi

api = SitecApi()

# api.login('18212170', 'jajatujefa42')
api.is_connected = True

api.retrieve_cycle_advance_data()