from read_data import fromJson

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    x = 0
    
    for i in data['messages']:
        if i['type']=='message':
            x += 1

    return x
data = fromJson('data/result.json')
print(get_number_of_posts(data))