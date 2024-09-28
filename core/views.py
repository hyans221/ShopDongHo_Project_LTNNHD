from audioop import reverse
from datetime import timezone
import datetime
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import DonHangForm, LoginForm, SigninForm
from core.models import ChiTietDonHang, Menu,DanhMucSanPham,DanhMucThuongHieu,SanPham,ChiTietSanPham,Cart,Account,LoaiSanPham,ThuongHieuSanPham,Roles
from datetime import date
from django.views.decorators.cache import never_cache
from decimal import Decimal
@never_cache

def home(request):
    menus = Menu.objects.all()
    danh_mucs = DanhMucThuongHieu.objects.all()
    danh_muc_san_phams = DanhMucSanPham.objects.all()
    data = {
        'menus': menus,
        'danh_mucs': danh_mucs,
        'danh_muc_san_phams': danh_muc_san_phams,
    }
    return render(request, 'pages/home.html', data)

def cart(request):
    menus = Menu.objects.all()
    danh_mucs = DanhMucThuongHieu.objects.all()
    danh_muc_san_phams = DanhMucSanPham.objects.all()
    user_id = request.session.get('user_id')
    total_price = Decimal('0')
    product_list = []

    if user_id:
        cart_items = Cart.objects.filter(NguoiDung_id=user_id)

        for cart_item in cart_items:
            product = get_object_or_404(SanPham, MaSP=cart_item.SanPham_id)
            item_quantity = cart_item.SoLuong

            product_info = {
                'id': product.MaSP,
                'name': product.TenSP,
                'price': float(product.GiaBan),
                'price_sale': float(product.GiaGiam),
                'quantity': item_quantity,
            }
            product_list.append(product_info)

            if product.GiaGiam != 0:
                total_price += Decimal(product.GiaGiam) * item_quantity
            else:
                total_price += Decimal(product.GiaBan) * item_quantity

    request.session['total_price'] = float(total_price)

    data = {
        'menus': menus,
        'danh_mucs': danh_mucs,
        'danh_muc_san_phams': danh_muc_san_phams,
        'product_list': product_list,
        'total_price': total_price,
    }
    return render(request, 'pages/cart.html', data)
def product(request,MaSP):
    menus = Menu.objects.all()
    danh_mucs = DanhMucThuongHieu.objects.all()
    danh_muc_san_phams = DanhMucSanPham.objects.all()
    product = SanPham.objects.get(MaSP=MaSP)
    product_details = ChiTietSanPham.objects.filter(MaSP=product.MaSP)
    thuonghieu = []
    for detail in product_details:
        tenthuonghieu = detail.MaThuongHieu.TenThuongHieu
        thuonghieu.append(tenthuonghieu)
    data = {
        'menus': menus,
        'danh_mucs': danh_mucs,
        'danh_muc_san_phams': danh_muc_san_phams,
        'product': product,
        'product_details':product_details,
        'thuonghieu': thuonghieu,
    }
    return render(request, 'pages/product.html', data)

def add_to_cart(request, MaSP):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            id = MaSP
            num = request.POST.get('num')
            proDetails = get_object_or_404(SanPham, MaSP=id)
            cart_item, created = Cart.objects.get_or_create(NguoiDung_id=user_id, SanPham_id=id)
            cart_item.SoLuong += int(num)
            cart_item.save()
            cart = request.session.get('cart', {})
            if id in cart.keys():
                itemCart = {
                    'id': proDetails.MaSP,
                    'name': proDetails.TenSP,
                    'price': float(proDetails.GiaBan),
                    'price-sale': float(proDetails.GiaGiam),
                    'num': int(cart[id]['num']) + 1
                }
            else:
                itemCart = {
                    'id': proDetails.MaSP,
                    'name': proDetails.TenSP,
                    'price': float(proDetails.GiaBan),
                    'price-sale': float(proDetails.GiaGiam),
                    'num': num
                }
            cart[id] = itemCart
            request.session['cart'] = cart

            return redirect('product', MaSP=id)
        else:
            return JsonResponse({'status': 'error'})
    else:
        return redirect('login')
    
def remove_from_cart(request, MaSP):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            cart_item = Cart.objects.filter(NguoiDung_id=user_id, SanPham_id=MaSP).first()
            if cart_item:
                cart_item.delete()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Sản phẩm không tồn tại trong giỏ hàng.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Yêu cầu không hợp lệ.'})
    else:
        return redirect('login')

def dat_hang(request):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            form = DonHangForm(request.POST)
            if form.is_valid():
                don_hang = form.save(commit=False)
                user_id = request.session.get('user_id')
                account = get_object_or_404(Account, IDAC=user_id)
                don_hang.IDAC = account
                don_hang.TongTien = request.session.get('total_price', 0)
                don_hang.save()
                cart = request.session.get('cart', {})
                for product_id, item in cart.items():
                    product = get_object_or_404(SanPham, MaSP=product_id)
                    chi_tiet_don_hang = ChiTietDonHang(
                        MaDon=don_hang,
                        MaSP=product,
                        SL=item['num'],
                        Total = Decimal(item['num']) * Decimal(product.GiaGiam) if product.GiaGiam != 0 else Decimal(item['num']) * Decimal(product.GiaBan),
                        GiaBan=product.GiaBan,
                        GiaGiam=product.GiaGiam
                    )
                    chi_tiet_don_hang.save()
                request.session['cart'] = {}
                return redirect('cart')
        else:
            form = DonHangForm()
    else:
        return redirect('login')
    return render(request, 'pages/cart.html', {'form': form})

def login(request):
    form = LoginForm()
    account_name = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Pass']
            accounts = Account.objects.filter(Username=username)
            if accounts.exists():
                for account in accounts:
                    if account.Pass == password:
                        request.session['user_id'] = account.IDAC
                        account_name = account.NameAc
                        return redirect('home')
                form.add_error('Pass', 'Mật khẩu không đúng')
            else:
                form.add_error('Username', 'Tài khoản không tồn tại')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form, 'account_name': account_name})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            role = Roles.objects.get(RoleID=2)
            account.RoleID = role
            account.save()
            return redirect('login')
    else:
        form = SigninForm()
    return render(request, 'pages/signin.html', {'form': form})