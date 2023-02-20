from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    x = 0
    for i in data['messages']:
        date_year = i['date'].split('T')
        date_month = date_year[0].split('-')
        
        if (date_month[1][1]).isdigit():
            
            if int(date_month[1][0])==0:
                if int(date_month[1][1])==month:
                    x += 1

            if int(date_month[1])==month:
                x += 1 

    return x
    
data = fromJson('data/result.json')
print(get_post_month(data, 11))