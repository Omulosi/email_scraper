# from scrapers.princeton_scraper import princeton_scraper
# from scrapers.rutgers_scraper import rutgers_scraper
import scrapers
import csv
import pandas as pd


def load_names():
    print('Loading names...')
    data = pd.read_excel('33000names.xlsx')
    data = data.head(1000)
    print('Finish loading names...')
    return data

def parse_name(name):
    name = ' '.join([word for word in name.split() if len(word) > 1])
    titles = ['Dr.', 'Mr.','Prof.','Ms.']
    for title in titles:
        if title in name:
            name = name.replace(title, '')
    return name

data = load_names()

EMAILS = []

for row in data.itertuples(index=False):
    name, institution = getattr(row, 'name'), getattr(row, 'company')
    
    # if isinstance(institution, str) and 'princeton' in institution.lower():
    #     # extract email
    #     email = scrapers.princeton_scraper(parse_name(name))
    #     EMAILS.append((name, institution, email))

    if isinstance(institution, str) and 'rutgers' in institution.lower():
        email = scrapers.rutgers_scraper(parse_name(name))
        EMAILS.append((name, institution, email))

    # if isinstance(institution, str) and 'virginia tech' in institution.lower():
    #     # extract email
    #     email = scrapers.virginia_tech_scraper(parse_name(name))
    #     EMAILS.append((name, institution, email))
    # if isinstance(institution, str) and 'stony brook' in institution.lower():
    #     # extract email
    #     email = scrapers.stony_brook_scraper(parse_name(name))
    #     EMAILS.append((name, institution, email))


#print(EMAILS)

df  = pd.DataFrame(EMAILS, columns=['name', 'institution', 'email'])
df.to_csv('data.csv')