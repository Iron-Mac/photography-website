from django import template

register = template.Library()

@register.inclusion_tag("registration/partials/active_menu.html")
def ActiveMenu(request, link_name, content):
    return{
        "requset":request,
        "link_name":link_name,
        "link":f"account:{link_name}",
        "content":content
    }