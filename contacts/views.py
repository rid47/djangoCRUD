import sys
import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
# from django.utils import
from .forms import *

'###--------------------------READ DATA FROM DB---------------------------------------###'


def contacts(request):
    template = "contacts/all_contacts.html"
    context = {}

    try:
        contacts_list = Contact.objects.filter(delete_status=0)
        # contacts_list2 = Contact.objects.latest('id')
        # print(contacts_list2)
    except Exception as e:
        error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
        messages.error(request, error)
    else:
        context["title"] = "Contact List"
        context["contacts"] = contacts_list
        #print(context)

    finally:
        return render(request, template, context)


'###------------------------------SOFT DELETE------------------------------------------------###'
# path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),


def delete_contact(request, pk):
    try:
        Contact.objects.filter(pk=pk).update(delete_status=1, update_date=datetime.now())
        messages.success(request, "Data Deleted!")
    except Exception as e:
        error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
        messages.error(request, error)
    finally:
        return redirect('contacts:all_contacts')


'###---------------------------------CREATE NEW CONTACT---------------------------------------###'


def create_contact(request):

    form = ContactForm()
    template = "contacts/create_contact.html"
    context = {
        'title': "Create Contact",
        'form': form,
    }
    if request.method == 'POST':

        '# Model_Field_Name: request.POST[form_field_name].strip  //.strip removes any space before or after the input'
        data = {
            'name': request.POST['name'].strip(),
            'email': request.POST['email'].strip(),
            'address':request.POST['address'].strip(),
            'phone':request.POST['phone'].strip()
        }
        #print(data)
        form = ContactForm(data)
        if form.is_valid():
            try:
                '#Model_name.objects.filter(condition)----------------#'

                exist_contact = Contact.objects.filter(name=form.data['name']).exists()
            except Exception as e:
                error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
                messages.error(request, error)
                return render(request, template, context)
            else:
                if exist_contact is True:
                    messages.error(request, 'Name Already Exists!')
                    context = {
                        'title': "Create Contact",
                        'form': form,
                    }
                    return render(request, template, context)
                else:
                    try:
                        form_instance = form.save()
                        form_instance.save()
                        messages.success(request, 'Contact Created!')
                        # return render(request, "wasa_utility/division_type.html", context)
                        return redirect('contacts:all_contacts')
                    except Exception as e:
                        error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
                        messages.error(request, error)
                        return render(request, template, context)
        else:
            # messages.error(request, "Invalid Form Request")
            return HttpResponse(json.dumps(form.errors))
            # return render(request, template, context)
    else:
        return render(request, template, context)


'###--------------------------------------------EDIT EXISTING CONTACT--------------------------------------------###'


def edit_contact(request, pk):
    template = 'contacts/edit_contact.html'
    context = {}
    data = {}
    context["id"] = pk
    try:
        contact = Contact.objects.get(pk=pk)
    except Exception as e:
        error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
        messages.error(request, error)
    else:
        data["name"] = contact.name
        data["email"] = contact.email
        data["address"] = contact.address
        data["phone"] = contact.phone

        if request.method == 'POST':
            data = {
                'name': request.POST['name'].strip(),
                'email': request.POST['email'].strip(),
                'address': request.POST['address'].strip(),
                'phone': request.POST['phone'].strip()


            }
            form = ContactForm(data)
            context["form"] = form
            try:
                # checking if updated name already exists in db (.exclude(pk=pk)clause is for if name is not updated
                # at all)

                exist_name = Contact.objects.filter(name=request.POST['name'], delete_status=0).exclude(pk=pk).exists()
            except Exception as e:
                error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
                messages.error(request, error)
                return render(request, template, context)
            else:   # else condition works if try success
                if exist_name is True:
                    messages.error(request, 'Name Already Exists!')
                    return render(request, template, context)
                else:
                    try:
                        Contact.objects.filter(pk=pk).update(
                            name=request.POST['name'].strip(),
                            email=request.POST['email'].strip(),
                            address=request.POST['address'].strip(),
                            phone=request.POST['phone'].strip(),
                            update_date=datetime.now()

                        )
                        messages.success(request, "Contact Updated!")
                        return redirect('contacts:all_contacts')
                    except Exception as e:
                        error = 'on line {}'.format(sys.exc_info()[-1].tb_lineno), e
                        messages.error(request, error)
                        return render(request, template, context)

# ----------------if request.method != 'POST' then load form with existing info of db------------------------------
#         form = ourform not model (data)
        form = ContactForm(data)
        print(form)
        context["form"] = form
        print(context)
        return render(request, template, context)


# --------------------------------VIEW CONTACT INFO----------------------------#

def profile_info(request,pk):
    user = Contact.objects.get(pk=pk)
    context = {}
    context["profile"] = user
    return render(request, 'contacts/profile.html', context)
