from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sample

class SampleAPI(APIView):
    
    def post(self, request):
        
        print(request.data) # termilin la data va print
        
        new_data = Sample(name = request.data[ 'name' ], age = request.data[ 'age' ]) # pus data to model

        new_data.save() # save data in databse

        return Response("Sucessfully POSTED") # post panna out mess

    def get(self, request):

        all_data = Sample.objects.all()

        data_list = []

        for value in all_data:

            data_dict = {
                "id" : value.id,
                "name" : value.name,
                "age" : value.age
            }

            data_list.append(data_dict)

        return Response(data_list)

    def put(self, request, data_id):

        data = Sample.objects.filter(id = data_id)

        data.update(name = request.data[ 'name' ], age = request.data[ 'age' ])

        return Response("Data Updated")
    
    def delete(self, request, data_id):

        data = Sample.objects.filter(id = data_id)

        data.delete()

        return Response("Sucessfully Deleted!!")