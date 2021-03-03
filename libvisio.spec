#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvisio
Version  : 0.1.7
Release  : 9
URL      : https://dev-www.libreoffice.org/src/libvisio-0.1.7.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libvisio-0.1.7.tar.xz
Summary  : Library for parsing the visio file format structure
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libvisio-bin = %{version}-%{release}
Requires: libvisio-lib = %{version}-%{release}
Requires: libvisio-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : gperf
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : sed

%description
libvisio is a library and a set of tools for reading and converting MS
Visio diagrams.

%package bin
Summary: bin components for the libvisio package.
Group: Binaries
Requires: libvisio-license = %{version}-%{release}

%description bin
bin components for the libvisio package.


%package dev
Summary: dev components for the libvisio package.
Group: Development
Requires: libvisio-lib = %{version}-%{release}
Requires: libvisio-bin = %{version}-%{release}
Provides: libvisio-devel = %{version}-%{release}
Requires: libvisio = %{version}-%{release}

%description dev
dev components for the libvisio package.


%package doc
Summary: doc components for the libvisio package.
Group: Documentation

%description doc
doc components for the libvisio package.


%package lib
Summary: lib components for the libvisio package.
Group: Libraries
Requires: libvisio-license = %{version}-%{release}

%description lib
lib components for the libvisio package.


%package license
Summary: license components for the libvisio package.
Group: Default

%description license
license components for the libvisio package.


%prep
%setup -q -n libvisio-0.1.7
cd %{_builddir}/libvisio-0.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592624865
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1592624865
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvisio
cp %{_builddir}/libvisio-0.1.7/COPYING.MPL %{buildroot}/usr/share/package-licenses/libvisio/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vsd2raw
/usr/bin/vsd2text
/usr/bin/vsd2xhtml
/usr/bin/vss2raw
/usr/bin/vss2text
/usr/bin/vss2xhtml

%files dev
%defattr(-,root,root,-)
/usr/include/libvisio-0.1/libvisio/VisioDocument.h
/usr/include/libvisio-0.1/libvisio/libvisio.h
/usr/lib64/libvisio-0.1.so
/usr/lib64/pkgconfig/libvisio-0.1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libvisio/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvisio-0.1.so.1
/usr/lib64/libvisio-0.1.so.1.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvisio/9744cedce099f727b327cd9913a1fdc58a7f5599
