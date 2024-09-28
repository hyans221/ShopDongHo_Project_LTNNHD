from django.db import models
from django.utils import timezone

class Menu(models.Model):
    MaMenu = models.CharField(max_length=20, primary_key=True)
    TenMenu = models.CharField(max_length=100)
    class Meta:
        app_label = 'core'

class DanhMucThuongHieu(models.Model):
    MaDanhMuc = models.CharField(max_length=20, primary_key=True)
    TenDanhMuc = models.CharField(max_length=100)
    MaMenu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class DanhMucSanPham(models.Model):
    MaDanhMuc = models.CharField(max_length=20, primary_key=True)
    TenDanhMuc = models.CharField(max_length=100)
    Publish = models.IntegerField()

class ThuongHieuSanPham(models.Model):
    MaThuongHieu = models.AutoField(primary_key=True)
    TenThuongHieu = models.CharField(max_length=100)
    MaDanhMuc = models.ForeignKey(DanhMucThuongHieu,on_delete=models.CASCADE)

class LoaiSanPham(models.Model):
    MaLoaiSP = models.CharField(max_length=20, primary_key=True)
    TenLoaiSP = models.CharField(max_length=100)
    SoLuong = models.IntegerField()
    NgayTao = models.DateField(auto_now_add=True)
    NgayCapNhat = models.DateField(blank=True, null=True)
    NguoiTao = models.CharField(max_length=100)
    NguoiCapNhat = models.CharField(max_length=100,null=True)
    
class SanPham(models.Model):
    MaSP = models.CharField(max_length=20, primary_key=True)
    MaLoaiSP = models.ForeignKey(LoaiSanPham, on_delete=models.CASCADE)
    TenSP = models.CharField(max_length=255)
    HinhAnh = models.CharField(max_length=255)
    MoTa = models.TextField()
    SoLuong = models.IntegerField()
    GiaBan = models.DecimalField(max_digits=10, decimal_places=2)
    GiaGiam = models.DecimalField(max_digits=10, decimal_places=2)
    NguoiTao = models.CharField(max_length=100)
    NgayTao = models.DateField(auto_now_add=True)
    NguoiCapNhat = models.CharField(max_length=100)
    NgayCapNhat = models.DateField(blank=True, null=True)
    TrangThai = models.CharField(max_length=100)

class ChiTietSanPham(models.Model):
    MaChiTietSP = models.CharField(max_length=20, primary_key=True)
    MaSP = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    MaThuongHieu = models.ForeignKey(ThuongHieuSanPham,on_delete=models.CASCADE)
    XuatXu = models.CharField(max_length=100)
    DongMay = models.CharField(max_length=100)
    ChatLieu = models.CharField(max_length=100)
    PhongCach = models.CharField(max_length=100)
    DoiTuong = models.CharField(max_length=100)
    MaDanhMuc = models.ForeignKey(DanhMucSanPham, on_delete=models.CASCADE)

class Roles(models.Model):
    RoleID = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=100)
    Decription = models.CharField(max_length=100)

class Account(models.Model):
    IDAC = models.AutoField(primary_key=True)
    NameAc = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Pass = models.CharField(max_length=100)
    Avatar = models.CharField(max_length=100)
    NgaySinh = models.DateField(blank=True, null=True)
    DiaChi = models.CharField(max_length=100)
    NgayTao = models.DateField(auto_now_add=True)
    GioiTinh = models.CharField(max_length=10)
    Salt = models.CharField(max_length=10)
    RoleID = models.ForeignKey(Roles, on_delete=models.CASCADE)

class TrangThaiGiaoHang(models.Model):
    TransactStatusID = models.IntegerField(primary_key=True)
    Status = models.CharField(max_length=100)
    Decription = models.CharField(max_length=100)

class DonDatHang(models.Model):
    MaDon = models.AutoField(primary_key=True)
    IDAC = models.ForeignKey(Account, on_delete=models.CASCADE)
    Deleted = models.IntegerField(default=0)
    SDT = models.CharField(max_length=100)
    TongTien = models.DecimalField(max_digits=10, decimal_places=2)
    NgayDat = models.DateField(default=timezone.now)
    NgayGiao = models.DateField(blank=True, null=True)
    TransactStatusID = models.ForeignKey(TrangThaiGiaoHang, on_delete=models.CASCADE, default=1)
    DiaChi = models.CharField(max_length=100)

class ChiTietDonHang(models.Model):
    MaCTDH = models.AutoField(primary_key=True)
    MaDon = models.ForeignKey(DonDatHang, on_delete=models.CASCADE)
    MaSP = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SL = models.IntegerField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    GiaBan = models.DecimalField(max_digits=10, decimal_places=2)
    GiaGiam = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    NguoiDung = models.ForeignKey(Account, on_delete=models.CASCADE)
    SanPham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SoLuong = models.PositiveIntegerField(default=0)
    NgayTao  = models.DateTimeField(default=timezone.now)
