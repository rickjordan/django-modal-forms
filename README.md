# django-modal-forms

A Python package that seamlessly integrates Django forms within Bootstrap modals.

### Features:
- Django forms within Bootstrap modals
- Adding & editing within single form
- Multiple forms per view page
- Validation & error handling
- Templates for Bootstrap 3 & 4

### Dependencies:
- Django
- Bootstrap
- jQuery

## Installation

- Via [PyPi](https://pypi.org/project/django-modal-forms/):
```
$ pip install django-modal-forms [--upgrade]
```

## Setup

1. Add `modal_forms` & `widget_tweaks` to `INSTALLED_APPS`:
```python
# settings.py

INSTALLED_APPS = [
    'widget_tweaks',
    'modal_forms',
]
```

2. Add endpoint for serialized form data to each app where package will be used:
```python
# urls.py

from . import views

urlpatterns = [
    path('mf-data/<name>/', views.mf_data),
    path('mf-data/<name>/<int:pk>', views.mf_data),
]
```
```python
# views.py

from django.http import HttpResponse
from modal_forms import ModalForm
from . import forms

def mf_data(request, name, pk=None):
    form = getattr(forms, name)()
    mf = ModalForm(form, request, pk)
    data = mf.serialize_form()
    return HttpResponse(data)
```

3. Add script reference & hidden inputs to base template of each app where package will be used:
```html
<!-- base.html -->

<script src="{% static "modal_forms/js/script.js" %}"></script>
<input type="hidden" id="mf-url-base" value="/mf-data">
	
{% if invalid_form %}
<input
    type="hidden"
    id="mf-error"
    data-mf_name="{{ invalid_form.name }}"
    data-mf_pk="{{ invalid_form.pk }}"
>
{% endif %}
```

## Basic Usage

1. Add forms & handlers to views methods:
```python
# views.py

from django.shortcuts import render
from modal_forms import ModalForm
from . import forms, models

def view(request):
    entities = models.Entity.objects.all()
    invalid_form = None

    page_forms = {
        'entity': forms.EntityForm(auto_id="EntityForm_%s"),
    }
    
    if request.POST:
        name = request.POST.get('mf-name', None)
        pk = request.POST.get('mf-pk', None)

        mf = ModalForm(page_forms[name], request, pk)
        page_forms[name], invalid_form = mf.process_form()

    context = {
        'forms': page_forms,
        'invalid_form': invalid_form,
        'entities': entities,
    }

    return render(request, 'view.html', context)
```

2. Add form triggers & modals to templates:
```html
<!-- view.html -->

<button
    class="btn btn-primary mf-btn"
    data-mf_name="EntityForm"
    data-mf_pk="0"
>
    Add Entity
</button>

{% for e in entities %}
<button
    class="btn btn-primary mf-btn"
    data-mf_name="EntityForm"
    data-mf_pk="{{ e.id }}"
>
    Edit Entity
</button>
{% endfor %}

<div class="modal" id="mf-EntityForm" tabindex="-1" role="dialog">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">
                    <span class="mf-action-label"></span>
                    Entity
                </h5>
                <button type="button" class="close" data-dismiss="modal">
                    <span>&times;</span>
                </button>
            </div>

            <form method="post" action="">
                {% csrf_token %}

                <input type="hidden" name="mf-name" value="entity">
                <input type="hidden" name="mf-pk" value="">

                <div class="modal-body">
                    {% include "modal_forms/bootstrap4/form_horizontal.html" with form=forms.entity col_label=4 col_field=8 %}
                </div>

                <div class="modal-footer text-right">
                    <button type="submit" class="btn btn-primary">
                        Submit
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
```

## Advanced Usage

- Setting default field values:
```html
<!-- view.html -->

<button
    class="btn btn-primary mf-btn"
    data-mf_name="EntityForm"
    data-mf_pk="0"
    data-mf_defaults='{"form_field_1":"default-value-1","form_field_2":"default-value-2"}'
>
    Add Entity
</button>
```

- Excluding fields from serialization:

```html
<!-- view.html -->

<button
    class="btn btn-primary mf-btn"
    data-mf_name="EntityForm"
    data-mf_pk="0"
    data-mf_excluded='["form_field_1","form_field_2"]'
>
    Add Entity
</button>
```

## Development

- Starting example app server:
```
$ python example/manage.py runserver
```

- Building package:
```
$ python setup.py sdist bdist_wheel
```

- Installing package locally:
```
$ pip install dist/django-modal-forms-[VERSION].tar.gz [--upgrade]
```

- Uploading package to PyPI:
```
$ twine upload --skip-existing dist/*
```

## References
- [Bootstrap Forms](https://getbootstrap.com/docs/4.0/components/forms/)
- [Django Forms](https://docs.djangoproject.com/en/3.1/topics/forms/)
- [Django Reusable Apps](https://docs.djangoproject.com/en/3.1/intro/reusable-apps/)
- [Python Packaging Projects](https://packaging.python.org/tutorials/packaging-projects/)
