#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rope
Version  : 0.11.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/52/8d/2ebe70e55742a46813952493f8fc86ff2800ccc105e2dfcb25298f7eeb72/rope-0.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/8d/2ebe70e55742a46813952493f8fc86ff2800ccc105e2dfcb25298f7eeb72/rope-0.11.0.tar.gz
Summary  : a python refactoring library...
Group    : Development/Tools
License  : GPL-2.0
Requires: rope-python3
Requires: rope-license
Requires: rope-python
BuildRequires : buildreq-distutils3

%description
.. _GitHub python-rope / rope: https://github.com/python-rope/rope
========================================
rope, a python refactoring library ...
========================================

%package license
Summary: license components for the rope package.
Group: Default

%description license
license components for the rope package.


%package python
Summary: python components for the rope package.
Group: Default
Requires: rope-python3

%description python
python components for the rope package.


%package python3
Summary: python3 components for the rope package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rope package.


%prep
%setup -q -n rope-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533788718
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/rope
cp COPYING %{buildroot}/usr/share/doc/rope/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/rope/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
