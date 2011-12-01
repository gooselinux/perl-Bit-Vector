Name:           perl-Bit-Vector
Version:        7.1
Release:        2%{?dist}
Summary:        Efficient bit vector, set of integers and "big int" math library

Group:          Development/Libraries
# Clarified by a private mail from the author:
License:        (GPLv2+ or Artistic) and LGPLv2+
URL:            http://search.cpan.org/dist/Bit-Vector/
Source0:        http://www.cpan.org/authors/id/S/ST/STBEY/Bit-Vector-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(Carp::Clan) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Bit::Vector is an efficient C library which allows you to handle bit
vectors, sets (of integers), "big integer arithmetic" and boolean
matrices, all of arbitrary sizes.

The library is efficient (in terms of algorithmical complexity) and
therefore fast (in terms of execution speed) for instance through the
widespread use of divide-and-conquer algorithms.


%prep
%setup -q -n Bit-Vector-%{version} 
chmod 644 examples/*.pl
%{__perl} -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' examples/benchmk1.pl
%{__perl} -pi -e 's|^#!perl\b|#!%{__perl}|' \
    examples/{benchmk{2,3},primes,SetObject}.pl

# Filter unwanted Provides:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
  sed -e '/perl(Bit::Vector)$/d'
EOF

%define __perl_provides %{_builddir}/Bit-Vector-%{version}/%{name}-prov
chmod +x %{__perl_provides}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Artistic.txt GNU_GPL.txt GNU_LGPL.txt
%doc CHANGES.txt CREDITS.txt README.txt examples/
%{perl_vendorarch}/Bit/
%{perl_vendorarch}/auto/Bit/
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 7.1-2
- rebuild against perl 5.10.1

* Fri Oct  2 2009 Stepan Kasal <skasal@redhat.com> - 7.1-2
- fixed the license tag

* Thu Oct  1 2009 Stepan Kasal <skasal@redhat.com> - 7.1-1
- new upstream release

* Tue Aug  4 2009 Stepan Kasal <skasal@redhat.com> - 6.6-1
- new upstream release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 6.4-8
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.4-7
- Autorebuild for GCC 4.3

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 6.4-6
- fix license tag, rebuild for new perl

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 6.4-5
- Rebuild for selinux ppc32 issue.

* Fri Jul 06 2007 Robin Norwood <rnorwood@redhat.com> 6.4-4
- Resolves: rhbz#247212
- Fix broken perl_provides script - it was removing both the versioned
  and unversioned Provides: perl(Bit::Vector)

* Sat Jun 30 2007 Steven Pritchard <steve@kspei.com> 6.4-3
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Remove check macro cruft.
- Improve Summary.
- Remove redundant perl build dependency.
- BR ExtUtils::MakeMaker.
- Set OPTIMIZE when we run Makefile.PL, not make.
- BR perl(Carp::Clan) instead of perl-Carp-Clan.
- Remove redundant Carp::Clan dependency.
- Filter unversioned Provides: perl(Bit::Vector)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.4-2.2.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6.4-2.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6.4-2.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 6.4-2.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sat Apr  2 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 6.4-1
- Update to 6.4.
- Bring up to date with current Fedora.Extras perl spec template.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 6.3-1
- update to 6.3

* Wed Jul 16 2003 Elliot Lee <sopwith@redhat.com> 
- Rebuild, remove unpackaged files

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Aug 15 2002 Chip Turner <cturner@redhat.com>
- file list fix for Clan stuff

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Wed Jan 30 2002 cturner@redhat.com
- Specfile autogenerated

