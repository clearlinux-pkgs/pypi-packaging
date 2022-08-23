#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-packaging
Version  : 21.3
Release  : 68
URL      : https://files.pythonhosted.org/packages/df/9e/d1a7217f69310c1db8fdf8ab396229f55a699ce34a203691794c5d1cad0c/packaging-21.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/9e/d1a7217f69310c1db8fdf8ab396229f55a699ce34a203691794c5d1cad0c/packaging-21.3.tar.gz
Summary  : Core utilities for Python packages
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: pypi-packaging-license = %{version}-%{release}
Requires: pypi-packaging-python = %{version}-%{release}
Requires: pypi-packaging-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
packaging
=========
.. start-intro
Reusable core utilities for various Python Packaging
`interoperability specifications <https://packaging.python.org/specifications/>`_.

%package license
Summary: license components for the pypi-packaging package.
Group: Default

%description license
license components for the pypi-packaging package.


%package python
Summary: python components for the pypi-packaging package.
Group: Default
Requires: pypi-packaging-python3 = %{version}-%{release}

%description python
python components for the pypi-packaging package.


%package python3
Summary: python3 components for the pypi-packaging package.
Group: Default
Requires: python3-core
Provides: pypi(packaging)
Requires: pypi(pyparsing)

%description python3
python3 components for the pypi-packaging package.


%prep
%setup -q -n packaging-21.3
cd %{_builddir}/packaging-21.3
pushd ..
cp -a packaging-21.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656392525
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . pyparsing
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . pyparsing
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-packaging
cp %{_builddir}/packaging-21.3/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-packaging/598f87f072f66e2269dd6919292b2934dbb20492
cp %{_builddir}/packaging-21.3/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-packaging/fdc0e4eabc45522b079deff7d03d70528d775dc0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} pyparsing
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-packaging/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-packaging/fdc0e4eabc45522b079deff7d03d70528d775dc0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
