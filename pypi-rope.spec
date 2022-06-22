#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-rope
Version  : 1.2.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/7a/46/412e491b73bb5e906178677917395b6437b7914576a85468fad22d575e32/rope-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/46/412e491b73bb5e906178677917395b6437b7914576a85468fad22d575e32/rope-1.2.0.tar.gz
Summary  : a python refactoring library...
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0-or-later
Requires: pypi-rope-license = %{version}-%{release}
Requires: pypi-rope-python = %{version}-%{release}
Requires: pypi-rope-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. _GitHub python-rope / rope: https://github.com/python-rope/rope
=========================================================================
rope -- the world's most advanced open source Python refactoring library
=========================================================================

%package license
Summary: license components for the pypi-rope package.
Group: Default

%description license
license components for the pypi-rope package.


%package python
Summary: python components for the pypi-rope package.
Group: Default
Requires: pypi-rope-python3 = %{version}-%{release}

%description python
python components for the pypi-rope package.


%package python3
Summary: python3 components for the pypi-rope package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypi-rope package.


%prep
%setup -q -n rope-1.2.0
cd %{_builddir}/rope-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655933042
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rope
cp %{_builddir}/rope-1.2.0/COPYING %{buildroot}/usr/share/package-licenses/pypi-rope/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-rope/a8a12e6867d7ee39c21d9b11a984066099b6fb6b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
