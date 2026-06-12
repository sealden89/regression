import pytest
import pybdsim
import numpy as np
import os

def test() :

    os.chdir(os.path.dirname(__file__))
    
    base_name     = "trajectory_base"
    template_name = base_name+".tpl"
    gmad_name     = base_name+".gmad"
    root_name     = base_name+".root"

    params = {
        'ENERGY': '250',
        'L1' : '0.5',
        'L2' : '1.0',
    }
    ngenerate = 1

    pybdsim.Run.RenderGmadJinjaTemplate(template_name,gmad_name,params)
    pybdsim.Run.Bdsim(gmad_name,base_name,ngenerate,1)

    data = pybdsim.DataPandas.BDSIMOutput(root_name)
    n_steps_expected = 30
    traj = data.get_trajectories(ngenerate-1)
    nsteps = traj['nstep'][0]
    number_particles = len(traj)

    assert(number_particles == ngenerate)
    assert(n_steps_expected == nsteps)    






    



