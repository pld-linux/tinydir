Summary:	Lightweight, portable and easy to integrate C directory and file reader
Summary(pl.UTF-8):	Lekka, przenośna i łatwa w integracji biblioteka C do odczytu katalogów i plików
Name:		tinydir
Version:	1.2.5
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/cxong/tinydir/releases
Source0:	https://github.com/cxong/tinydir/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bdb6716f92999fe6ddeaf0a3307b63b2
URL:		https://github.com/cxong/tinydir
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight, portable and easy to integrate C directory and file
reader. TinyDir wraps dirent for POSIX and FindFirstFile for Windows.

%description -l pl.UTF-8
Lekka, przenośna i łatwa w integracji biblioteka do odczytu katalogów
i plików w C. TinyDir obudowuje API dirent dla systemów zgodnych z
POSIX oraz FindFirstFile dla Windows.

%package devel
Summary:	Lightweight, portable and easy to integrate C directory and file reader
Summary(pl.UTF-8):	Lekka, przenośna i łatwa w integracji biblioteka C do odczytu katalogów i plików
Group:		Development/Libraries

%description devel
Lightweight, portable and easy to integrate C directory and file
reader. TinyDir wraps dirent for POSIX and FindFirstFile for Windows.

%description devel -l pl.UTF-8
Lekka, przenośna i łatwa w integracji biblioteka do odczytu katalogów
i plików w C. TinyDir obudowuje API dirent dla systemów zgodnych z
POSIX oraz FindFirstFile dla Windows.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_examplesdir}/%{name}-%{version}}

cp -p tinydir.h $RPM_BUILD_ROOT%{_includedir}
cp -p samples/*.{c,cpp,txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING README.md
%{_includedir}/tinydir.h
%{_examplesdir}/%{name}-%{version}
