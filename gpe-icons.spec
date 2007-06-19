Summary:	GPE icons
Summary(pl.UTF-8):	Ikony GPE
Name:		gpe-icons
Version:	0.25
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	9845af06d8337fa41725c731ba3dab08
URL:		http://gpe.linuxtogo.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE icons.

%description -l pl.UTF-8
Ikony GPE.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/gpe
%dir %{_datadir}/gpe/pixmaps
%{_datadir}/gpe/pixmaps/*.png
%dir %{_datadir}/gpe/pixmaps/default
%{_datadir}/gpe/pixmaps/default/*.png
