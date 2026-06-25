import pandas as pd
import pybdsim
import pytest
import os

SAMPLER_CONFIGS = {
    "name": [
        "0p5",
        "1p0",
        "2p0",
        "5p0",
    ],
    "SAMPLER_SIZE_X": [
        "0.5",
        "1.0",
        "2.0",
        "5.0",
    ],
    "SAMPLER_SIZE_Y": [
        "0.5",
        "1.0",
        "2.0",
        "5.0",
    ],
}

configs = pd.DataFrame(SAMPLER_CONFIGS).to_dict(orient="records")

simulation_results = {}


@pytest.mark.parametrize("config", configs, ids=[c["name"] for c in configs])
def test_trajectory_volume(config):

    os.chdir(os.path.dirname(__file__))

    base_name = f"trajectory_storeSamplerID_{config['name']}"
    template_name = "trajectory_volume.tpl"
    gmad_name = base_name + ".gmad"
    root_name = base_name + ".root"

    params = {
        "SAMPLER_SIZE_X": config["SAMPLER_SIZE_X"],
        "SAMPLER_SIZE_Y": config["SAMPLER_SIZE_Y"],
    }

    print("name ", config["name"])
    print("SAMPLER_SIZE_X ", config["SAMPLER_SIZE_X"])
    print("SAMPLER_SIZE_y ", config["SAMPLER_SIZE_Y"])

    ngenerate = 2

    pybdsim.Run.RenderGmadJinjaTemplate(template_name, gmad_name, params)
    pybdsim.Run.Bdsim(gmad_name, base_name, ngenerate, 1)

    data = pybdsim.DataPandas.BDSIMOutput(root_name)

    ntraj = 0
    for i in range(ngenerate):
        traj = data.get_trajectories(i)
        ntraj += len(traj)

    print(ntraj )
    simulation_results[config["name"]] = ntraj


def test_trajectory_volume_ordering():

    assert simulation_results["0p5"] < simulation_results["1p0"]
    assert simulation_results["1p0"] < simulation_results["2p0"]
    assert simulation_results["2p0"] < simulation_results["5p0"]