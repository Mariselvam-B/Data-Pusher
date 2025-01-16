from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Destination, Incoming
from .serializers import AccountSerializer, DestinationSerializer, IncomingSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(detail=False, methods=['post'])
    def manage(self, request):
        if 'ACTION' not in request.headers:
            return Response({"message": "Invalid Action"}, status=status.HTTP_400_BAD_REQUEST)
        
        action = request.headers['ACTION']
        
        if action == 'create':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif action == 'update':
            account_id = request.data.get('account_id')
            try:
                account = Account.objects.get(account_id=account_id)
            except Account.DoesNotExist:
                return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(account, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Account updated successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif action == 'delete':
            account_id = request.data.get('account_id')
            try:
                account = Account.objects.get(account_id=account_id)
                account.delete()
                return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except Account.DoesNotExist:
                return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response({"message": "Invalid Action"}, status=status.HTTP_400_BAD_REQUEST)
        
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    @action(detail=False, methods=['post'])
    def manage(self, request):
        if 'ACTION' not in request.headers:
            return Response({"message": "Invalid Action"}, status=status.HTTP_400_BAD_REQUEST)
        
        action = request.headers['ACTION']
        secretToken = request.headers['CL-X-TOKEN']
        account_id = request.data.get('account_id')
        try:
            account = Account.objects.get(account_id=account_id, app_secret_token=secretToken)
            account.__sizeof__
        except:
            return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if action == 'create':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Destination created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif action == 'update':
            destination_id = request.data.get('destination_id')
            try:
                destination = Destination.objects.get(destination_id=destination_id)
            except destination.DoesNotExist:
                return Response({"message": "Destination not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(destination, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Destination updated successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif action == 'delete':
            destination_id = request.data.get('destination_id')
            try:
                destination = Destination.objects.get(destination_id=destination_id)
                Destination.delete()
                return Response({"message": "Destination deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except Destination.DoesNotExist:
                return Response({"message": "Destination not found"}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response({"message": "Invalid Action"}, status=status.HTTP_400_BAD_REQUEST)


class IncomingViewSet(viewsets.ModelViewSet):
    queryset = Incoming.objects.all()
    serializer_class = IncomingSerializer

    @action(detail=False, methods=['post'])
    def manage(self, request):
        if 'ACTION' not in request.headers:
            return Response({"message": "Invalid Action"}, status=status.HTTP_400_BAD_REQUEST)
        
        action = request.headers['ACTION']
        secretToken = request.headers['CL-X-TOKEN']
        destination_id = request.data.get('destination_id')
        try:
            destination = Destination.objects.get(destination_id=destination_id)
            print(destination.account_id)
            account = Account.objects.get(account_id=destination.account_id, app_secret_token=secretToken)
            
            account.__sizeof__
        except:
            return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if action == 'create':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Destination created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"message": "Invalid Action"}, status=status.HTTP_400_BAD_REQUEST)