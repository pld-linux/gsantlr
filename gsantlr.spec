Summary:	LR parser generator for GNUstep
Summary(pl.UTF-8):	Generator parserów LR dla GNUstepa
Name:		gsantlr
Version:	0
%define cvs 20061113
Release:	0.%{cvs}.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-cvs-%{cvs}.tar.gz
Patch0:	%{name}-buildfix.patch
# Source0-md5:	486669ee86622c1c0152fa2f9d56c25c
URL:		http://www.gnustepweb.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%description
LR parser generator for GNUstep.

%description -l pl.UTF-8
Generator parserów LR dla GNUstepa.

%package devel
Summary:	Header files for gsantlr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gsantlr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gsantlr library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gsantlr.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_prefix}/System/Library/Libraries/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Libraries/*.so
%{_prefix}/System/Library/Headers/*
