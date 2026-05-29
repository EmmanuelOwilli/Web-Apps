# Import required Django functions
from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedFile
from .forms import UploadFileForm


# Home page view
def home(request):

    # Get all uploaded files
    files = UploadedFile.objects.all()

    # Send files to home page
    return render(request, "home.html", {"files": files})


# Upload page view
def upload_file(request):

    # Check if form is submitted
    if request.method == "POST":

        # Create form with submitted data
        form = UploadFileForm(request.POST, request.FILES)

        # Validate form
        if form.is_valid():

            # Save uploaded file
            form.save()

            # Redirect to home page
            return redirect("/")

    else:

        # Create empty form
        form = UploadFileForm()

    # Show upload page
    return render(request, "upload.html", {"form": form})


# Delete file view
def delete_file(request, file_id):

    # Get file by ID
    file = get_object_or_404(UploadedFile, id=file_id)

    # Delete file
    file.delete()

    # Redirect back home
    return redirect("/")
