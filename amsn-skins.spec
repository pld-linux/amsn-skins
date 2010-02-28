Summary:	Skins for aMSN
Name:		amsn-skins
Version:	0.1
Release:	2
License:	GPL
Group:		Themes
Source0:	http://downloads.sourceforge.net/amsn/amsn-0.98.1.tar.gz
# Source0-md5:	8c608673a4e920b83cc9f41c2cb837dc
Source1:	http://downloads.sourceforge.net/project/amsn/amsn-skins/0.95-skins/aMSN_Live-1.0.tar.gz
# Source1-md5:	5079184f1f75d6b53ca6e7577aa5b66d
URL:		http://www.amsn-project.net/skins.php
Requires:	amsn-skin-aMSN_Live
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/amsn
%define		skinsdir	%{_appdir}/skins

%description
Skins for aMSN.

%package -n amsn-skin-default
Summary:	aMSN default skin: Sapphire Skin
Version:	2.0
License:	GPL
Group:		Themes
URL:		http://www.amsn-project.net/skins.php
Provides:	amsn-skin

%description -n amsn-skin-default
Sapphire Skin by Gustavo A. Diaz.

%package -n amsn-skin-Dark_Matter
Summary:	Dark Matter Skin
Version:	4.0
License:	GPL
Group:		Themes
URL:		http://www.amsn-project.net/skins.php
Provides:	amsn-skin

%description -n amsn-skin-Dark_Matter
Dark Matter Skin for aMSN.

%package -n amsn-skin-aMSN_Live
Summary:	aMSN Live Messenger Skin
Version:	1.0
License:	GPL
Group:		Themes
URL:		http://www.amsn-project.net/skins.php
Provides:	amsn-skin

%description -n amsn-skin-aMSN_Live
WLMSN look alike skin for aMSN.

%prep
%setup -qc -a1

# prep skins
install -d skins
mv amsn-*/skins/default skins
mv amsn-*/skins/'Dark Matter 4.0' skins/Dark_Matter
mv 'aMSN Live-1.0' skins/aMSN_Live

# cleanups
find skins -name 'winicons' | xargs rm -rv
find skins -name '*.xcf' | xargs rm -fv

# standard GPL license
rm skins/aMSN_Live/license
rm skins/default/license
rm skins/Dark_Matter/license

# not part of skin, setting up needs patching amsn itself, besides, seems outdated
rm -rf skins/aMSN_Live/pixmapmenu
rm -rf skins/aMSN_Live/pixmapscroll

find skins '(' -name '*.txt' -o -name '*.xml' -o -name 'license' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'
find skins '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{skinsdir}
cp -a skins/* $RPM_BUILD_ROOT%{skinsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n amsn-skin-default
%defattr(644,root,root,755)
%{skinsdir}/default

%files -n amsn-skin-Dark_Matter
%defattr(644,root,root,755)
%{skinsdir}/Dark_Matter

%files -n amsn-skin-aMSN_Live
%defattr(644,root,root,755)
%{skinsdir}/aMSN_Live
