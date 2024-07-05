import random
def get_user_agent():
    ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15']

    return random.choice(ua_list)
    
carrier_gateways = {
    'AT&T': 'txt.att.net',
    'Sprint': 'messaging.sprintpcs.com',
    'T-Mobile': 'tmomail.net',
    "Mint Mobile": "tmomail.net",
    'Verizon Wireless': 'vtext.com',
    'Virgin Mobile': 'vmobl.com',
    'Rogers Wireless': 'sms.rogers.com',
    'Boost Mobile': 'sms.myboostmobile.com',
    'Telus Mobility': 'msg.telus.com',
    'Airfire Mobile': 'sms.airfiremobile.com',
    'Ameritech': 'paging.acswireless.com',
    'Assurance Wireless': 'vmobl.com',
    'BellSouth': 'bellsouth.cl',
    'Bluegrass Cellular': 'sms.bluecell.com',
    'Cellcom': 'cellcom.quiktxt.com',
    'Cellular South': 'csouth1.com',
    'Chariton Valley Wireless': 'sms.cvalley.net',
    'Chat Mobility': 'mail.msgsender.com',
    'Cleartalk': 'sms.cleartalk.us',
    'Consumer Cellular': 'cingularme.com',
    'Cricket': 'sms.cricketwireless.net',
    'Element Mobile': 'SMS.elementmobile.net',
    'Esendex': 'echoemail.net',
    'Mellon Mobile': 'mellonmobile.ga',
    'MetroPCS': 'mymetropcs.com',
    'Nextech': 'sms.ntwls.net',
    'Page Plus Cellular(Verizon MVNO)': 'vtext.com',
    'South Central Communications': 'rinasms.com',
    'Southernlinc': 'page.southernlinc.com',
    'Straight Talk': 'txt.att.net',
    'Syringa Wireless': 'rinasms.com',
    'Teleflip': 'teleflip.com',
    'Union Wireless': 'union-tel.com',
    'US Cellular': 'email.uscc.net',
    'Voyager Mobile': 'text.voyagermobile.com',
    'Centennial Wireless': 'cwemail.com',
    'TracFone (prepaid)': 'txt.att.net'
}

def get_carriers():
    return carrier_gateways.keys()

def get_carrier_gateway(carrier):
    return carrier_gateways[carrier]
