#
# crash core analysis suite
#
%global reponame crash-trace

Summary: Trace extension module for the crash utility
Name: crash-trace-command
Version: 3.0
Release: 1%{?dist}
License: GPLv2
Group: Development/Debuggers
Source: https://github.com/fujitsu/crash-trace/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-trace
# Vendor: Fujitsu Limited
# Packager: Qiao Nuohan <qiaonuohan@cn.fujitsu.com>
ExclusiveOS: Linux
ExclusiveArch: x86_64 %{ix86} ppc64 ia64 s390 s390x aarch64 ppc64le
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: zlib-devel lzo-devel snappy-devel
BuildRequires: crash-devel >= 7.2.0-2
Requires: trace-cmd
Requires: crash >= 7.2.0-2

Patch0: 0001-Makefile-set-DT_SONAME-to-trace.so.patch
Patch1: 0002-Makefile-fix-build-failure-on-aarch64-and-ppc64le.patch

%description
Command for reading ftrace data from a dumpfile.

%prep
%setup -q -n %{reponame}-%{version}
%patch0 -p1 -b 0001-Makefile-set-DT_SONAME-to-trace.so.patch
%patch1 -p1 -b 0002-Makefile-fix-build-failure-on-aarch64-and-ppc64le.patch

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/crash/extensions/
cp %{_builddir}/%{reponame}-%{version}/trace.so %{buildroot}%{_libdir}/crash/extensions/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/trace.so
%doc COPYING

%changelog
* Fri Nov 18 2022 Lianbo Jiang <lijiang@redhat.com> - 3.0-1
- Rebase to upstream v3.0
- Update to the latest upstream commit
  Resolves: rhbz#2119709

* Mon Feb 08 2021 Lianbo Jiang <lijiang@redhat.com> - 2.0-18
- Rename trace_buffer to array_buffer
- Rename ring_buffer to trace_buffer
  Resolves: rhbz#1925907

* Mon Jul 27 2020 Bhupesh Sharma <bhsharma@redhat.com> - 2.0-17
- Chnage Source/URL to point to the latest github location
  Resolves: rhbz#1851746

* Tue Apr 28 2019 Dave Anderson <anderson@redhat.com> - 2.0-16
- Fix for RHEL7 ftrace_event_call data structure change
  Resolves: rhbz#1827734

* Wed Sep 19 2018 Dave Anderson <anderson@redhat.com> - 2.0-15
- annocheck: link with -Wl,-z,now
  Resolves: rhbz#1630558

* Mon Aug 13 2018 Dave Anderson <anderson@redhat.com> - 2.0-14
- Bump release for mass rebuild
  Resolves: rhbz#1615511

* Wed Dec  6 2017 Dave Anderson <anderson@redhat.com> - 2.0.13
- Build requires crash-devel-7.2.0-2 and usage requires crash-7.2.0-2
  because of load_module structure change.
  Resolves: rhbz#1520825

* Sun Apr 16 2017 Dave Anderson <anderson@redhat.com> - 2.0.12
- Differentiate ppc64 .ring_buffer_read text symbol from ring_buffer_read data symbol
- Fix for ring_buffer_per_cpu.nr_pages size change on big-endian systems 
- Fix for Linux 4.7 change to the TRACE_EVENT_FL_TRACEPOINT flag
  Resolves: rhbz#1441914
  Resolves: rhbz#1440726

* Thu Feb 25 2016 Dave Anderson <anderson@redhat.com> - 2.0-10
- Fix for ftrace symbol name changes in Linux 4.2 
  Resolves: rhbz#1265553

* Tue Sep 02 2014 Dave Anderson <anderson@redhat.com> - 2.0-9
- Add ppc64le support.
  Resolves: rhbz#1123995

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.0-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.0-7
- Mass rebuild 2013-12-27

* Thu Dec  5 2013 Dave Anderson <anderson@redhat.com> - 2.0-6
- Add Linux 3.10 support.
  Resolves: rhbz#863833

* Tue Nov 12 2013 Dave Anderson <anderson@redhat.com> - 2.0-5
- Add ARM64 support.
  Resolves: rhbz#1028580

* Tue Aug 20 2013 Dave Anderson <anderson@redhat.com> - 2.0-4
- crash utility has added LZO and snappy compression in addition to zlib

* Wed May 29 2013 Dave Anderson <anderson@redhat.com> - 2.0-3
- Replace obsolete _init() and _fini() functions.
- Fix possible segmentation violation on calloc() failure.
- Initialize trace_dat to avoid compiler warning.

* Mon Nov 26 2012 Dave Anderson <anderson@redhat.com> - 2.0-2
- trace-cmd package required
- rpmlint cleanups to this file 
- fix compiler warnings for trace.c

* Wed Nov  21 2012 Qiao Nuohan <qiaonuohan@cn.fujitsu.com> - 2.0-1
- update code
  Resolves: rhbz#863833

* Wed Feb  8 2012 Dave Anderson <anderson@redhat.com> - 1.0-4
- Build with RPM_OPT_FLAGS.
  Resolves: rhbz#729018

* Wed Jun  9 2010 Dave Anderson <anderson@redhat.com> - 1.0-3
- Remove trace_dump.patch, which requires a kernel later than
  the RHEL6 base of 2.6.32.
  Resolves: rbhz#601536

* Mon May 24 2010 Dave Anderson <anderson@redhat.com> - 1.0-2
- Fix for segmentation violation with "trace show -c cpu" command,
  and add "trace dump -t" command.
  Resolves: rbhz#592887

* Wed Dec 09 2009 Dave Anderson <anderson@redhat.com> - 1.0-1.2
- fix Makefile to account for s390 build
- change exclusive arch entry from i386 to {ix86}
- Resolves: rbhz#545564

* Tue Dec 08 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-1.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009  Dave Anderson <anderson@redhat.com>
- Initial crash-trace-command package

