%define	major	%{version}
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	Ut Video codec suite
Name:		utvideo
Version:	16.1.0
Release:	2
License:	GPLv2+
Group:		System/Libraries
Source0:	http://umezawa.dyndns.info/archive/utvideo/utvideo-%{version}-src.zip
Patch0:		utvideo-16.1.0-compile.patch
# Based on the scripts found in the 14.2.0 tarball of unknown origins
Source10:	configure
Source11:	GNUmakefile

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
%autopatch -p1
cp -af %{_datadir}/automake*/* %{SOURCE10} %{SOURCE11} .

%build
./configure	--enable-shared \
		--disable-static \
		--enable-debug \
		--optlevel=fast \
%ifarch x86_64
		--enable-asm=x64  \
%endif
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
