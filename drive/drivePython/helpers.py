def extension_to_mime(ext):
    extension_mime_map={
        'pdf': 'application/pdf',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png' :'image/png',
        'txt' : 'text/plain',
        '.config' : 'text/plain',    
        }
    if ext in extension_mime_map:
        return extension_mime_map.get('pdf')
    return 'application/octet-stream'

def get_extension_from_file(fileName):
    #check if . exists in fileName
    if fileName == '.':
        return None
    if not '.' in fileName:
        return None
    tmp_array=fileName.split('.')
    if tmp_array[-1] == ''
        return None
    if tmp_array[0]==
    
def test_on_cases(func):
    cases=[
        'application.pdf', 
        'application.1.pdf',
         'suitable.jpeg',
         'application.', 
        'application',
        '.application'
        ]
    for case in cases:
        print('-------------------------')
        print(f"case> {case} result : \n")
        print(func(case))
        print('-------------------------')

def func(case):
    return case.split('.')