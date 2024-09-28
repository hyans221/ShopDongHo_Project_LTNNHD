from django import template
from core.models import SanPham
from django.shortcuts import get_object_or_404
register = template.Library()

@register.simple_tag(takes_context=True)
def cart_quantity(context):
    cart = context['request'].session.get('cart', {})
    quantity = sum(item.get('quantity', 1) for item in cart.values())
    return quantity

def cart_item(context):
    cart = context['request'].session.get('cart', {})
    product_list = []
    for product_id, item in cart.items():
        product = get_object_or_404(SanPham, MaSP=product_id)
        product_info = {
            'id': product.MaSP,
            'name': product.TenSP,
            'price': float(product.GiaBan),
            'price_sale': float(product.GiaGiam),
            'quantity': item['num'],
        }
        product_list.append(product_info)
    return {'cart_items': product_list}