Name:   rpkg-action
Vendor: ublue-os
Version:  1.0.0
Release:  1%{?dist}
Summary:  Centralized update service/checker made for Universal Blue
License:  Apache-2.0
URL:      https://github.com/%{vendor}/%{name}
# Detailed information about the source Git repository and the source commit
# for the created rpm package
VCS:        git+git@github.com:akdev1l/rpkg-action.git#127d7eb701b56162b5e676f780cdb9345db0a6c9:

# git_dir_pack macro places the repository content (the source files) into a tarball
# and returns its filename. The tarball will be used to build the rpm.
Source:     rpkg-action-127d7eb7.tar.gz

BuildArch:     noarch
Supplements:   rpm-ostree flatpak
BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: black
BuildRequires: ShellCheck
BuildRequires: python-flake8
BuildRequires: python-build
BuildRequires: python-setuptools
BuildRequires: python
BuildRequires: python-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python-setuptools_scm
BuildRequires: python-wheel
Requires: skopeo

%global sub_name %{lua:t=string.gsub(rpm.expand("%{NAME}"), "^ublue%-", ""); print(t)}

%description
Installs and configures ublue-update script, systemd services, and systemd timers for auto update

%prep
env
pwd
%setup -T -b 0 -q -n rpkg-action

%build

%install

%post

%preun

%files

%changelog
%autochangelog
