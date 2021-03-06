from datetime import date
import json

class ModalForm:
    def __init__(self, form, request, pk=0):
        self.form = form.__class__
        self.request = request
        
        self.name = self.form.__name__
        self.auto_id_format = "{}_%s"
        self.date_format = "%m/%d/%Y"
        
        self.instance = None
        self.bound_form = None
        self.invalid_form = None
        self.is_valid = False

        # setup model instance
        if pk and pk != "0": # get existing
            self.instance = form.Meta.model.objects.get(id=pk)
        else: # create new
            self.instance = form.Meta.model()
            
        # setup form instance
        self.bound_form = self.form(self.request.POST,
            instance=self.instance, auto_id=self.get_auto_id())

    def get_auto_id(self):
        return self.auto_id_format.format(self.name)

    def get_signature(self):
        return {
            'name': self.name,
            'pk': self.instance.id if self.instance.id else 0,
        }

    def process_form(self, commit=True):
        # validate form & save instance
        if self.bound_form.is_valid():
            self.instance = self.bound_form.save(commit=commit)
            self.is_valid = True
        else:
            self.invalid_form = self.get_signature()
            
        return self.bound_form, self.invalid_form

    def serialize_form(self):
        form = self.form(instance=self.instance, auto_id=self.get_auto_id())
        fields = {}

        for field in form:
            if hasattr(field.field, 'fields'): # field has sub-values
                widget = field.field.widget
                value = getattr(form.instance, field.name)
                sub_values = widget.decompress(value)

                for i, sub_value in enumerate(sub_values):
                    auto_id = "{}_{}".format(field.auto_id, i)
                    fields[auto_id] = self.serialize_value(sub_value)
            else:
                fields[field.auto_id] = self.serialize_value(field.value())

        return json.dumps(fields)

    def serialize_value(self, value):
        if not value or type(value) is bool:
            return value

        if type(value) is date:
            return value.strftime(self.date_format)

        return str(value)
