from django.shortcuts import render, redirect
from django.views import View
from .models import Contact


class Home(View):
    def get(self, request):
        return render(request, "home.html")


class About(View):
    def get(self, request):
        return render(request, "about.html")


class Skills(View):
    def get(self, request):
        return render(request, "skills.html")


class Resume(View):
    def get(self, request):
        return render(request, "resume.html")


class ContactView(View):

    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):

        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )

        return redirect('contact')


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


class Dashboard(View):

    def get(self, request):

        if not request.session.get('admin'):
            return redirect('admin_login')

        data = Contact.objects.all()

        return render(request, "dashboard.html", {'data': data})


class ViewContact(View):

    def get(self, request, id):

        if not request.session.get('admin'):
            return redirect('admin_login')

        data = Contact.objects.get(id=id)

        return render(request, "view.html", {'data': data})

class EditContact(View):

    def get(self, request, id):

        data = Contact.objects.get(id=id)

        return render(request, 'edit.html', {'data': data})

    def post(self, request, id):

        data = Contact.objects.get(id=id)

        data.name = request.POST['name']
        data.email = request.POST['email']
        data.subject = request.POST['subject']
        data.message = request.POST['message']

        data.save()

        return redirect('dashboard')
class DeleteContact(View):

    def get(self, request, id):

        if not request.session.get('admin'):
            return redirect('admin_login')

        Contact.objects.get(id=id).delete()

        return redirect('dashboard')