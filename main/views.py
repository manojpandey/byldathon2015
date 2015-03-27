from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from models import Contact, Resource
from forms import ContactForm, RForm





class AddcontactView(FormView):
	form_class = ContactForm
	success_url = "/"
	template_name = 'contact/add.html'

	def form_valid(self, form):
		form.save(commit = True)
		return super(AddcontactView, self).form_valid(form)

class AddresourceView(FormView):
	form_class = RForm
	success_url = "/"
	template_name = 'contact/add.html'

	def form_valid(self, form):
		form.save(commit = True)
		return super(AddresourceView, self).form_valid(form)

class ContactDetailView(DetailView):

    model = Contact
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        return context

		