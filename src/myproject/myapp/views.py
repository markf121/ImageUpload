# -*coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

def list(request):
    #Handle image upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(userImage = request.FILES['userImage'])
            newdoc.save() #saves to default directory: /media/

            # Redirect to list view of uploaded images after image has been uploaded
            return HttpResponseRedirect(reverse('myapp.views.list'))

    else:
        form = DocumentForm() #empty form

    #Load uploaded images
    documents = Document.objects.all()

    #Send images to list.html and render form

    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
        )


# # -*- coding: utf-8 -*-
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

# from myproject.myapp.models import Document
# from myproject.myapp.forms import DocumentForm

# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])
#             newdoc.save()
            
#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
#     else:
#         form = DocumentForm() # A empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     return render_to_response(
#         'list.html',
#         {'documents': documents, 'form': form},
#         context_instance=RequestContext(request)
#     )
