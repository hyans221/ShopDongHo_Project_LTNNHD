from datetime import datetime
import os
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

from ShopDongHo import settings
from .forms import *
from core.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

def custom_login_required(login_url='admincustom:admin_login'):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if 'user_id' not in request.session:
                return redirect(login_url)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

@custom_login_required(login_url='admincustom:admin_login')
def dashboard(request):
    return render(request, 'pages_admin/dashboard.html')

# Login - Logout -------------------------------------------------------------
def logout_view(request):
    logout(request)
    return redirect('admincustom:admin_login')

def admin_login(request):
    form = AdminLoginForm()
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Pass']
            try:
                account = Account.objects.get(Username=username)
                if account.Pass == password:
                    request.session['user_id'] = account.IDAC
                    return redirect('admincustom:dashboard')
                else:
                    form.add_error('Pass', 'Mật khẩu không đúng')
            except Account.DoesNotExist:
                form.add_error('Username', 'Tài khoản không tồn tại')
    else:
        form = AdminLoginForm()
    return render(request, 'pages_admin/login.html', {'form': form})

# LOẠI SẢN PHẨM -------------------------------------------------------------
def index_loai_sp(request):
    list_loai_sp = LoaiSanPham.objects.all()
    data = {
        'list_loai_sp': list_loai_sp,
    }
    return render(request, 'pages_admin/LoaiSanPham/index_loai_sp.html', data)

def ThemLoaiSP(request):
    if request.method == 'POST':
        form = LoaiSanPhamForm(request.POST)
        if form.is_valid():
            loai_san_pham = form.save(commit=False)
            loai_san_pham.NguoiTao = request.session.get('user_id')
            loai_san_pham.NgayCapNhat = datetime.now()
            loai_san_pham.save()
            messages.success(request, 'Thêm loại sản phẩm thành công.')
            return redirect('admincustom:index_loai_sp')
    else:
        form = LoaiSanPhamForm(initial={'NguoiTao': request.session.get('user_id')})
    return render(request, 'pages_admin/LoaiSanPham/ThemLoaiSP.html', {'form': form})

def XoaLoaiSP(request, MaLoaiSP):
    if request.method == 'GET':
        loai_sp = LoaiSanPham.objects.get(MaLoaiSP=MaLoaiSP)
        loai_sp.delete()
        messages.success(request, 'Xóa loại sản phẩm thành công.')
        return redirect('admincustom:index_loai_sp')

def SuaLoaiSP(request, MaLoaiSP):
    loai_sp = LoaiSanPham.objects.get(MaLoaiSP = MaLoaiSP)
    form = LoaiSanPhamForm(instance=loai_sp)
    if request.method == 'POST':
        form = LoaiSanPhamForm(request.POST, instance=loai_sp)
        if form.is_valid():
            loai_san_pham = form.save(commit=False)
            loai_san_pham.NguoiCapNhat = request.session.get('user_id')
            loai_san_pham.NgayCapNhat = datetime.now()
            loai_san_pham.save()
            messages.success(request, 'Sửa loại sản phẩm thành công.')
            return redirect('admincustom:index_loai_sp')
        else:
            messages.error(request, 'Sửa loại sản phẩm thất bại.')
    context = {'form' : form}
    return render(request, 'pages_admin/LoaiSanPham/SuaLoaiSP.html', context)

def ChiTietLoaiSP(request, MaLoaiSP):
    loai_sp = get_object_or_404(LoaiSanPham, MaLoaiSP=MaLoaiSP)
    return render(request, 'pages_admin/LoaiSanPham/ChiTietLoaiSP.html', {'loai_sp': loai_sp})

# SẢN PHẨM -------------------------------------------------------------
def index_sp(request):
    list_loai_sp = SanPham.objects.all()
    data = {
        'list_loai_sp': list_loai_sp,
    }
    return render(request, 'pages_admin/SanPham/index_sp.html', data)

def ThemSP(request):
    loai_sp_list = LoaiSanPham.objects.all()
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES)
        if form.is_valid():
            san_pham = form.save(commit=False)
            san_pham.NguoiTao = request.session.get('user_id')
            san_pham.save()
            messages.success(request, 'Thêm sản phẩm thành công.')
            return redirect('admincustom:index_sp')
    else:
        form = SanPhamForm(initial={'NguoiTao': request.session.get('user_id')})
    return render(request, 'pages_admin/SanPham/ThemSP.html', {'form': form, 'loai_sp_list': loai_sp_list})

def XoaSP(request, MaSP):
    if request.method == 'GET':
        sp = SanPham.objects.get(MaSP=MaSP)
        sp.delete()
        messages.success(request, 'Xóa sản phẩm thành công.')
        return redirect('admincustom:index_sp')

def SuaSP(request, MaSP):
    loai_sp_list = LoaiSanPham.objects.all()
    sp = SanPham.objects.get(MaSP = MaSP)
    form = SanPhamForm(instance=sp)
    if request.method == 'POST':
        form = SanPhamForm(request.POST, instance=sp)
        if form.is_valid():
            san_pham = form.save(commit=False)
            san_pham.NguoiCapNhat = request.session.get('user_id')
            san_pham.save()
            messages.success(request, 'Sửa sản phẩm thành công.')
            return redirect('admincustom:index_sp')
        else:
            messages.error(request, 'Sửa sản phẩm thất bại.')
    context = {'form' : form}
    return render(request, 'pages_admin/SanPham/SuaSP.html', {'form': form,'loai_sp_list': loai_sp_list})

def ChiTietSP(request, MaSP):
    sp = get_object_or_404(SanPham, MaSP=MaSP)
    return render(request, 'pages_admin/SanPham/ChiTietSP.html', {'sp': sp})

# Menu -------------------------------------------------------------
# Index, Sua, Xoa, ChiTiet
def ThemMenu(request):    
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm menu thành công.')
            return redirect('admincustom:index_menu')
    else:
        form = MenuForm()
    
    return render(request, 'pages_admin/Menu/ThemMenu.html', {'form': form})

def index_menu(request):
    list_menu = Menu.objects.all()
    data = {
        'list_menu': list_menu,
    }
    return render(request, 'pages_admin/Menu/index_menu.html', data)

def XoaMenu(request, MaMenu):
    if request.method == 'GET':
        menu = Menu.objects.get(MaMenu=MaMenu)
        menu.delete()
        messages.success(request, 'Xóa menu thành công.')
        return redirect('admincustom:index_menu')
    
def SuaMenu(request, MaMenu):
    menu = Menu.objects.get(MaMenu = MaMenu)
    form = MenuForm(instance=menu)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa menu thành công.')
            return redirect('admincustom:index_menu')
    return render(request, 'pages_admin/Menu/SuaMenu.html', {'form': form})

def ChiTietMenu(request, MaMenu):
    menu = get_object_or_404(Menu, MaMenu=MaMenu)
    return render(request, 'pages_admin/Menu/ChiTietMenu.html', {'menu': menu})


#  Danh mục sản phẩm -------------------------------------------------------------
# Index, Sua, Xoa, ChiTiet
def ThemDMSP(request):    
    if request.method == 'POST':
        form = DanhMucSanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm danh mục sp thành công.')
            return redirect('admincustom:index_dmsp')
    else:
        form = DanhMucSanPhamForm()
    
    return render(request, 'pages_admin/DanhMucSanPham/ThemDMSP.html', {'form': form})

def index_dmsp(request):
    list_dmsp = DanhMucSanPham.objects.all()
    data = {
        'list_dmsp': list_dmsp,
    }
    return render(request, 'pages_admin/DanhMucSanPham/index_dmsp.html', data)

def XoaDMSP(request, MaDanhMuc):
    if request.method == 'GET':
        dmsp = DanhMucSanPham.objects.get(MaDanhMuc=MaDanhMuc)
        dmsp.delete()
        messages.success(request, 'Xóa danh mục sản phẩm thành công.')
        return redirect('admincustom:index_dmsp')

def SuaDMSP(request, MaDanhMuc):
    dmsp = DanhMucSanPham.objects.get(MaDanhMuc = MaDanhMuc)
    form = DanhMucSanPhamForm(instance=dmsp)
    if request.method == 'POST':
        form = DanhMucSanPhamForm(request.POST, instance=dmsp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa danh mục sản phẩm thành công.')
            return redirect('admincustom:index_dmsp')
    return render(request, 'pages_admin/DanhMucSanPham/SuaDMSP.html', {'form': form})

def ChiTietDMSP(request, MaDanhMuc):
    dmsp = get_object_or_404(DanhMucSanPham, MaDanhMuc=MaDanhMuc)
    return render(request, 'pages_admin/DanhMucSanPham/ChiTietDMSP.html', {'dmsp': dmsp})



# Danh mục thương hiệu -------------------------------------------------------------
# Index, Sua, Xoa, ChiTiet

def index_dmth(request):
    list_dmth = DanhMucThuongHieu.objects.all()
    data = {
        'list_dmth': list_dmth,
    }
    return render(request, 'pages_admin/DanhMucThuongHieu/index_dmth.html', data)


def ThemDMTH(request):
    loai_mn_list = Menu.objects.all()    
    if request.method == 'POST':
        form = DanhMucThuongHieuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm danh mục th thành công.')
            return redirect('admincustom:index_dmth')
    else:
        form = DanhMucThuongHieuForm()
    
    return render(request, 'pages_admin/DanhMucThuongHieu/ThemDMTH.html', {'form': form, 'loai_mn_list': loai_mn_list})

def XoaDMTH(request, MaDanhMuc):
    if request.method == 'GET':
        dmth = DanhMucThuongHieu.objects.get(MaDanhMuc=MaDanhMuc)
        dmth.delete()
        messages.success(request, 'Xóa danh mục thương hiệu thành công.')
        return redirect('admincustom:index_dmth')
    
def SuaDMTH(request, MaDanhMuc):
    loai_mn_list = Menu.objects.all()  
    dmth = DanhMucThuongHieu.objects.get(MaDanhMuc = MaDanhMuc)
    form = DanhMucThuongHieuForm(instance=dmth)
    if request.method == 'POST':
        form = DanhMucThuongHieuForm(request.POST, instance=dmth)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa danh mục thương hiệu thành công.')
            return redirect('admincustom:index_dmth')
    return render(request, 'pages_admin/DanhMucThuongHieu/SuaDMTH.html', {'form': form, 'loai_mn_list': loai_mn_list})

def ChiTietDMTH(request, MaDanhMuc):
    dmth = get_object_or_404(DanhMucThuongHieu, MaDanhMuc=MaDanhMuc)
    return render(request, 'pages_admin/DanhMucThuongHieu/ChiTietDMTH.html', {'dmth': dmth})


# Chi tiết sản phẩm -------------------------------------------------------------
# Index, Sua, Xoa, ChiTiet
def index_ctsp(request):
    list_ctsp = ChiTietSanPham.objects.all()
    data = {
        'list_ctsp': list_ctsp,
    }
    return render(request, 'pages_admin/ChiTietSanPham/index_ctsp.html', data)

def ThemCTSP(request):
    ma_sp_list = SanPham.objects.all()
    ma_thsp_list = ThuongHieuSanPham.objects.all()
    ma_dm_list = DanhMucSanPham.objects.all()          
    if request.method == 'POST':
        form = ChiTietSanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm ctsp thành công.')
            return redirect('admincustom:index_ctsp')
    else:
        form = ChiTietSanPhamForm()
    
    return render(request, 'pages_admin/ChiTietSanPham/ThemCTSP.html', {'form': form, 'ma_sp_list': ma_sp_list, 'ma_thsp_list': ma_thsp_list, 'ma_dm_list': ma_dm_list})

def XoaCTSP(request, MaChiTietSP):
    if request.method == 'GET':
        ctsp = ChiTietSanPham.objects.get(MaChiTietSP=MaChiTietSP)
        ctsp.delete()
        messages.success(request, 'Xóa chi tiết sản phẩm thành công.')
        return redirect('admincustom:index_ctsp')
    
def SuaCTSP(request, MaChiTietSP):
    ma_sp_list = SanPham.objects.all()
    ma_thsp_list = ThuongHieuSanPham.objects.all()
    ma_dm_list = DanhMucSanPham.objects.all()   
    ctsp = ChiTietSanPham.objects.get(MaChiTietSP = MaChiTietSP)
    form = ChiTietSanPhamForm(instance=ctsp)
    if request.method == 'POST':
        form = ChiTietSanPhamForm(request.POST, instance=ctsp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa chi tiết sản phẩm thành công.')
            return redirect('admincustom:index_ctsp')
    return render(request, 'pages_admin/ChiTietSanPham/SuaCTSP.html', {'form': form, 'ma_sp_list': ma_sp_list, 'ma_thsp_list': ma_thsp_list, 'ma_dm_list': ma_dm_list})

def ChiTietCTSP(request, MaChiTietSP):
    ctsp = get_object_or_404(ChiTietSanPham, MaChiTietSP=MaChiTietSP)
    return render(request, 'pages_admin/ChiTietSanPham/ChiTietCTSP.html', {'ctsp': ctsp})

# Thương hiệu sản phẩm -------------------------------------------------------------
# Index, Sua, Xoa, ChiTiet

def index_thsp(request):
    list_thsp = ThuongHieuSanPham.objects.all()
    data = {
        'list_thsp': list_thsp,
    }
    return render(request, 'pages_admin/ThuongHieuSanPham/index_thsp.html', data)

def ThemTHSP(request):
    ma_dm_list = DanhMucThuongHieu.objects.all()
    if request.method == 'POST':
        form = ThuongHieuSanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm thsp thành công.')
            return redirect('admincustom:index_thsp')
    else:
        form = ThuongHieuSanPhamForm()
    
    return render(request, 'pages_admin/ThuongHieuSanPham/ThemTHSP.html', {'form': form, 'ma_dm_list': ma_dm_list})

def XoaTHSP(request, MaThuongHieu):
    if request.method == 'GET':
        thsp = ThuongHieuSanPham.objects.get(MaThuongHieu=MaThuongHieu)
        thsp.delete()
        messages.success(request, 'Xóa thương hiệu sản phẩm thành công.')
        return redirect('admincustom:index_thsp')
    
def SuaTHSP(request, MaThuongHieu):
    ma_dm_list = DanhMucThuongHieu.objects.all()
    thsp = ThuongHieuSanPham.objects.get(MaThuongHieu = MaThuongHieu)
    form = ThuongHieuSanPhamForm(instance=thsp)
    if request.method == 'POST':
        form = ThuongHieuSanPhamForm(request.POST, instance=thsp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa thương hiệu sản phẩm thành công.')
            return redirect('admincustom:index_thsp')
    return render(request, 'pages_admin/ThuongHieuSanPham/SuaTHSP.html', {'form': form, 'ma_dm_list': ma_dm_list})

def ChiTietTHSP(request, MaThuongHieu):
    thsp = get_object_or_404(ThuongHieuSanPham, MaThuongHieu=MaThuongHieu)
    return render(request, 'pages_admin/ThuongHieuSanPham/ChiTietTHSP.html', {'thsp': thsp})


# ĐƠN HÀNG -------------------------------------------------------------
def index_dh(request):
    list_dh = DonDatHang.objects.all()
    data = {
        'list_dh': list_dh,
    }
    return render(request, 'pages_admin/DonHang/index_dh.html', data)


def XoaDH(request, MaDon):
    if request.method == 'GET':
        dh = DonDatHang.objects.get(MaDon=MaDon)
        dh.delete()
        messages.success(request, 'Xóa đơn hàng thành công.')
        return redirect('admincustom:index_dh')
    
def SuaDH(request, MaDon):
    dh = DonDatHang.objects.get(MaDon = MaDon)
    form = DonDatHangForm(instance=dh)
    if request.method == 'POST':
        form = DonDatHangForm(request.POST, instance=dh)
        if form.is_valid():
            don_dat_hang = form.save(commit=False)
            # don_dat_hang.NguoiCapNhat = request.session.get('user_id')
            don_dat_hang.save()
            messages.success(request, 'Sửa đơn hàng thành công.')
            return redirect('admincustom:index_dh')
        else:
            messages.error(request, 'Sửa đơn hàng thất bại.')
    context = {'form' : form}
    return render(request, 'pages_admin/DonHang/SuaDH.html', {'form' : form})

def ChiTietDH(request, MaDon):
    dh = get_object_or_404(DonDatHang, MaDon=MaDon)
    return render(request, 'pages_admin/DonHang/ChiTietDH.html', {'dh': dh})

# Tài khoản -------------------------------------------------------------
def index_tk(request):
    list_tk = Account.objects.all()
    data = {
        'list_tk': list_tk,
    }
    return render(request, 'pages_admin/TaiKhoan/index_tk.html', data)

def ThemTK(request):
    role_list = Roles.objects.all()
    if request.method == 'POST':
        form = TaiKhoanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm TK thành công.')
            return redirect('admincustom:index_tk')
    else:
        form = TaiKhoanForm()
    return render(request, 'pages_admin/TaiKhoan/ThemTK.html', {'form': form,'role_list':role_list})


def XoaTK(request, IDAC):
    if request.method == 'GET':
        tai_khoan = Account.objects.get(IDAC=IDAC)
        tai_khoan.delete()
        messages.success(request, 'Xóa tài khoản thành công.')
        return redirect('admincustom:index_tk')
    else:
        return HttpResponse("Invalid request method") 

def SuaTK(request, IDAC):
    role_list = Roles.objects.all()
    tai_khoan = Account.objects.get(IDAC=IDAC)
    form = TaiKhoanForm(instance=tai_khoan)
    if request.method == 'POST':
        form = TaiKhoanForm(request.POST, instance=tai_khoan)
        if form.is_valid():
            tai_khoan = form.save(commit=False)
            form.save()
            messages.success(request, 'Sửa tài khoản thành công.')
            return redirect('admincustom:index_tk')
    return render(request, 'pages_admin/TaiKhoan/SuaTK.html', {'form': form, 'role_list':role_list})

def ChiTietTK(request, IDAC):
    tai_khoan = get_object_or_404(Account, IDAC=IDAC)
    return render(request, 'pages_admin/TaiKhoan/ChiTietTK.html', {'tai_khoan': tai_khoan})


# Phân quyền -------------------------------------------------------------
def index_pq(request):
    list_pq = Roles.objects.all()
    data = {
        'list_pq': list_pq,
    }
    return render(request, 'pages_admin/PhanQuyen/index_pq.html', data)

def ThemPQ(request):
    if request.method == 'POST':
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm phân quyền thành công.')
            return redirect('admincustom:index_pq')
    else:
        form = RolesForm()
    return render(request, 'pages_admin/PhanQuyen/ThemPQ.html', {'form': form})

def XoaPQ(request, RoleID):
    if request.method == 'POST':
        phan_quyen = Roles.objects.get(RoleID=RoleID)
        phan_quyen.delete()
        messages.success(request, 'Xóa phân quyền thành công.')
        return redirect('admincustom:index_pq')

def SuaPQ(request, RoleID):
    phan_quyen = Roles.objects.get(RoleID=RoleID)
    form = RolesForm(instance=phan_quyen)
    if request.method == 'POST':
        form = RolesForm(request.POST, instance=phan_quyen)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa phân quyền thành công.')
            return redirect('admincustom:index_pq')
    return render(request, 'pages_admin/PhanQuyen/SuaPQ.html', {'form': form})

def ChiTietPQ(request, RoleID):
    phan_quyen = get_object_or_404(Roles, RoleID=RoleID)
    return render(request, 'pages_admin/PhanQuyen/ChiTietPQ.html', {'phan_quyen': phan_quyen})


# Chi tiết đơn hàng -------------------------------------------------------------
def index_ctdh(request):
    list_ctdh = ChiTietDonHang.objects.all()
    data = {
        'list_ctdh': list_ctdh,
    }
    return render(request, 'pages_admin/ChiTietDH/index_ctdh.html', data)

def ThemCTDH(request):
    if request.method == 'POST':
        form = ChiTietDonHangForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm chi tiết đơn hàng thành công.')
            return redirect('admincustom:index_ctdh')
    else:
        form = ChiTietDonHangForm()
    return render(request, 'pages_admin/ChiTietDH/ThemCTDH.html', {'form': form})

def XoaCTDH(request, MaCTDH):
    if request.method == 'GET':
        ctdh = ChiTietDonHang.objects.get(MaCTDH=MaCTDH)
        ctdh.delete()
        messages.success(request, 'Xóa chi tiết đơn hàng thành công.')
        return redirect('admincustom:index_ctdh')
    
def SuaCTDH(request, MaCTDH):
    ctdh = ChiTietDonHang.objects.get(MaCTDH = MaCTDH)
    form = ChiTietDonHangForm(instance=ctdh)
    if request.method == 'POST':
        form = ChiTietDonHangForm(request.POST, instance=ctdh)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa chi tiết đơn hàng thành công.')
            return redirect('admincustom:index_ctdh')
    return render(request, 'pages_admin/ChiTietDH/SuaCTDH.html', {'form': form})

def ChiTietCTDH(request, MaCTDH):
    ctdh = get_object_or_404(ChiTietDonHang, MaCTDH=MaCTDH)
    return render(request, 'pages_admin/ChiTietDH/ChiTietCTDH.html', {'ctdh': ctdh})



# -----------------------------------------------------------------