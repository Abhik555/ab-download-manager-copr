Name:           ab-download-manager
Version:        1.10.1
Release:        %autorelease
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

# Upstream GitHub release archive.
Source0:        https://github.com/amir1376/ab-download-manager/releases/download/v%{version}/ABDownloadManager_%{version}_linux_%{upstream_arch}.tar.gz

# Upstream license.
Source1:        https://raw.githubusercontent.com/amir1376/ab-download-manager/v%{version}/LICENSE

# Fedora desktop entry.
Source2:        %{name}.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  findutils

%description
AB Download Manager is a fast and modern download manager for Linux.
It provides download acceleration, download queues, scheduling, browser
integration, multiple themes, and a modern graphical interface.

%prep
%setup -q -n ABDownloadManager

%build
# AB Download Manager is distributed upstream as a prebuilt Linux
# application. No compilation is required.

%install
rm -rf %{buildroot}

# Install the complete upstream application.
install -d %{buildroot}%{_libdir}/%{name}

cp -a . \
    %{buildroot}%{_libdir}/%{name}/

# Main executable.
chmod 0755 \
    %{buildroot}%{_libdir}/%{name}/bin/ABDownloadManager

# Command available in PATH.
install -d %{buildroot}%{_bindir}

ln -s \
    %{_libdir}/%{name}/bin/ABDownloadManager \
    %{buildroot}%{_bindir}/ab-download-manager

# Desktop entry.
install -d %{buildroot}%{_datadir}/applications

install -p -m 0644 \
    %{SOURCE2} \
    %{buildroot}%{_datadir}/applications/ab-download-manager.desktop

# Application icon.
install -d \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

install -p -m 0644 \
    %{buildroot}%{_libdir}/%{name}/lib/ABDownloadManager.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

# License.
install -d \
    %{buildroot}%{_licensedir}/%{name}

install -p -m 0644 \
    %{SOURCE1} \
    %{buildroot}%{_licensedir}/%{name}/LICENSE

%check
# Validate desktop entry.
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/ab-download-manager.desktop

# Validate main executable.
test -x \
    %{buildroot}%{_libdir}/%{name}/bin/ABDownloadManager

# Validate icon.
test -f \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

# Validate application directory.
test -d \
    %{buildroot}%{_libdir}/%{name}/bin

test -d \
    %{buildroot}%{_libdir}/%{name}/lib

%files
%license %{_licensedir}/%{name}/LICENSE

%{_bindir}/ab-download-manager
%{_libdir}/%{name}/
%{_datadir}/applications/ab-download-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

%changelog
%autochangelog
```
