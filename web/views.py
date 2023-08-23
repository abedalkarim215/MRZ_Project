from django.views.generic import TemplateView
from django.shortcuts import render
from passporteye import read_mrz
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import pycountry
import PyPDF2
from django.conf import settings
import os
import re


# Create your views here.

class Landing(TemplateView):
    template_name = 'web/landing.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

class MRZ_Extractor(TemplateView):
    template_name = 'web/mrz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access request object using self.request
        context['passport_type'] = "- "
        context['first_name'] = "-"
        context['second_name'] = "-"
        context['third_name'] = "-"
        context['surname'] = "-"
        context['passport_numebr'] = "-"
        context['personal_ID_number'] = "-"
        context['nationality'] = "-"
        context['gender'] = "-"
        context['date_of_birth'] = "-"
        context['passport_expiry_date'] = "-"
        context['uploaded_image'] = "web/img/1.png"
        context['get'] = True
        context['mrz_code'] = "-"
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
    def post(self, request, *args, **kwargs):
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            image_content = uploaded_image.read()
            fs = FileSystemStorage()
            saved_image = fs.save(uploaded_image.name, uploaded_image)
            def get_gender_name(gender_code):
                if gender_code == 'M':
                    return "Male"
                elif gender_code == "F":
                    return "Female"
                else:
                    return "Unknown"
            try:
                mrz = read_mrz(image_content)
                mrz_data = mrz.to_dict()
                print(mrz_data)
                print("*"*10)
                print(mrz_data['raw_text'].split("\n")[0])
                context = self.get_context_data()
                context['uploaded_image'] = fs.url(saved_image)
                context['mrz_code'] = mrz_data['raw_text'] if "raw_text" in mrz_data else "-"
                context['passport_type'] = mrz_data['type'].replace('<', '') if "type" in mrz_data else "-"
                context['first_name'] = mrz_data['names'] if "names" in mrz_data else "-"
                # context['second_name'] = mrz_data['names'] if "names" in mrz_data else "-"
                # context['third_name'] = mrz_data['names'] if "names" in mrz_data else "-"
                context['surname'] = mrz_data['surname'] if "surname" in mrz_data else "-"
                context['passport_numebr'] = mrz_data['number'].replace('<', '')  if "number" in mrz_data else "-"
                context['personal_ID_number'] = mrz_data['personal_number'].replace('<', '') if "personal_number" in mrz_data else "-"
                # context['nationality'] = mrz_data['nationality'] if "nationality" in mrz_data else "-"
                context['gender'] = get_gender_name(mrz_data['sex']) if "sex" in mrz_data else "-"
                context['date_of_birth'] = datetime.strptime(mrz_data['date_of_birth'], '%y%m%d').date().strftime('%y-%m-%d') if "date_of_birth" in mrz_data else "-"
                context['passport_expiry_date'] = datetime.strptime(mrz_data['expiration_date'],'%y%m%d').date().strftime('%y-%m-%d') if "expiration_date" in mrz_data else "-"
                context['get'] = False
                if 'nationality' in mrz_data:
                    try:
                        nationality = pycountry.countries.get(alpha_3=mrz_data['nationality'])
                        context['nationality'] = nationality.name
                    except LookupError:
                        context['nationality'] = mrz_data['nationality']
                else:
                    context['nationality'] = '-'
                return render(request, self.template_name, context)
            except Exception as e:
                print("Error processing image:", e)
        return self.render_to_response(self.get_context_data())


class Ticket(TemplateView):
    template_name = 'web/ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access request object using self.request
        context['Traveler'] = "- "
        context['Departure'] = "-"
        context['Arrival'] = "-"
        context['Duration'] = "-"
        context['Booking_status'] = "-"
        context['Class'] = "-"
        context['Baggage_allowance'] = "-"
        context['Equipment'] = "-"
        context['Flight_meal'] = "-"
        context['uploaded_image'] = "web/img/1.png"
        context['get'] = True
        return context

    def extract_ticket_info(self,text):
        # Define the regular expression patterns to match the desired information
        patterns = {
            "Traveler": r"Traveler\s+(.*?)(?=\n|$)",
            "Departure": r"Departure\s+(\S.*?)(?=\n|$)",
            "Arrival": r"Arrival\s+(\S.*?)(?=\n|$)",
            "Duration": r"Duration\s+(\S.*?)(?=\n|$)",
            "Booking_status": r"Booking status\s+(\S.*?)(?=\n|$)",
            "Class": r"Class\s+(\S.*?)(?=\n|$)",
            "Baggage_allowance": r"(\d+\s*Kg\(s\))\s+for\s+.*?(?=\n|$)",
            "Equipment": r"Equipment\s+(.*?)(?=\n|$)",
            "Flight_meal": r"(?:Flight meal|Meal)\s+(.*?)(?=\n|$)"
        }

        ticket_info = {}

        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            if match:
                ticket_info[key] = match.group(1).strip()

        return ticket_info


    def extract_text_from_pdf(self, pdf_path):
        text = ""
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Specify the media root
            saved_image = fs.save(uploaded_file.name, uploaded_file)
            pdf_path = fs.path(saved_image)  # Get the full filesystem path
            ticket_info = self.extract_ticket_info(self.extract_text_from_pdf(pdf_path))
            ticket_info['get'] = False
            return render(request, self.template_name, ticket_info)
        return self.render_to_response(self.get_context_data())
