from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Sum

from expenses.models import User, Expense
from expenses.serializers import UserSerializer, ExpenseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'])
    def list_by_date_range(self, request):
        user_id = request.query_params.get('user')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if not (user_id and start_date and end_date):
            return Response({'error': 'user, start_date, and end_date are required'}, status=400)
        expenses = self.queryset.filter(user_id=user_id, date__range=[start_date, end_date])
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        user_id = request.query_params.get('user')
        month = request.query_params.get('month')
        if not (user_id and month):
            return Response({'error': 'user and month are required'}, status=400)
        expenses = self.queryset.filter(user_id=user_id, date__month=month)
        summary = expenses.values('category').annotate(total=Sum('amount'))
        return Response(summary)
