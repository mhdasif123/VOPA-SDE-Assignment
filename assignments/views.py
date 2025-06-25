from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Assignment
from .serializers import AssignmentSerializer
from django.utils.timezone import now

@api_view(['POST'])
def assign_lesson(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def student_assignments(request, student_id):
    status_filter = request.GET.get('status')
    assignments = Assignment.objects.filter(student_id=student_id)
    if status_filter == 'incomplete':
        assignments = assignments.filter(is_completed=False)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def mark_complete(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.is_completed = True
        assignment.completed_at = now()
        assignment.save()
        return Response({"message": "Marked as complete."})
    except Assignment.DoesNotExist:
        return Response({"error": "Assignment not found."}, status=404)

@api_view(['GET'])
def teacher_assignment_status(request, teacher_id):
    assignments = Assignment.objects.filter(teacher_id=teacher_id)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)
