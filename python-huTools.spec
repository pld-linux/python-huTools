
%define		module	huTools

Summary:	huTools - Various tiny tools and toys for Python
Summary(pl.UTF-8):	huTools - zestaw malutkich modułów dla Pythona
Name:		python-%{module}
Version:	0.39p3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://cybernetics.hudora.biz/dist/huTools/huTools-%{version}.tar.gz
# Source0-md5:	2eb653af7e3dfd9d0deb6619043621c0
URL:		http://cybernetics.hudora.biz/projects/wiki/huTools
BuildRequires:	python-devel >= 2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various tiny tools and toys to make Python coding less work more fun.

%description -l pl.UTF-8
Kilka przydatnych mdułów dla Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/calendar
%{py_sitescriptdir}/%{module}/calendar/*.py[co]
%{py_sitescriptdir}/*.egg-info
