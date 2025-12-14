#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-openapi-spec-validator.spec)

Summary:	OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 spec validator
Summary(pl.UTF-8):	Walidator specyfikacji OpenAPI 2.0 (Swagger) i OpenAPI 3.0
Name:		python-openapi-spec-validator
# keep 0.3.x here for python2 support
Version:	0.3.3
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/openapi-spec-validator/
Source0:	https://files.pythonhosted.org/packages/source/o/openapi-spec-validator/openapi-spec-validator-%{version}.tar.gz
# Source0-md5:	1b9fcadfabbaf18af9f9d89624d5351e
URL:		https://pypi.org/project/openapi-spec-validator/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenAPI Spec Validator is a Python library that validates OpenAPI
Specs against the OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0
<https://github.com/OAI/OpenAPI-Specification/blob/master/versions>
specification. The validator aims to check for full compliance with
the Specification.

%description -l pl.UTF-8
OpenAPI Spec Validator to biblioteka Pythona sprawdzająca poprawność
względem specyfikacji OpenAPI 2.0 (Swagger) i OpenAPI 3.0
<https://github.com/swagger-api/swagger-spec/blob/master/versions/>.
Celem walidatora jest sprawdzanie pełnej zgodności ze specyfikacją.

%package -n python3-openapi-spec-validator
Summary:	OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 spec validator
Summary(pl.UTF-8):	Walidator specyfikacji OpenAPI 2.0 (Swagger) i OpenAPI 3.0
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-openapi-spec-validator
OpenAPI Spec Validator is a Python library that validates OpenAPI
Specs against the OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0
<https://github.com/OAI/OpenAPI-Specification/blob/master/versions>
specification. The validator aims to check for full compliance with
the Specification.

%description -n python3-openapi-spec-validator -l pl.UTF-8
OpenAPI Spec Validator to biblioteka Pythona sprawdzająca poprawność
względem specyfikacji OpenAPI 2.0 (Swagger) i OpenAPI 3.0
<https://github.com/swagger-api/swagger-spec/blob/master/versions/>.
Celem walidatora jest sprawdzanie pełnej zgodności ze specyfikacją.

%prep
%setup -q -n openapi-spec-validator-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/openapi-spec-validator{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/openapi-spec-validator{,-3}
ln -sf openapi-spec-validator-3 $RPM_BUILD_ROOT%{_bindir}/openapi-spec-validator
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/openapi-spec-validator-2
%{py_sitescriptdir}/openapi_spec_validator
%{py_sitescriptdir}/openapi_spec_validator-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-openapi-spec-validator
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/openapi-spec-validator-3
%{_bindir}/openapi-spec-validator
%{py3_sitescriptdir}/openapi_spec_validator
%{py3_sitescriptdir}/openapi_spec_validator-%{version}-py*.egg-info
%endif
