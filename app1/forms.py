from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea)
    project_name = forms.CharField(label="Project name")


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name project", max_length=200)


class DeleteProject(forms.Form):
    name = forms.CharField(label="Name project", max_length=200)


class DeleteTask(forms.Form):
    title = forms.CharField(label="Title task", max_length=200)
