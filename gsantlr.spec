Summary:	MIME library for GNUstep
Summary(pl):	Biblioteka MIME dla ¶rodowiska GNUstep
Name:		gsantlr
Version:	0
%define cvs 20041118
Release:	0.%{cvs}.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-cvs-%{cvs}.tar.gz
# Source0-md5:	54210525844ed1d67d45269d6cfc155b
URL:		http://www.gnustepweb.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description

%package devel
Summary:	Header files for gsantlr library
Summary(pl):	Pliki nag³ówkowe biblioteki gsantlr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gsantlr library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gsantlr.

%prep
%setup -q -n %{name}

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
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/*.so
%{_prefix}/System/Library/Headers/%{libcombo}/*
