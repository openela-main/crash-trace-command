%global reponame crash-trace

Summary: Trace extension module for the crash utility
Name: crash-trace-command
Version: 3.0
Release: 6%{?dist}
License: GPLv2
Source: https://github.com/fujitsu/crash-trace/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-trace
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le s390x x86_64
BuildRequires: crash-devel >= 7.2.0-2
BuildRequires: gcc
Requires: trace-cmd
Requires: crash >= 7.2.0-2

Patch0001: 0001-Makefile-set-DT_SONAME-to-trace.so.patch
Patch0002: 0002-Makefile-fix-build-failure-on-aarch64-and-ppc64le.patch

%description
Command for reading ftrace data from a dump file.

%prep
%autosetup -n %{reponame}-%{version}

%build
%make_build

%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions %{_builddir}/%{reponame}-%{version}/trace.so

%files
%dir %{_libdir}/crash
%dir %{_libdir}/crash/extensions
%{_libdir}/crash/extensions/trace.so
%license COPYING

%changelog
* Wed Dec 15 2021 Lianbo Jiang <lijiang@redhat.com> - 3.0-6
- Rebuild for the compatibility issue

* Thu Dec 09 2021 Lianbo Jiang <lijiang@redhat.com> - 3.0-5
- Fix the hardening issue "FAIL: bind-now test because not linked with -Wl,-z,now"

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 3.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Feb 19 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 3.0-2
- Makefile: set DT_SONAME to trace.so
- Makefile: fix build failure on aarch64 and ppc64le
* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 3.0-1
- Initial crash-trace-command package
