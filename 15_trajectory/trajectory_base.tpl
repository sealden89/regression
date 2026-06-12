! the basic lattice for all trajectory tests
! a short drift followed by a 1m block of copper that a 250MeV
! e- beam smashes into

d1: drift, l={{ L1 }}*m;
d2: drift, l={{ L2 }}*m;
d3: drift, l=0.5*m;
d4: drift, l=0.5*m;
THINOCTUPOLE1 : thinmultipole , knl={ 0,0,1 } , ksl={ 0,0,0 };
l1: line=(d1,d2,THINOCTUPOLE1,d3,d4);
use, l1;

beam, particle="e-",
      energy={{ ENERGY }}*MeV;


option, storeTrajectories=1;

!s1: samplerplacement, z=0.4*m,
!                      shape="rectangular",
!                      aper1=1*m, aper2=1*m;

!s2: samplerplacement, referenceElement="d2",
!                      x=0*cm, y=0*cm, s=0*cm,
!                      axisAngle=0, axisY=0, angle=0,
!                      aper1=10*cm;

sample, all;