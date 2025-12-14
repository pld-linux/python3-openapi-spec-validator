#
# Conditional build:
%bcond_without	tests	# integration tests

Summary:	OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 spec validator
Summary(pl.UTF-8):	Walidator specyfikacji OpenAPI 2.0 (Swagger) i OpenAPI 3.0
Name:		python3-openapi-spec-validator
Version:	0.7.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/openapi-spec-validator/
Source0:	https://files.pythonhosted.org/packages/source/o/openapi-spec-validator/openapi_spec_validator-%{version}.tar.gz
# Source0-md5:	c5bf8550c7f187e12497e4c96f2285f3
URL:		https://pypi.org/project/openapi-spec-validator/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-poetry-core >= 1.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
%if "%{py3_ver}" == "3.8"
BuildRequires:	python3-importlib_resources >= 5.8
%endif
BuildRequires:	python3-jsonschema >= 4.18.0
BuildRequires:	python3-jsonschema-path >= 0.3.1
BuildRequires:	python3-lazy-object-proxy >= 1.7.1
BuildRequires:	python3-openapi-schema-validator >= 0.6.0
BuildRequires:	python3-pytest >= 8.2.2
BuildRequires:	python3-pytest-cov >= 4.1.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
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

%prep
%setup -q -n openapi_spec_validator-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__mv} $RPM_BUILD_ROOT%{_bindir}/openapi-spec-validator{,-3}
ln -sf openapi-spec-validator-3 $RPM_BUILD_ROOT%{_bindir}/openapi-spec-validator

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/openapi-spec-validator-3
%{_bindir}/openapi-spec-validator
%{py3_sitescriptdir}/openapi_spec_validator
%{py3_sitescriptdir}/openapi_spec_validator-%{version}.dist-info
