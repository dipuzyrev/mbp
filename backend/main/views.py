from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound

from .models import *

SAULT = 'cp3twep8onrgy'


class UpdateHeightAndWeightAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        height = request.data.get('height')
        weight = request.data.get('weight')

        if not height or not weight:
            raise ParseError('Bad request')
            
        try:
            height = int(height)
            weight = int(weight)
        except ValueError:
            raise ParseError('Bad request')

        request.user.weight = weight
        request.user.height = height
        request.user.save()

        return Response(status=status.HTTP_200_OK)


class AddMeasurementsAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        upper = request.data.get('upper')
        bottom = request.data.get('bottom')
        pulse = request.data.get('pulse')
        comment = request.data.get('comment')

        if not upper or not bottom or not pulse:
            raise ParseError('Bad request')
            
        try:
            upper = int(upper)
            bottom = int(bottom)
            pulse = int(pulse)
        except ValueError:
            raise ParseError('Bad request')

        Measurement.objects.create(
            user=request.user,
            upper=upper,
            bottom=bottom,
            pulse=pulse,
            comment=comment,
        )

        return Response(status=status.HTTP_200_OK)


class UpdateTonometerAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')

        tonometer = Tonometer.objects.create(name=name)
        request.user.tonometer = tonometer
        request.user.save()

        return Response(status=status.HTTP_200_OK)


class AddTreatmentAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        snils = request.data.get('snils')
        comment = request.data.get('comment')
        sault = request.data.get('sault')

        if sault != SAULT:
            raise ParseError('Wrong sault')

        if not comment:
            raise ParseError('No treatment text')

        user = User.objects.filter(snils=snils).first()
        if not user:
            raise NotFound('Wrong SNILS')

        Treatment.objects.create(user=user, comment=comment)

        # TODO: notify user!

        return Response(status=status.HTTP_200_OK)


class AddNoteAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        snils = request.data.get('snils')
        text = request.data.get('text')
        sault = request.data.get('sault')

        if sault != SAULT:
            raise ParseError('Wrong sault')

        if not text:
            raise ParseError('No note text')

        user = User.objects.filter(snils=snils).first()
        if not user:
            raise NotFound('Wrong SNILS')
        
        note = Notes.objects.filter(user=user).first()
        if note:
            note.text = text
            note.save()
        else:
            Notes.objects.create(user=user, text=text)

        return Response(status=status.HTTP_200_OK)


class PatientProfileAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        if ((not user.weight) or (not user.height) or (not user.tonometer)):
            raise ParseError('Weight, height or tonometer is missing')

        response = {
            'treatment': '',
            'measurements': [],
            'tonometer': user.tonometer.name,
        }

        treatment = Treatment.objects.filter(user=user).order_by('-date').first()
        if treatment:
            response['treatment'] = treatment.comment
        
        measurements = Measurement.objects.filter(user=user)
        if measurements:
            for measurement in measurements:
                response['measurements'].append({
                    "upper": measurement.upper,
                    "bottom": measurement.bottom,
                    "pulse": measurement.pulse,
                    "comment": measurement.comment,
                    "date": measurement.date,
                })
        
        return Response(response, status=status.HTTP_200_OK)


class PatientBySnilsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        snils = request.data.get('snils')
        sault = request.data.get('sault')

        if sault != SAULT:
            raise ParseError('Wrong sault')

        user = User.objects.filter(snils=snils).first()
        if not user:
            raise NotFound('Wrong SNILS')

        response = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
            'gender': user.gender,
            'height': user.height,
            'weight': user.weight,
            'snils': user.snils,
            'phone': user.phone,
            'treatment_start': '',
            'treatment': [],
            'measurements': [],
            'tonometer': user.tonometer.name,
            'notes': '',
        }

        treatment = Treatment.objects.filter(user=user).order_by('-date')
        if treatment:
            response["treatment_start"] = treatment[0].date
            for t in treatment:
                response['treatment'].append({
                    "comment": t.comment,
                    "date": t.date,
                })
        
        measurements = Measurement.objects.filter(user=user)
        if measurements:
            for measurement in measurements:
                response['measurements'].append({
                    "upper": measurement.upper,
                    "bottom": measurement.bottom,
                    "pulse": measurement.pulse,
                    "comment": measurement.comment,
                    "date": measurement.date,
                })

        notes = Notes.objects.filter(user=user).first()
        if notes:
            response["notes"] = notes.text
        
        return Response(response, status=status.HTTP_200_OK)