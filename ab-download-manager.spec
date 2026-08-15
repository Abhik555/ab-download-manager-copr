Name:           ab-download-manager
Version:        1.10.1
Release:        1%{?dist}
Summary:        Fast and modern download manager

License:        Apache-2.0
URL:            https://github.com/amir1376/ab-download-manager

ExclusiveArch:  x86_64 aarch64

%ifarch x86_64
%global upstream_arch x64
%endif
%ifarch aarch64
%global upstream_arch arm64
%endif

Source0:        https://github.com/amir1376/ab-download-manager/releases/download/v%{version}/ABDownloadManager_%{version}_linux_%{upstream_arch}.tar.gz
Source1:        https://raw.githubusercontent.com/amir1376/ab-download-manager/v%{version}/LICENSE
Source2:        %{name}.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme

%description
AB Download Manager is a fast and modern download manager for Linux.
It provides download acceleration, queues, scheduling, browser integration,
multiple themes, and a modern graphical interface.

%prep
%setup -q -n ABDownloadManager

%build
# The upstream Linux release is distributed as a prebuilt application.
# No compilation is required here.

%install
rm -rf %{buildroot}

# Install the complete upstream application into a private directory.
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a . %{buildroot}%{_libdir}/%{name}/

# Ensure the main executable has the correct mode.
chmod 0755 %{buildroot}%{_libdir}/%{name}/bin/ABDownloadManager

# Provide a normal command in PATH.
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/bin/ABDownloadManager \
    %{buildroot}%{_bindir}/ab-download-manager

# Install the desktop entry.
mkdir -p %{buildroot}%{_datadir}/applications

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE2}

# Install the upstream application icon into the standard hicolor theme.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

install -p -m 0644 \
    %{buildroot}%{_libdir}/%{name}/lib/ABDownloadManager.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

# Install the upstream license.
mkdir -p %{buildroot}%{_licensedir}/%{name}

install -p -m 0644 \
    %{SOURCE1} \
    %{buildroot}%{_licensedir}/%{name}/LICENSE

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/ab-download-manager.desktop

test -x %{buildroot}%{_libdir}/%{name}/bin/ABDownloadManager
test -f %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

%files
%license %{_licensedir}/%{name}/LICENSE

%{_bindir}/ab-download-manager
%{_libdir}/%{name}/
%{_datadir}/applications/ab-download-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

%changelog
* Sat Aug 15 2026 Abhik555 <abhik555@hotmail.com> - 1.10.1-1
- Initial COPR package for AB Download Manager
