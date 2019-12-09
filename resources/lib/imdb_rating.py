
import re
import requests

# get the movie info via imdb


def get_imdb_rating_and_votes(id):
    votes = 0
    rating = 0
    r = requests.get('http://www.imdb.com/title/'+id+'/ratings')
    if r.status_code == 200:
        res = re.search(
            r'([\d|,]+)\s*IMDb users have given a.*vote of\s*([\d|\.]+) / 10', r.text)
        if (res):
            votes = int(res.group(1).replace(',', ''))
            rating = float(res.group(2))
    return {'votes': votes, 'rating': rating}
