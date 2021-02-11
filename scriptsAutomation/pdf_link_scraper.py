import math

url_template = "https://webservices.ignou.ac.in/Pre-Question/Question%20Paper%20{month}%20{year}/{school}/{subject}/{file}"


def month_yielder (i):
    month=['June','December']
    if i==13:
        return 'Dec'
    else:
        return month[i%2]

def year_yielder(i):
    return 2020-math.ceil(i/2)

def school_yielder(i):
    return 'SOSS'

def subject_yielder(i):
    return 'MA(ECONOMICS)'

def file_yielder(i):
    return 'MEC-001.PDF'

def url_create (url_template,i) :
    return url_template.format(**{
    'month':month_yielder(i),
    'year': year_yielder(i),
    'school': school_yielder(i),
    'subject':subject_yielder(i),
    'file': file_yielder(i)
    })

def sequencer():
    for i in range(0,17):
        yield i

def url_generator(url_template=url_template,sequence=sequencer):
    for i in sequencer():
        yield url_create(url_template,i)        


