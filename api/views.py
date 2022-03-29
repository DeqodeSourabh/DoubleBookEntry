from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Books, Shelf, Journal, BookEntity
# Create your views here.
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def show_balance_view(request, *args, **kwargs):
#     try:
#         qs = User.objects.filter(username=request.user)[0].profile
#         serializer = walletSerializer(qs)
#         print(type(serializer))
#         # balance = serializer.data['balance']
#         print(serializer.data['balance'])
#         return Response(serializer.data, status=200)
#     except Exception as e:
#         print(e)
#         return Response({"Something went wrong. Please try again later."}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_Book_view(request, *args, **kwargs):
    try:
       # with transaction.atomic():
            user = request.user
            toAdd = request.data.get("toAdd")
            amount = request.data.get("quantity")

            is_user = Shelf.objects.get(username=request.user)
            if not is_user:
                shelf = Shelf(username=user)
            else:
                qs=Books.objects.get()


                return Response({"Deposit successful."}, status=200)
    except Exception as e:

        return Response({"Something went wrong. Please try again later."}, status=404)
