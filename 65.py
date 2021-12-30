marketing=['loyality program','client promotion','market research']
print(marketing)

marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2, 'investors relations')
print(marketing)

emailMarketing = marketing.copy()
emailMarketing.sort()
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)

NewEmailMarketing = tuple(emailMarketing)
print(NewEmailMarketing)