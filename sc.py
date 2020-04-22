# Copy your credentials from the console
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print('Go to the following link in your browser: ' + authorize_url)
code = input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

webmasters_service = build('webmasters', 'v3', http=http)

# Retrieve list of properties in account
site_list = webmasters_service.sites().list().execute()


# Filter for verified websites
verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry']
                       if s['permissionLevel'] != 'siteUnverifiedUser'
                          and s['siteUrl'][:4] == 'http']


#You can choose different dimensions - look at google sc api documentation
# Fill site, startdate and enddate variables.

site = "##WEBSITE URI"
keywords_request = {
      'startDate': "##REPORT_STARTDATE",
      'endDate': "##EPORT_ENDDATE",
      
       'dimensions': ['query'],
       'rowLimit': 500,
  }

#Simple Query with webmaster_service
query_keys = webmasters_service.searchanalytics().query(siteUrl=site, 
                                               body=keywords_request).execute()

#Make Search Console Report Great Again with some codes in here.