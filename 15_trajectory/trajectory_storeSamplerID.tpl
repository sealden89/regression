d1: drift, l=30*cm;

t1: target, l=10*cm, material="tungsten";

s1: samplerplacement, z=1*m,
                      shape="rectangular",
                      aper1={{ SAMPLER_SIZE_X }}*m, aper2={{ SAMPLER_SIZE_Y }}*m;

l1: line = (d1, t1, d1);

use, l1;

beam, particle="proton",
      energy=1*TeV;

sample, all;

option, physicsList="g4FTFP_BERT",
        defaultRangeCut=1*cm;

option,storeTrajectory=1,
    storeTrajectorySamplerID="s1";