from flask import url_for, render_template, request, redirect, Flask
import json
from urllib.parse import unquote
import re
from collections import Counter

app = Flask(__name__)

@app.route('/')
def question():
    return render_template('question.html')

@app.route('/thanks')
def thanks():
    if request.args:
        name = unquote(request.args['name'])
        age = unquote(request.args['age'])
        throw = unquote(request.args['throw'])
        nishtak = unquote(request.args['nishtak'])
        vs1 = unquote(request.args['vs1'])
        vs2 = unquote(request.args['vs2'])
        vs3 = unquote(request.args['vs3'])
        vs4 = unquote(request.args['vs4'])
        if len(name) == 0 or len(age) == 0 or len(throw) == 0 or len(nishtak) == 0:
            return render_template('question.html')
        else:
            throw = throw.split(',')
            arr_throw = ['throw']
            i = 0
            while i < len(throw):
                arr_throw.append(throw[i])
                i += 1
            nishtak = nishtak.split(',')
            arr_nishtak = ['nishtak']
            i = 0
            while i < len(nishtak):
                arr_nishtak.append(nishtak[i])
                i += 1
            all_data_arr = [name,age,arr_throw,arr_nishtak,vs1,vs2,vs3,vs4]
            file(str(all_data_arr)+'\n','data.txt')
            return render_template('thanks.html', name=name)
    else:
        return render_template('question.html')

@app.route('/jsn')
def jsn():
    all_mass = all_m()
    create_jsn = json.dumps(all_mass,ensure_ascii=False)
    file(create_jsn,'jsn_file.json')
    return render_template('jsn.html',create_jsn=create_jsn)

@app.route('/stats')
def statistic():
    s = first()
    n = second()
    a,b,c,d,aa,bb,cc,dd,e,f,g,h,ee,ff,gg,hh,y,x,o,m,yy,xx,oo,mm = third2()
    return render_template('stats.html',s=s,n=n,a=a,b=b,c=c,d=d,aa=aa,bb=bb,cc=cc,dd=dd,e=e,f=f,g=g,h=h,ee=ee,ff=ff,gg=gg,\
                           hh=hh,y=y,x=x,o=o,m=m,yy=yy,xx=xx,oo=oo,mm=mm)

def first():
    all_mass = all_m()
    z = 0
    mass_throw = []
    str_throw = ''
    while z < len(all_mass):
        ans = re.search('(?:\[\'throw\'\,)([ \'а-я,]+).*?]',all_mass[z])
        ans = re.sub('[\' ]+','',ans.group(1))
        str_throw = str_throw + ans + ','
        z += 1
    mass_throw = str_throw.split(',')
    mass_throw = mass_throw[:-1]
    count = Counter(mass_throw)
    d = {}
    k = 0
    while k < len(mass_throw):
        d[mass_throw[k]] = count[mass_throw[k]]
        k += 1
    s = ''
    for key in d:
        percent = round(100*d[key]/len(all_mass))
        s = s + 'Значение \'%s\' указало %s процентов информантов. ' % (key,percent)
    return s

def second():
    all_mass = all_m()
    z = 0
    mass_nishtak = []
    str_nishtak = ''
    while z < len(all_mass):
        ans = re.search('(?:\[\'nishtak\'\,)([ \'а-я,]+).*?]',all_mass[z])
        ans = re.sub('[\' ]+','',ans.group(1))
        str_nishtak = str_nishtak + ans + ','
        z += 1
    mass_nishtak = str_nishtak.split(',')
    mass_nishtak = mass_nishtak[:-1]
    count = Counter(mass_nishtak)
    d = {}
    k = 0
    while k < len(mass_nishtak):
        d[mass_nishtak[k]] = count[mass_nishtak[k]]
        k += 1
    n = ''
    for key in d:
        percent = round(100*d[key]/len(all_mass))
        n = n + 'Значение \'%s\' слова указало %s процентов информантов. ' % (key,percent)
    return n

def third1():
    all_mass = all_m()
    z = 0
    third_mass = []
    while z < len(all_mass):
        year = re.search('[0-9]+',all_mass[z])
        one = re.search('(a(?:c|k)[a-z]+).*?',all_mass[z])
        two = re.search('(lin[a-z]+).*?',all_mass[z])
        three = re.search('(aut[a-z]+).*?',all_mass[z])
        four = re.search('(pr[a-z]+).*?',all_mass[z])
        third_str = year.group(0) + ',' + one.group(0) + ',' + two.group(0) + ',' + three.group(0) + ',' + four.group(0)
        third_mass.append(third_str)
        z += 1
    return third_mass

def third2():
    third_mass = third1()
    mass00 = []
    mass33 = []
    mass66 = []
    for line in third_mass:
        if int(line[0:line.find(',')]) > 66:
            mass66.append(line.split(','))
        elif int(line[0:line.find(',')]) > 33:
            mass33.append(line.split(','))
        else:
            mass00.append(line.split(','))
    a,b,c,d = third3(mass66)
    e,f,g,h = third3(mass33)
    y,x,o,m = third3(mass00)
    if a == 0 and b == 0 and c == 0 and d == 0:
        a,b,c,d = round(a),round(b),round(c),round(d)
        aa,bb,cc,dd = 0,0,0,0
    else:
        a,b,c,d = round(a),round(b),round(c),round(d)
        aa,bb,cc,dd = 100-a,100-b,100-c,100-d
    if e == 0 and f == 0 and g == 0 and h == 0:
        e,f,g,h = round(e),round(f),round(g),round(h)
        ee,ff,gg,hh = 0,0,0,0
    else:
        e,f,g,h = round(e),round(f),round(g),round(h)
        ee,ff,gg,hh = 100-e,100-f,100-g,100-h
    if y == 0 and x == 0 and o == 0 and m == 0:
        y,x,o,m = round(y),round(x),round(o),round(m)
        yy,xx,oo,mm = 0,0,0,0
    else:
        y,x,o,m = round(y),round(x),round(o),round(m)
        yy,xx,oo,mm = 100-y,100-x,100-o,100-m
    return a,b,c,d,aa,bb,cc,dd,e,f,g,h,ee,ff,gg,hh,y,x,o,m,yy,xx,oo,mm

def third3(mass):
    i = 0
    statvs1 = 0
    statvs2 = 0
    statvs3 = 0
    statvs4 = 0
    while i < len(mass):
        if mass[i][1] == 'akademka':
            statvs1 += 1
        if mass[i][2] == 'lineyka':
            statvs2 += 1
        if mass[i][3] == 'automat':
            statvs3 += 1
        if mass[i][4] == 'prepod':
            statvs4 += 1
        i += 1
    num = len(mass)
    if num == 0:
        num = 1
    return statvs1/num*100,statvs2/num*100,statvs3/num*100,statvs4/num*100

def all_m():
    fj = open ('data.txt', 'r', encoding = 'utf-8')
    all_mass = []
    for line in fj:
        all_mass.append(line)
    fj.close()
    return all_mass
            
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results')
def result():
    if request.args:
        choose = unquote(request.args['choose']) 
        a,b,c,d,aa,bb,cc,dd,e,f,g,h,ee,ff,gg,hh,y,x,o,m,yy,xx,oo,mm = third2()
        s = first()
        n = second() 
        return render_template('results.html',choose=choose,s=s,n=n,a=a,b=b,c=c,d=d,aa=aa,bb=bb,cc=cc,dd=dd,e=e,f=f,g=g,h=h,ee=ee,ff=ff,gg=gg,\
                           hh=hh,y=y,x=x,o=o,m=m,yy=yy,xx=xx,oo=oo,mm=mm)
    else:
        return render_template('search.html')

def file(inf,name):
    f = open(name, 'a', encoding = 'utf-8')
    f.write(inf)
    f.close()

if __name__ == '__main__':
    app.run()
