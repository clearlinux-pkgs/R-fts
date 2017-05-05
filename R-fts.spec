#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fts
Version  : 0.9.9
Release  : 6
URL      : https://cran.r-project.org/src/contrib/fts_0.9.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fts_0.9.9.tar.gz
Summary  : R interface to tslib (a time series library in c++)
Group    : Development/Tools
License  : GPL-3.0
Requires: R-fts-lib
Requires: R-BH
Requires: R-zoo
BuildRequires : R-BH
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-fts package.
Group: Libraries

%description lib
lib components for the R-fts package.


%prep
%setup -q -c -n fts

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492797208

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492797208
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fts
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fts


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fts/DESCRIPTION
/usr/lib64/R/library/fts/INDEX
/usr/lib64/R/library/fts/Meta/Rd.rds
/usr/lib64/R/library/fts/Meta/features.rds
/usr/lib64/R/library/fts/Meta/hsearch.rds
/usr/lib64/R/library/fts/Meta/links.rds
/usr/lib64/R/library/fts/Meta/nsInfo.rds
/usr/lib64/R/library/fts/Meta/package.rds
/usr/lib64/R/library/fts/NAMESPACE
/usr/lib64/R/library/fts/R/fts
/usr/lib64/R/library/fts/R/fts.rdb
/usr/lib64/R/library/fts/R/fts.rdx
/usr/lib64/R/library/fts/help/AnIndex
/usr/lib64/R/library/fts/help/aliases.rds
/usr/lib64/R/library/fts/help/fts.rdb
/usr/lib64/R/library/fts/help/fts.rdx
/usr/lib64/R/library/fts/help/paths.rds
/usr/lib64/R/library/fts/html/00Index.html
/usr/lib64/R/library/fts/html/R.css
/usr/lib64/R/library/fts/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fts/libs/fts.so
