Name:           ab-download-manager
Version:        1.10.1
Release:        %autorelease
Summary:        Fast and modern download manager

License:        Apache-2.0
URL:            https://github.com/amir1376/ab-download-manager

ExclusiveArch:  x86_64 aarch64

Source0:        ABDownloadManager_%{version}_linux_x64.tar.gz
Source1:        ABDownloadManager_%{version}_linux_arm64.tar.gz
Source2:        %{name}.desktop
Source3:        LICENSE

BuildRequires:  desktop-file-utils

%description
AB Download Manager is a fast and modern download manager for Linux.
It provides download acceleration, download queues, scheduling, browser
integration, multiple themes, and a modern graphical interface.

%prep
rm -rf %{_builddir}/ab-download-manager

mkdir -p %{_builddir}/ab-download-manager

%ifarch x86_64
tar -xzf %{SOURCE0} \
    -C %{_builddir}/ab-download-manager \
    --strip-components=1
%endif

%ifarch aarch64
tar -xzf %{SOURCE1} \
    -C %{_builddir}/ab-download-manager \
    --strip-components=1
%endif

%build
# AB Download Manager is distributed upstream as a prebuilt Linux
# application. No compilation is required.

%install
rm -rf %{buildroot}

install -d \
    %{buildroot}%{_libdir}/%{name}

cp -a \
    %{_builddir}/ab-download-manager/. \
    %{buildroot}%{_libdir}/%{name}/

# Main executable
chmod 0755 \
    %{buildroot}%{_libdir}/%{name}/bin/ABDownloadManager

# Command available in PATH
install -d \
    %{buildroot}%{_bindir}

ln -s \
    %{_libdir}/%{name}/bin/ABDownloadManager \
    %{buildroot}%{_bindir}/ab-download-manager

# Desktop entry
install -d \
    %{buildroot}%{_datadir}/applications

install -p -m 0644 \
    %{SOURCE2} \
    %{buildroot}%{_datadir}/applications/ab-download-manager.desktop

# Icon
install -d \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

install -p -m 0644 \
    %{buildroot}%{_libdir}/%{name}/lib/ABDownloadManager.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

# License
install -d \
    %{buildroot}%{_licensedir}/%{name}

install -p -m 0644 \
    %{SOURCE3} \
    %{buildroot}%{_licensedir}/%{name}/LICENSE

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/ab-download-manager.desktop

test -x \
    %{buildroot}%{_libdir}/%{name}/bin/ABDownloadManager

test -f \
    %{buildroot}%{_libdir}/%{name}/lib/ABDownloadManager.png

%files
%license %{_licensedir}/%{name}/LICENSE

%{_bindir}/ab-download-manager
%{_libdir}/%{name}/
%{_datadir}/applications/ab-download-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/ab-download-manager.png

%changelog
%autochangelog
