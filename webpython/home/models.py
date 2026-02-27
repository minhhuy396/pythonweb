from django.db import models


class Phongban(models.Model):
    maphg = models.IntegerField(db_column='MAPHG', primary_key=True)
    tenphg = models.CharField(db_column='TENPHG', max_length=50)
    trphg = models.CharField(db_column='TRPHG', max_length=9, blank=True, null=True)
    ngaynhanchuc = models.DateField(db_column='NGAYNHANCHUC', blank=True, null=True)

    class Meta:
        db_table = 'PHONGBAN'


class Nhanvien(models.Model):
    manv = models.CharField(db_column='MANV', max_length=9, primary_key=True)
    honv = models.CharField(db_column='HONV', max_length=20)
    tennv = models.CharField(db_column='TENNV', max_length=10)
    phai = models.CharField(db_column='PHAI', max_length=3)
    ngsinh = models.DateField(db_column='NGSINH')
    dchi = models.CharField(db_column='DCHI', max_length=100)
    luong = models.FloatField(db_column='LUONG')
    ma_nql = models.CharField(db_column='MA_NQL', max_length=9, blank=True, null=True)
    phg = models.ForeignKey(
        Phongban,
        models.DO_NOTHING,
        db_column='PHG'
    )

    class Meta:
        db_table = 'NHANVIEN'


class Dean(models.Model):
    mada = models.IntegerField(db_column='MADA', primary_key=True)
    tenda = models.CharField(db_column='TENDA', max_length=50)
    ddiem_da = models.CharField(db_column='DDIEM_DA', max_length=50)
    phong = models.ForeignKey(
        Phongban,
        models.DO_NOTHING,
        db_column='PHONG'
    )

    class Meta:
        db_table = 'DEAN'


class Phancong(models.Model):
    manv = models.ForeignKey(
        Nhanvien,
        models.DO_NOTHING,
        db_column='MANV'
    )
    mada = models.ForeignKey(
        Dean,
        models.DO_NOTHING,
        db_column='MADA'
    )
    thoigian = models.FloatField(db_column='THOIGIAN')

    class Meta:
        db_table = 'PHANCONG'
        unique_together = (('manv', 'mada'),)


class Thannhan(models.Model):
    manv = models.ForeignKey(
        Nhanvien,
        models.DO_NOTHING,
        db_column='MANV'
    )
    tentn = models.CharField(db_column='TENTN', max_length=20)
    phai = models.CharField(db_column='PHAI', max_length=3)
    ngsinh = models.DateField(db_column='NGSINH')
    quanhe = models.CharField(db_column='QUANHE', max_length=20)

    class Meta:
        db_table = 'THANNHAN'
        unique_together = (('manv', 'tentn'),)