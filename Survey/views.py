from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Question,Modern_Home,Sales_team,Finished_Inventory,Builder_Data
# from .models import Question,Builder_Data,Modern_Home,Sales_team,Finished_Inventory,Join_Inventory,Join_Modern_Home,Join_Sales
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from json import loads as jsonloads
from PIL import Image
import os

from django.template.loader import get_template 
from django.template import Context
import numpy as np
import json
from Survey import cuatom_function

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import reportlab.platypus

def index(request):
    print("LOG!","enter in the index")
    return render(request)
    # return render(request,'index.html',context={"Question":Question.objects.all(),
                                                # "Modern_Home":Modern_Home.objects.all(),
                                                # "Sales_team":Sales_team.objects.all(),
                                                # "Finished_Inventory":Finished_Inventory.objects.all()})

def data_test(request):
    return render(request,'form.html')
def test(request):
    return render(request,'test.html',context={"Question":Question.objects.all()})

@csrf_exempt
def Form_Data(request):
    print("enter in the scrf exempt")
    if request.method == 'POST':
        builder=request.POST.get('Builder')
        Community=request.POST.get('Community')
        Q_Notes=request.POST.get('Q_Notes')
        S_Notes=request.POST.get('S_Notes')
        H_Notes=request.POST.get('H_Notes')
        F_Notes=request.POST.get('F_Notes')
        Summary_Notes=request.POST.get('Summary_Notes')
        Question_list = json.loads(request.POST.get('Question'))
        Home_list=json.loads(request.POST.get('Home'))
        sales_list=json.loads(request.POST.get('sales'))
        inventory_list=json.loads(request.POST.get('inventory'))
        image_list_Q=json.loads(request.POST.get('image_list_Q'))
        # for i in image_list_Q['image_list']:
            # print("tets",i)
        image_list_F=json.loads(request.POST.get('image_list_F')) 
        image_list_S=json.loads(request.POST.get('image_list_S'))
        image_list_H=json.loads(request.POST.get('image_list_H')) 
        # print(image_list_Q)
        # print(Home_list)
        # print(sales_list)
        for i in Question_list:
            print("Hello",Question_list[i])
        # print("image_list",request.FILES)
        # im = Image.open(image)
        # frame = cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR) 
        # print("FInally:",image)
        # print("Final_Two:",builder)
        # print("Community",Community)
        # print("Q_Notes",Q_Notes)
        # print(Summary_Notes)
        # print(Question)
        # for i in image_list_Q['image_list']:
        #     print(request.FILES(i))

        # print(image_list_Q)
        img_path_Q=cuatom_function.get_image_link('imageFile_Q',7)
        img=request.FILES['images']
        for i in img_path_Q:
                try:
                    pass
                    # im = Image.open(request.FILES[i])
                    # frame = cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)
                    # print("image",frame)
                except:
                    pass
    return HttpResponse('done')

@csrf_exempt
def PDF_FILE(request):
    list_Q=[]
    list_H=[]
    list_S=[]
    list_I=[]
    Question_list = json.loads(request.POST.get('Question'))
    Home_list=json.loads(request.POST.get('Home'))
    sales_list=json.loads(request.POST.get('sales'))
    inventory_list=json.loads(request.POST.get('inventory'))
    print(Question_list)
    for i in Question_list:
            list_Q.append(Question_list[i])
    for i in Home_list:
            list_H.append(Home_list[i])
    for i in sales_list:
            list_S.append(sales_list[i])
    for i in inventory_list:
            list_I.append(inventory_list[i])
    # create_pdf('test.pdf',list_Q,list_H,list_S,list_I)
    return HttpResponse("Pdf_done")

def create_pdf(filename='test.pdf'):
    logo = "SSE.png"
    Builder_name="Salman Sajid"
    Community_name="G-10/2"
    Inspected_by="sassa"
    date="128/151"
    summary="dfdvlmnfkomtrmgkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkktprmogtrmtmpgtrmlkfgm "
    Question_list=Question.objects.all()
    Modern_Home_list=Modern_Home.objects.all()
    Sales_team_list=Sales_team.objects.all()
    Finished_Inventory_list=Finished_Inventory.objects.all()
    doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
    story = []
    im = reportlab.platypus.Image(logo, 2*inch, 2*inch)
    story.append(im)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    # ptext = '%s' % Builder_name
    story.append(Paragraph("Builder:  "+str(Builder_name), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Community:  "+str(Community_name), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Inspected By:  "+str(Inspected_by), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Date:  "+str(date), styles["Normal"]))
    story.append(Spacer(1, 12))

    section_data = [
        ("General Community Conditions!",Question_list),
        ("Model Home!", Modern_Home_list),
        ("Sales Team & Sales Center!", Sales_team_list),
        ("Finished Inventory!", Finished_Inventory_list),
    ]
    count=0
    for section, questions in section_data:
        print("data",count)
        heading = Paragraph(f"<b>{section}</b>", styles["Title"])
        story.append(heading)
        question_table_data = []
        question_table_data_P=[]
        for question in questions:
            question_table_data.append([question, "1", "2", "3", "4", "5"])
            # print("temp",temp)
          # Add summary paragraph (notes) row
        summary_paragraph = Paragraph("<i>Summary Notes:</i>", style=getSampleStyleSheet()['Normal'])
        question_table_data_P.append([summary_paragraph])

        question_table = Table(question_table_data, colWidths=[5*inch, 1*inch, 1*inch, 1*inch, 1*inch, 1*inch])
        question_table_P = Table(question_table_data_P, colWidths=[10*inch])
        question_table.setStyle(TableStyle([
            # ('TEXTCOLOR', (0, 0), (-1, 0), colors.blue),
            # ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (1, 0), (1, 0), colors.red),
        ]))
        question_table_P.setStyle(TableStyle([
            # ('TEXTCOLOR', (0, 0), (-1, 0), colors.blue),
            # ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        count=count+1
        story.append(Spacer(1, 0.5 * inch))
        story.append(question_table)
        story.append(question_table_P)

    # # Adding images
    # image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]  # Replace with your image paths
    # for image_path in image_paths:
    #     img = Image.open(image_path)
    #     img = img.resize((200, 150))
    #     story.append(Spacer(1, 0.5 * inch))
    #     story.append(img)

    doc.build(story)