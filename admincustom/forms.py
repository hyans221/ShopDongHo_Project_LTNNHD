from django import forms
from core.models import *

class LoaiSanPhamForm(forms.ModelForm):
    class Meta:
        model = LoaiSanPham
        fields = ['MaLoaiSP', 'TenLoaiSP', 'SoLuong']
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaLoaiSP = cleaned_data.get('MaLoaiSP')
    #     TenLoaiSP = cleaned_data.get('TenLoaiSP')
    #     if MaLoaiSP and TenLoaiSP:
    #         if LoaiSanPham.objects.filter(MaLoaiSP=MaLoaiSP).exists():
    #             self.add_error('MaLoaiSP', 'Mã Loại Sản Phẩm đã tồn tại.')
    #         if LoaiSanPham.objects.filter(TenLoaiSP=TenLoaiSP).exists():
    #             self.add_error('TenLoaiSP', 'Tên Loại Sản Phẩm đã tồn tại.')
    

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['MaSP', 'MaLoaiSP', 'TenSP', 'HinhAnh', 'MoTa', 'SoLuong', 'GiaBan', 'GiaGiam', 'NguoiTao', 'TrangThai']
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaSP = cleaned_data.get('MaSP')
    #     TenSP = cleaned_data.get('TenSP')
    #     if MaSP and TenSP:
    #         if SanPham.objects.filter(MaSP=MaSP).exists():
    #             self.add_error('MaSP', 'Mã Sản Phẩm đã tồn tại.')
    #         if SanPham.objects.filter(TenSP=TenSP).exists():
    #             self.add_error('TenSP', 'Tên Sản Phẩm đã tồn tại.')

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaMenu = cleaned_data.get('MaMenu')
    #     TenMenu = cleaned_data.get('TenMenu')
    #     if MaMenu and TenMenu:
    #         if Menu.objects.filter(MaMenu=MaMenu).exists():
    #             self.add_error('MaMenu', 'Mã Menu đã tồn tại.')
    #         if Menu.objects.filter(TenMenu=TenMenu).exists():
    #             self.add_error('TenMenu', 'Tên Menu đã tồn tại.')

class DanhMucSanPhamForm(forms.ModelForm):
    class Meta:
        model = DanhMucSanPham
        fields = '__all__'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaDanhMuc = cleaned_data.get('MaDanhMuc')
    #     TenDanhMuc = cleaned_data.get('TenDanhMuc')
    #     if MaDanhMuc and TenDanhMuc:
    #         if DanhMucSanPham.objects.filter(MaDanhMuc=MaDanhMuc).exists():
    #             self.add_error('MaDanhMuc', 'Mã Danh Mục đã tồn tại.')
    #         if DanhMucSanPham.objects.filter(TenDanhMuc=TenDanhMuc).exists():
    #             self.add_error('TenDanhMuc', 'Tên Danh Mục đã tồn tại.')

class DanhMucThuongHieuForm(forms.ModelForm):
    class Meta:
        model = DanhMucThuongHieu
        fields = '__all__'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaDanhMuc = cleaned_data.get('MaDanhMuc')
    #     TenDanhMuc = cleaned_data.get('TenDanhMuc')
    #     if MaDanhMuc and TenDanhMuc:
    #         if DanhMucThuongHieu.objects.filter(MaDanhMuc=MaDanhMuc).exists():
    #             self.add_error('MaDanhMuc', 'Mã Danh Mục đã tồn tại.')
    #         if DanhMucThuongHieu.objects.filter(TenDanhMuc=TenDanhMuc).exists():
    #             self.add_error('TenDanhMuc', 'Tên Danh Mục đã tồn tại.')

class ChiTietSanPhamForm(forms.ModelForm):
    class Meta:
        model = ChiTietSanPham
        fields = '__all__'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaChiTietSP = cleaned_data.get('MaChiTietSP')
    #     if MaChiTietSP:
    #         if ChiTietSanPham.objects.filter(MaChiTietSP=MaChiTietSP).exists():
    #             self.add_error('MaDanhMuc', 'Mã CTSP đã tồn tại.')
                
class ThuongHieuSanPhamForm(forms.ModelForm):
    class Meta:
        model = ThuongHieuSanPham
        fields = '__all__'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     MaThuongHieu = cleaned_data.get('MaThuongHieu')
    #     TenThuongHieu = cleaned_data.get('TenThuongHieu')
    #     if MaThuongHieu and TenThuongHieu:
    #         if ThuongHieuSanPham.objects.filter(MaThuongHieu=MaThuongHieu).exists():
    #             self.add_error('MaThuongHieu', 'Mã Thương Hiệu đã tồn tại.')
    #         if ThuongHieuSanPham.objects.filter(TenThuongHieu=TenThuongHieu).exists():
    #             self.add_error('TenThuongHieu', 'Tên Thương Hiệu đã tồn tại.')

class TaiKhoanForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     Username = cleaned_data.get('Username')
    #     Email = cleaned_data.get('Email')
    #     Phone = cleaned_data.get('Phone')
    #     if Username and Email and Phone:
    #         if Account.objects.filter(Username=Username).exists():
    #             self.add_error('Username', 'Username đã tồn tại.')
    #         if Account.objects.filter(Email=Email).exists():
    #             self.add_error('Email', 'Email đã tồn tại.')
    #         if Account.objects.filter(Phone=Phone).exists():
    #             self.add_error('Phone', 'Phone đã tồn tại.')


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = fields = ['Username', 'Pass']

class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'

# ------------------------------------------
# Đơn hàng
class DonDatHangForm(forms.ModelForm):
    class Meta:
        model = DonDatHang
        fields = ['MaDon', 'IDAC', 'Deleted', 'SDT', 'TongTien', 'NgayDat', 'NgayGiao', 'TransactStatusID', 'DiaChi']


class ChiTietDonHangForm(forms.ModelForm):
    class Meta:
        model = ChiTietDonHang
        fields = ['MaCTDH', 'MaDon', 'MaSP', 'SL', 'Total', 'GiaBan', 'GiaGiam']

