# from scrapers.princeton_scraper import princeton_scraper
# from scrapers.rutgers_scraper import rutgers_scraper
import scrapers
import csv
import pandas as pd
from cache import Cache


def load_records():
    print('Loading names...')
    data = pd.read_excel('33000names.xlsx')
    data = data.head(1000)
    print('Finish loading names...\n')
    return data

def parse_name(name):
    name = ' '.join([word for word in name.split() if len(word) > 1])
    titles = ['Dr.', 'Mr.','Prof.','Ms.']
    for title in titles:
        if title in name:
            name = name.replace(title, '')
    return name


records = load_records()
saved_data = pd.read_csv('data.csv')

EMAILS = []

for row in records.itertuples(index=False):
    name, institution = getattr(row, 'name'), getattr(row, 'company')

    if isinstance(institution, str) and 'princeton' in institution.lower():
        # extract email
        email = scrapers.princeton_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'rutgers' in institution.lower():
        email = scrapers.rutgers_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'virginia tech' in institution.lower():
        # extract email
        email = scrapers.virginia_tech_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))
    if isinstance(institution, str) and 'stony brook' in institution.lower():
        # extract email
        email = scrapers.stony_brook_scraper(parse_name(name))
        EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'delaware' in institution.lower():
        # extract email
        email = scrapers.delaware_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'temple' in institution.lower():
        # extract email
        email = scrapers.temple_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))


    if isinstance(institution, str) and 'minnesota' in institution.lower():
        # extract email
        email = scrapers.minnesota_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'university of pennsylvania' in institution.lower():
        # extract email
        email = scrapers.upenn_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))


    if isinstance(institution, str) and 'drexel' in institution.lower():
        # extract email
        email = scrapers.drexel_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'oak' in institution.lower():
        # extract email
        email = scrapers.oak_ridge_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))


    if isinstance(institution, str) and 'michigan' in institution.lower():
        # extract email
        email = scrapers.michigan_scraper(parse_name(name))
        if email is None: continue
        EMAILS.append((name, institution, email))


#print(EMAILS)

df  = pd.DataFrame(EMAILS, columns=['name', 'institution', 'email'])
df.to_csv('data.csv')
