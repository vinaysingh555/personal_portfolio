from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from django.core.mail import send_mail





class Home(View):
    def get(self, request):
        return render(request, "index.html")


# =========================
# CONTACT FORM
# =========================




class ContactView(View):
    def post(self, request):

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        send_mail(
            subject=f"Portfolio Contact: {subject}",
            message=f"""
New message from your portfolio

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
""",
            from_email='vinaysinghh7976@gmail.com',
            recipient_list=['vinaysinghh7976@gmail.com'],
            fail_silently=False,
        )

        return redirect('/?success=1#contact')

# =========================
# ADMIN LOGIN
# =========================

class AdminLogin(View):

    def get(self, request):
        return render(request, "admin_login.html")

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password == "vinays":
            request.session['admin'] = True
            return redirect('dashboard')

        return render(request, "admin_login.html")


# =========================
# ADMIN DASHBOARD
# =========================

class Dashboard(View):

    def get(self, request):

        if not request.session.get('admin'):
            return redirect('admin_login')

        data = Contact.objects.all()

        return render(request, "dashboard.html", {'data': data})


# =========================
# VIEW CONTACT
# =========================

class ViewContact(View):

    def get(self, request, id):

        if not request.session.get('admin'):
            return redirect('admin_login')

        data = Contact.objects.get(id=id)

        return render(request, "view.html", {'data': data})


# =========================
# EDIT CONTACT
# =========================

class EditContact(View):

    def get(self, request, id):

        if not request.session.get('admin'):
            return redirect('admin_login')

        data = Contact.objects.get(id=id)

        return render(request, 'edit.html', {'data': data})

    def post(self, request, id):

        if not request.session.get('admin'):
            return redirect('admin_login')

        data = Contact.objects.get(id=id)

        data.name = request.POST['name']
        data.email = request.POST['email']
        data.subject = request.POST['subject']
        data.message = request.POST['message']

        data.save()

        return redirect('dashboard')


# =========================
# DELETE CONTACT
# =========================

class DeleteContact(View):

    def get(self, request, id):

        if not request.session.get('admin'):
            return redirect('admin_login')

        Contact.objects.get(id=id).delete()

        return redirect('dashboard')