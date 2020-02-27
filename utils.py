
DIRECTORIES = {
    'princeton': 'https://www.princeton.edu/search',
    'rutgers': 'https://search.rutgers.edu/',
    'virginia tech': 'http://search.vt.edu/search/m/people.html',
    'stony brook': 'https://adam.cc.sunysb.edu:8443/acc/new-dirsearch.cgi?name_string={}&status=Any',
    'university of minnesota': 'https://myaccount.umn.edu/lookup',
    'temple university': 'https://directory.temple.edu/',
    'delaware': 'https://udapps.nss.udel.edu/directory/search',
    'temple': 'https://directory.temple.edu/',
    'minnesota': 'https://myaccount.umn.edu/lookup?SET_INSTITUTION=UMNTC&type=name&CN={}&campus=a&role=any'
}

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

def split_name(name):
    # split name into first name and last name
    name = name.split()
    if len(name) > 1:
        return name[0], name[-1]
    return ' '.join(name)
