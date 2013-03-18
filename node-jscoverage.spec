%define _unpackaged_files_terminate_build 0
%define major 0
%define minor 4
%define tag 36b3ba5
%define srcdir visionmedia-node-jscoverage-%{tag}
Release: 1

Summary: Secure Sockets Layer and cryptography libraries and tools
Name: node-jscoverage
Version: %{major}.%{minor}
Source0: https://github.com/visionmedia/node-jscoverage/tarball/master/36baba5
License: GPL2
URL: https://github.com/visionmedia/node-jscoverage/
Packager: Peter Janes <peter.janes@ek3.com>
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
JScoverage for node.

%prep

%setup -q -n %{srcdir}

%build 

./configure --prefix $RPM_BUILD_ROOT/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_PREFIX="$RPM_BUILD_ROOT/usr" install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(0644,root,root,0755)

%attr(0755,root,root) /usr/bin/*
%attr(0644,root,root) /usr/share/man/man1/*
