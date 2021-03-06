from rest_framework import generics
from rest_framework.response import Response
from .serializers import GetAccountSerializer, ExternalTransferSerializer
from .models import Account, Ledger

class GetAccount(generics.ListCreateAPIView):
  def get(self, request):
    accounts = Account.objects.all()
    id = request.query_params.get("id")

    account = accounts.get(id=id)
    serializer = GetAccountSerializer(account, many=False)
    return Response(data=serializer.data, status=200)

class ExtrenalTransfer(generics.ListCreateAPIView):
  def post(self, request):
    accounts = Account.objects.all()
    account = request.query_params.get("id")
    transaction_id = request.query_params.get("transaction_id")
    amount = int(request.query_params.get("amount"))
    text = request.query_params.get("text") 
    account = accounts.get(pk=account)

    try: 
      bank_account = accounts.get(title="Bank OPS Account")
      Ledger.externalTransfer(
        amount=amount,
        debit_account=bank_account,
        debit_text=text,
        credit_account=account,
        credit_text=text,
        transaction_id=transaction_id,
      )
      return Response({"info": "Transaction went through"}, status=200)
    except Exception as error:
      return Response({error}, status=500)