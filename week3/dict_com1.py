def find_domain(username,filename):
    dict_username_domain = {line.strip('From:').strip().split('@')[0] : line.strip('From:').strip().split('@')[1]
                        for line in open(filename) if line.startswith('From: ')}
    return dict_username_domain.get(username)

find_domain('stephen.marquard','mbox-short.txt')
    
