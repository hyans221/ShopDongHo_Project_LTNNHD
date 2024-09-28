from django.urls import path
from admincustom.views import *
from django.conf.urls.static import static

app_name = 'admincustom'

urlpatterns = [

    path('login/', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),

    # ----------------- Loại sản phẩm -----------------
    path('LoaiSanPham/index_loai_sp', index_loai_sp, name='index_loai_sp'),
    path('LoaiSanPham/ThemLoaiSP', ThemLoaiSP, name='ThemLoaiSP'),
    path('LoaiSanPham/SuaLoaiSP/<str:MaLoaiSP>/', SuaLoaiSP, name='SuaLoaiSP'),
    path('LoaiSanPham/ChiTietLoaiSP/<str:MaLoaiSP>/', ChiTietLoaiSP, name='ChiTietLoaiSP'),
    path('LoaiSanPham/XoaLoaiSP/<str:MaLoaiSP>/', XoaLoaiSP, name='XoaLoaiSP'),
    # ----------------- Sản phẩm -----------------
    path('SanPham/index_sp', index_sp, name='index_sp'),
    path('SanPham/ThemSP', ThemSP, name='ThemSP'),
    path('SanPham/SuaSP/<str:MaSP>/', SuaSP, name='SuaSP'),
    path('SanPham/ChiTietSP/<str:MaSP>/', ChiTietSP, name='ChiTietSP'),
    path('SanPham/XoaSP/<str:MaSP>/', XoaSP, name='XoaSP'),
    # ----------------- Menu -----------------
    path('Menu/ThemMenu', ThemMenu, name='ThemMenu'),
    path('Menu/index_menu', index_menu, name='index_menu'),
    path('Menu/SuaMenu/<str:MaMenu>/', SuaMenu, name='SuaMenu'),
    path('Menu/ChiTietMenu/<str:MaMenu>/', ChiTietMenu, name='ChiTietMenu'),
    path('Menu/XoaMenu/<str:MaMenu>/', XoaMenu, name='XoaMenu'),
    # ----------------- Danh mục sản phẩm -----------------
    path('DanhMucSanPham/ThemDMSP', ThemDMSP, name='ThemDMSP'),
    path('DanhMucSanPham/index_dmsp', index_dmsp, name='index_dmsp'),
    path('DanhMucSanPham/SuaDMSP/<str:MaDanhMuc>/', SuaDMSP, name='SuaDMSP'),
    path('DanhMucSanPham/ChiTietDMSP/<str:MaDanhMuc>/', ChiTietDMSP, name='ChiTietDMSP'),
    path('DanhMucSanPham/XoaDMSP/<str:MaDanhMuc>/', XoaDMSP, name='XoaDMSP'),
    # ----------------- Chi tiết sản phẩm -----------------
    path('ChiTietSanPham/ThemCTSP', ThemCTSP, name='ThemCTSP'),
    path('ChiTietSanPham/index_ctsp', index_ctsp, name='index_ctsp'),
    path('ChiTietSanPham/SuaCTSP/<str:MaChiTietSP>/', SuaCTSP, name='SuaCTSP'),
    path('ChiTietSanPham/ChiTietCTSP/<str:MaChiTietSP>/', ChiTietCTSP, name='ChiTietCTSP'),
    path('ChiTietSanPham/XoaCTSP/<str:MaChiTietSP>/', XoaCTSP, name='XoaCTSP'),
    # ----------------- Thương hiệu sản phẩm -----------------
    path('ThuongHieuSanPham/ThemTHSP', ThemTHSP, name='ThemTHSP'),
    path('ThuongHieuSanPham/index_thsp', index_thsp, name='index_thsp'),
    path('ThuongHieuSanPham/SuaTHSP/<str:MaThuongHieu>/', SuaTHSP, name='SuaTHSP'),
    path('ThuongHieuSanPham/ChiTietTHSP/<str:MaThuongHieu>/', ChiTietTHSP, name='ChiTietTHSP'),
    path('ThuongHieuSanPham/XoaTHSP/<str:MaThuongHieu>/', XoaTHSP, name='XoaTHSP'),

    # ----------------- Danh mục thương hiệu -----------------
    path('DanhMucThuongHieu/ThemDMTH', ThemDMTH, name='ThemDMTH'),
    path('DanhMucThuongHieu/index_dmth', index_dmth, name='index_dmth'),
    path('DanhMucThuongHieu/SuaDMTH/<str:MaDanhMuc>/', SuaDMTH, name='SuaDMTH'),
    path('DanhMucThuongHieu/ChiTietDMTH/<str:MaDanhMuc>/', ChiTietDMTH, name='ChiTietDMTH'),
    path('DanhMucThuongHieu/XoaDMTH/<str:MaDanhMuc>/', XoaDMTH, name='XoaDMTH'),

    # ----------------- Chi tiết đơn hàng -----------------
    path('ChiTietDH/ThemCTDH', ThemCTDH, name='ThemCTDH'),
    path('ChiTietDH/index_ctdh', index_ctdh, name='index_ctdh'),
    path('ChiTietDH/SuaCTDH/<str:MaCTDH>/', SuaCTDH, name='SuaCTDH'),
    path('ChiTietDH/ChiTietCTDH/<str:MaCTDH>/', ChiTietCTDH, name='ChiTietCTDH'),
    path('ChiTietDH/XoaCTDH/<str:MaCTDH>/', XoaCTDH, name='XoaCTDH'),
    
    # ----------------- Đơn hàng -----------------
    path('DonHang/index_dh', index_dh, name='index_dh'),
    path('DonHang/SuaDH/<str:MaDon>/', SuaDH, name='SuaDH'),
    path('DonHang/ChiTietDH/<str:MaDon>/', ChiTietDH, name='ChiTietDH'),
    path('DonHang/XoaDH/<str:MaDon>/', XoaDH, name='XoaDH'),
    # # ----------------- Tài khoản -----------------
    path('TaiKhoan/index_tk', index_tk, name='index_tk'),
    path('TaiKhoan/ThemTK', ThemTK, name='ThemTK'),
    path('TaiKhoan/SuaTK/<str:IDAC>/', SuaTK, name='SuaTK'),
    path('TaiKhoan/ChiTietTK/<str:IDAC>/', ChiTietTK, name='ChiTietTK'),
    path('TaiKhoan/XoaTK/<str:IDAC>/', XoaTK, name='XoaTK'),
    # # ----------------- Phân quyền -----------------
    path('PhanQuyen/index_pq', index_pq, name='index_pq'),
    path('PhanQuyen/ThemPQ', ThemPQ, name='ThemPQ'),
    path('PhanQuyen/SuaPQ/<str:RoleID>/', SuaPQ, name='SuaPQ'),
    path('PhanQuyen/ChiTietPQ/<str:RoleID>/', ChiTietPQ, name='ChiTietPQ'),
    path('PhanQuyen/XoaPQ/<str:RoleID>/', XoaPQ, name='XoaPQ'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)