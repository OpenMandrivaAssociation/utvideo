%define	major	%{version}
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	Ut Video codec suite
Name:		utvideo
Version:	14.2.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.xz
Patch0:		utvideo-14.2.0-add-missing-linkage-agaist-pthread.patch

%description
Ut Video Codec Suite is a multi-platform and multi-interface lossless
video codec.

%package -n	%{libname}
Summary:	Ut Video codec suite
Group:		System/Libraries

%description -n	%{libname}
Ut Video Codec Suite is a multi-platform and multi-interface lossless
video codec.

%package -n	%{devname}
Summary:	Header files for Ut Video library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Header files for Ut Video library.

%prep
%setup -q
%patch0 -p1 .lpthread~
cp -af %{_datadir}/automake*/* .

%build
./configure	--enable-shared \
		--disable-static \
		--enable-debug \
		--optlevel=fast \
		--enable-asm=x64  \
		--extra-ldflags="%{ldflags}" \
		--extra-cxxflags="%{optflags} -Ofast"

%make

%install
%makeinstall_std libdir=%{_libdir} prefix=%{_prefix}

%files -n  %{libname}
%doc readme.en.html
%lang(ja) %doc readme.ja.html
%{_libdir}/libutvideo.so.%{major}

%files -n %{devname}
%{_libdir}/libutvideo.so
%{_includedir}/utvideo
%{_libdir}/pkgconfig/libutvideo.pc
