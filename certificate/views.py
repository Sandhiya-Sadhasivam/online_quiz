import os
import pandas as pd
import shortuuid
from PIL import ImageFont, ImageDraw, Image
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.shortcuts import render

from .models import details


# Create your views here.

def generate(request):
    if request.method == "POST":
        fileUpload = request.FILES['file']
        f = FileSystemStorage()
        f.save(fileUpload.name, fileUpload)
        fileName = fileUpload.name

        df = pd.read_excel('uploads/%s' % fileName, sheet_name='Sheet1')
        n = df.columns[0]
        o = df.columns[1]
        c = df.columns[2]
        m = df.columns[3]

        fullName = df[n]
        org = df[o]
        cer = df[c]
        mail = df[m]
        for i in range(len(df)):
            uniqueId = shortuuid.uuid()
            # Email

            # data base save
            detail = details(name=fullName[i], organization=org[i], certification=cer[i], mail=mail[i], uid=uniqueId)
            detail.save()
            # Email

            # certificate generation

            image = Image.open('template/template.jpg')
            font = ImageFont.truetype("arial.ttf", 70)
            fontTwo = ImageFont.truetype("arial.ttf", 50)

            draw = ImageDraw.Draw(image)

            # use a bitmap font
            draw.text((500, 680), fullName[i], font=font, fill="black")
            # use a truetype font
            draw.text((1266, 850), cer[i], font=fontTwo, fill="black")
            draw.text((1035, 900), org[i], font=fontTwo, fill="black")
            # draw.text((935, 80), mail[i], font=fontTwo , fill ="black")

            image.save("static/certificates/winners/%s.jpg" % uniqueId)

            # Email

            email = EmailMessage(
                'Here is you certificate ',
                'Hi, this is your certificate for completing the course, you can verify this certificate using this unique ID: certify.com/verify/%s  ' % uniqueId,
                'rajeshwaran1718@gmail.com',
                [mail[i]])
            email.attach_file('static/certificates/winners/%s.jpg' % uniqueId)

            email.send()
            # Email

        os.remove('uploads/%s' % fileName)
        return render(request, 'certificate/genrate.html')
    else:

        return render(request, 'certificate/genrate.html')


def verify(request, slug):
    # found = False
    context = {'info': 'NotFound', 'flag': False}
    for f in os.listdir('static/certificates/winners'):
        fn, fext = os.path.splitext(f)
        print(fn)
        if fn == slug:
            context = {'info': slug, 'flag': True}
            found = True
            print("found the certificate")
    return render(request, 'certificate/verify.html', context)



def appreciation_generate(request):
    if request.method == "POST":
        fileUpload = request.FILES['file']
        f = FileSystemStorage()
        f.save(fileUpload.name, fileUpload)
        fileName = fileUpload.name

        df = pd.read_excel('uploads/%s' % fileName, sheet_name='Sheet1')
        n = df.columns[0]
        o = df.columns[1]
        c = df.columns[2]
        m = df.columns[3]

        fullName = df[n]
        org = df[o]
        cer = df[c]
        mail = df[m]
        for i in range(len(df)):
            uniqueId = shortuuid.uuid()
            # Email

            # data base save
            detail = details(name=fullName[i], organization=org[i], certification=cer[i], mail=mail[i], uid=uniqueId)
            detail.save()
            # Email

            # certificate generation

            image = Image.open('template/template1.jpg')
            font = ImageFont.truetype("arial.ttf", 70)
            fontTwo = ImageFont.truetype("arial.ttf", 50)

            draw = ImageDraw.Draw(image)

            # use a bitmap font
            draw.text((500, 680), fullName[i], font=font, fill="black")
            # use a truetype font
            draw.text((1266, 850), cer[i], font=fontTwo, fill="black")
            draw.text((1035, 900), org[i], font=fontTwo, fill="black")
            # draw.text((935, 80), mail[i], font=fontTwo , fill ="black")

            image.save("static/certificates/participant/%s.jpg" % uniqueId)

            # Email

            email = EmailMessage(
                'Here is you certificate ',
                'Hi, this is your appreciation certificate, you can verify this certificate using this unique ID: certify.com/verify/%s  ' % uniqueId,
                'rajeshwaran1718@gmail.com',
                [mail[i]])
            email.attach_file('static/certificates/participant/%s.jpg' % uniqueId)

            email.send()
            # Email

        os.remove('uploads/%s' % fileName)
        return render(request, 'certificate/appreciation_genrate.html')
    else:

        return render(request, 'certificate/appreciation_genrate.html')


def appreciation_verify(request, slug):
    # found = False
    context = {'info': 'NotFound', 'flag': False}
    for f in os.listdir('static/certificates/participant'):
        fn, fext = os.path.splitext(f)
        print(fn)
        if fn == slug:
            context = {'info': slug, 'flag': True}
            found = True
            print("found the certificate")
    return render(request, 'certificate/appreciation_verify.html', context)








