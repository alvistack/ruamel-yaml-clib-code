# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-ruamel-yaml-clib
Epoch: 100
Version: 0.2.6
Release: 2%{?dist}
Summary: C based reader/scanner and emitter for ruamel.yaml
License: MIT
URL: https://pypi.org/project/ruamel.yaml.clib/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package was split of from ruamel.yaml, so that ruamel.yaml can be
build as a universal wheel. Apart from the C code seldom changing, and
taking a long time to compile for all platforms, this allows
installation of the .so on Linux systems under /usr/lib64/pythonX.Y
(without a .pth file or a ruamel directory) and the Python code for
ruamel.yaml under /usr/lib/pythonX.Y.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
mkdir ruamel.yaml.clib
mv *.pyx ruamel.yaml.clib
cythonize -3 ruamel.yaml.clib/*.pyx
mv ruamel.yaml.clib/* .
rmdir ruamel.yaml.clib
%{__python3} setup.py build

%install
%{__python3} setup.py install --single-version-externally-managed --skip-build --root=%{buildroot} --prefix=%{_prefix}
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ruamel.yaml.clib
Summary: C based reader/scanner and emitter for ruamel.yaml
Requires: python3
Provides: python3-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python3dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ruamel.yaml.clib
This package was split of from ruamel.yaml, so that ruamel.yaml can be
build as a universal wheel. Apart from the C code seldom changing, and
taking a long time to compile for all platforms, this allows
installation of the .so on Linux systems under /usr/lib64/pythonX.Y
(without a .pth file or a ruamel directory) and the Python code for
ruamel.yaml under /usr/lib/pythonX.Y.

%files -n python%{python3_version_nodots}-ruamel.yaml.clib
%license LICENSE
%dir %{python3_sitearch}/ruamel
%dir %{python3_sitearch}/ruamel/yaml
%dir %{python3_sitearch}/ruamel/yaml/clib
%{python3_sitearch}/_ruamel_yaml.*.so
%{python3_sitearch}/ruamel.yaml.clib*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ruamel.yaml.clib
Summary: C based reader/scanner and emitter for ruamel.yaml
Requires: python3
Provides: python3-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python3dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}

%description -n python3-ruamel.yaml.clib
This package was split of from ruamel.yaml, so that ruamel.yaml can be
build as a universal wheel. Apart from the C code seldom changing, and
taking a long time to compile for all platforms, this allows
installation of the .so on Linux systems under /usr/lib64/pythonX.Y
(without a .pth file or a ruamel directory) and the Python code for
ruamel.yaml under /usr/lib/pythonX.Y.

%files -n python3-ruamel.yaml.clib
%license LICENSE
%dir %{python3_sitearch}/ruamel
%dir %{python3_sitearch}/ruamel/yaml
%dir %{python3_sitearch}/ruamel/yaml/clib
%{python3_sitearch}/_ruamel_yaml.*.so
%{python3_sitearch}/ruamel.yaml.clib*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-ruamel-yaml-clib
Summary: C based reader/scanner and emitter for ruamel.yaml
Requires: python3
Provides: python3-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python3dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ruamel.yaml.clib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ruamel.yaml.clib) = %{epoch}:%{version}-%{release}

%description -n python3-ruamel-yaml-clib
This package was split of from ruamel.yaml, so that ruamel.yaml can be
build as a universal wheel. Apart from the C code seldom changing, and
taking a long time to compile for all platforms, this allows
installation of the .so on Linux systems under /usr/lib64/pythonX.Y
(without a .pth file or a ruamel directory) and the Python code for
ruamel.yaml under /usr/lib/pythonX.Y.

%files -n python3-ruamel-yaml-clib
%license LICENSE
%dir %{python3_sitearch}/ruamel
%dir %{python3_sitearch}/ruamel/yaml
%dir %{python3_sitearch}/ruamel/yaml/clib
%{python3_sitearch}/_ruamel_yaml.*.so
%{python3_sitearch}/ruamel.yaml.clib*
%endif

%changelog
