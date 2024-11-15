#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-R2jags
Version  : 0.8.9
Release  : 35
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/R2jags_0.8-9.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/R2jags_0.8-9.tar.gz
Summary  : Using R to Run 'JAGS'
Group    : Development/Tools
License  : GPL-3.0+
Requires: R-R2WinBUGS
Requires: R-abind
Requires: R-coda
Requires: R-rjags
Requires: R-stringr
BuildRequires : R-R2WinBUGS
BuildRequires : R-abind
BuildRequires : R-coda
BuildRequires : R-rjags
BuildRequires : R-stringr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# R2jags
R2jags: Using R to Run 'JAGS'

%prep
%setup -q -n R2jags
pushd ..
cp -a R2jags buildavx2
popd
pushd ..
cp -a R2jags buildavx512
popd
pushd ..
cp -a R2jags buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731648360

%install
export SOURCE_DATE_EPOCH=1731648360
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R2jags/DESCRIPTION
/usr/lib64/R/library/R2jags/INDEX
/usr/lib64/R/library/R2jags/Meta/Rd.rds
/usr/lib64/R/library/R2jags/Meta/features.rds
/usr/lib64/R/library/R2jags/Meta/hsearch.rds
/usr/lib64/R/library/R2jags/Meta/links.rds
/usr/lib64/R/library/R2jags/Meta/nsInfo.rds
/usr/lib64/R/library/R2jags/Meta/package.rds
/usr/lib64/R/library/R2jags/NAMESPACE
/usr/lib64/R/library/R2jags/R/R2jags
/usr/lib64/R/library/R2jags/R/R2jags.rdb
/usr/lib64/R/library/R2jags/R/R2jags.rdx
/usr/lib64/R/library/R2jags/help/AnIndex
/usr/lib64/R/library/R2jags/help/R2jags.rdb
/usr/lib64/R/library/R2jags/help/R2jags.rdx
/usr/lib64/R/library/R2jags/help/aliases.rds
/usr/lib64/R/library/R2jags/help/paths.rds
/usr/lib64/R/library/R2jags/html/00Index.html
/usr/lib64/R/library/R2jags/html/R.css
/usr/lib64/R/library/R2jags/model/schools.txt
/usr/lib64/R/library/R2jags/tests/testthat.R
/usr/lib64/R/library/R2jags/tests/testthat/test-jags.R
/usr/lib64/R/library/R2jags/tests/testthat/test-jags.parallel.R
