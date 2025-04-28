from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import student_tbl
from . serializers import studentForm
 
 
@api_view(['GET'])
def ReadData(request):
    obj=student_tbl.objects.all()
    form=studentForm(obj,many=True)
    return Response(form.data)

@api_view(['GET'])
def OneData(request,pk):
    obj=student_tbl.objects.get(id=pk)
    form=studentForm(obj,many=False)
    return Response(form.data)
 
 
@api_view(['POST'])
def PostData(request):
    form=studentForm(data=request.data)
    if form.is_valid():
        form.save()
    return Response(form.data)

@api_view(['PUT'])
def UpdateData(request,pk):
    tbl=student_tbl.objects.get(id=pk)
    form=studentForm(instance=tbl,data=request.data)
    if form.is_valid():
        form.save()
    return Response(form.data)

api_view(['PATCH'])
def UpdateOne(req,pk):
    obj=student_tbl.objects.get(id=pk)
    one={'snm':req.data.get('snm'),'email':req.data.get('email')}
    form=studentForm(instance=obj,data=one,partial=True)#creating form object
    if form.is_valid():
        form.save()
    return Response(form.data)


api_view(['DELETE'])
def DeleteData(req,pk):
    obj=student_tbl.objects.get(id=pk)
    obj.delete()
    return Response("Item deleted Successfully")