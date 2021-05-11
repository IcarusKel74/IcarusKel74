info = {'name':'Bob','Ref':'Python','sys':'win'}
print('Info',type(info))
print('dict',info)

print('\nReference:',info['Ref'])

print('\nKeys',info.keys())

del info['name']

print('dict',info)

info['user']='Tom'
print('\ndict',info)

print('\nIs there a name?: ','name' in info)
