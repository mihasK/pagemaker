__author__ = 'robert'
from django import template

register = template.Library()

@register.inclusion_tag('form-video.html',takes_context=True)
def upload_form(context, klass=''):
    form_url = context.dicts[2]['request'].path
    form = context.dicts[1]['form']

    if context.dicts[1].get('form_url', None):
        form_url = context.dicts[1]['form_url']
    if context.dicts[1].get('upload_form', None):
        form = context.dicts[1]['upload_form']
    return {'klass':klass,
            'form_url':form_url,
            'form':context.dicts[1]['form']}

@register.inclusion_tag('form-embed.html', takes_context=True)
def embed_form(context):
    form_url = context.dicts[2]['request'].path
    form = context.dicts[1]['form']

    if context.dicts[1].get('form_url', None):
        form_url = context.dicts[1]['form_url']
    if context.dicts[1].get('upload_form', None):
        form = context.dicts[1]['upload_form']

    return {'form':form,
            'form_url': form_url}

@register.inclusion_tag('submit-button.html')
def submit_button():
    pass

@register.inclusion_tag('delete-form.html',takes_context=True)
def delete_form(context):
    form_url = context.dicts[2]['request'].path
    return {'form_url':form_url}


@register.filter
def split_string(value):
    return value.split(' ')

