## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(d):
    if d == ({}):
        return []
    d_counts = {}
    for k in d:
        counts = len(d[k])
        if counts == 0:
            counts = 0
        d_counts[k] = counts
    return d_counts
#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(d):
    if d == ({}):
        return []
    keys = []
    for k in d:
        keys.append(k)
    return keys

#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(d, author_count):
    counts = 0
    for k in d:
        for i in d[k]:
            i.items()
            for k , v in i.items():
                if type(v) == dict:
                    v.items()
                    for k, v in v.items():
                        if author_count == v:
                            counts = counts + 1
    return counts

#### End OF MARKER





if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print get_types(d)
    print get_types_counts(d)
    print get_author_count(d, 'cap')

    print get_author_count(d, 'jake', ['articles', 'tweets'])
