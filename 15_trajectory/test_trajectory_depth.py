import pandas as pd
import pybdsim
import pytest
import os

TRAJECTORY_CONFIGS = {
    "name": [
        "none",
        "primary",
        "all",
    ],
    "STORE_TRAJECTORIES": [
        "0",
        "1",
        "1",
    ],
    "STORE_SECONDARIES": [
        "0",
        "0",
        "1",
    ],
    "STORE_DEPTH": [
        "0",
        "0",
        "-1",
    ],
}

configs = pd.DataFrame(TRAJECTORY_CONFIGS).to_dict(orient="records")

simulation_results = {}


@pytest.mark.parametrize("config", configs, ids=[c["name"] for c in configs])
def test_trajectory_storage(config):

    os.chdir(os.path.dirname(__file__))

    base_name = f"trajectory_depth_{config['name']}"
    template_name = "trajectory_depth.tpl"
    gmad_name = base_name + ".gmad"
    root_name = base_name + ".root"

    params = {
        "STORE_TRAJECTORIES": config["STORE_TRAJECTORIES"],
        "STORE_SECONDARIES": config["STORE_SECONDARIES"],
        "STORE_DEPTH": config["STORE_DEPTH"],
    }

    ngenerate = 10

    pybdsim.Run.RenderGmadJinjaTemplate(template_name, gmad_name, params)
    pybdsim.Run.Bdsim(gmad_name, base_name, ngenerate, 1)

    data = pybdsim.DataPandas.BDSIMOutput(root_name)

    ntraj = 0
    for i in range(ngenerate):
        traj = data.get_trajectories(i)
        ntraj += len(traj)

    simulation_results[config["name"]] = ntraj

    if config["name"] == "none":
        assert ntraj == 0


def test_trajectory_storage_ordering():

    assert simulation_results["none"] == 0

    # one primary per event
    assert simulation_results["primary"] > 0

    # should include secondaries / tertiaries
    assert simulation_results["all"] > simulation_results["primary"]
