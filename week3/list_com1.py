username_mail = [line.strip('From:').strip().split('@')[0] for line in open('mbox-short.txt') if line.startswith('From: ')]
print(username_mail)
domain_mail = [line.strip('From:').strip().split('@')[1] for line in open('mbox-short.txt') if line.startswith('From: ')]
print(domain_mail)
